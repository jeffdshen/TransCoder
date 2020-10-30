import re
from enum import Enum
import io
import tokenize
import sacrebleu


ESCAPE = ("___", "____")


# token_name = (escape for token, token substitution, token)
# " " -> "_" -> "__" -> "___"
# "___*" -> "____*"
# "<token>" -> "___N"
class SpecialToken(Enum):
    CO_DEF_START = ("___0", "Disassembly of ", "CO_DEF_START")
    CO_START = ("___1", "<code object ", "CO_START")
    CO_MEMORY = ("___2", " at ", "CO_MEMORY")
    CO_LINE = ("___3", ', file "<dis>", line ', "CO_LINE")
    CO_END = ("___4", ">", "CO_END")
    CO_DEF_END = ("___5", ":", "CO_DEF_END")
    NEW_LINE = ("___N", "\n", "NEW_LINE")
    STR_SPACE = ("__", " ", "_")
    UNDERSCORE = ("___", "_", "__")


def interleave(*args):
    return [item for t in zip(*args) for item in t]


def split_and_keep(s, sep):
    t = s.split(sep)
    result = interleave(t, [sep] * len(t))
    if len(result) > 0:
        result.pop()
    return result


def escape_token(token):
    if isinstance(token, SpecialToken):
        return token.value[2]

    if token.startswith(ESCAPE[0]):
        return ESCAPE[1] + token[len(ESCAPE[0]) :]

    for sp in SpecialToken:
        if token == sp.value[2]:
            return sp.value[0]

    return token


def tokenize_dis(bytecode):
    if bytecode is None:
        return None
    assert isinstance(bytecode, str)

    split_bytecode = split_and_keep(
        bytecode.replace("\r\n", "\n").replace("\r", "\n"), "\n"
    )

    tokens = []
    for line in split_bytecode:
        res = tokenize_line(line)
        if res is None:
            return None
        tokens += res

    escaped_tokens = []
    for token in tokens:
        if isinstance(token, str):
            if (" " in token) or ("\n" in token):
                return None
        escaped_tokens.append(escape_token(token))

    return escaped_tokens


def tokenize_argrepr_co(argrepr):
    if not argrepr.startswith("<code"):
        return None

    regex = r'<code object (.*) at (0x[a-f0-9]+), file "<dis>", line (\d+)>'
    match = re.fullmatch(regex, argrepr)
    if match is None:
        return None

    parts = match.group(1, 2, 3)
    return [
        SpecialToken.CO_START,
        parts[0],
        SpecialToken.CO_MEMORY,
        parts[1],
        SpecialToken.CO_LINE,
        parts[2],
        SpecialToken.CO_END,
    ]


def tokenize_python_string(s):
    s = s.replace("a", "aa")
    s = s.replace(" ", " ab ")
    s = s.replace("  ", " ")
    s = sacrebleu.tokenize_v14_international(s)

    # "ab" -> " ", "aa" -> "a", "\ x" -> "\x"
    psuedo_tokens = s.split(" ")
    tokens = []
    escaped = False
    for t in psuedo_tokens:
        if t == "":
            continue

        real_t = SpecialToken.STR_SPACE if t == "ab" else t.replace("aa", "a")
        if escaped:
            tokens.append("\\" + real_t)
            escaped = False
        elif real_t == "\\":
            escaped = True
        else:
            tokens.append(real_t)
            escaped = False

    return tokens


def tokenize_argrepr_python(argrepr):
    tokens = []
    try:
        iterator = tokenize.tokenize(io.BytesIO(argrepr.encode()).readline)
    except SyntaxError:
        return None
    while True:
        try:
            toktype, tok, _, _, _ = next(iterator)
        except (
            tokenize.TokenError,
            IndentationError,
            SyntaxError,
            UnicodeDecodeError,
            StopIteration,
        ):
            return None

        if toktype == tokenize.ENCODING or toktype == tokenize.NL:
            continue
        elif toktype in (
            tokenize.COMMENT,
            tokenize.INDENT,
            tokenize.DEDENT,
        ):
            return None
        elif toktype == tokenize.STRING:
            tokens += tokenize_python_string(tok)
        elif toktype == tokenize.NEWLINE:
            tokens.append(None)
        elif toktype == tokenize.ENDMARKER:
            tokens.append(None)
            break
        else:
            tokens.append(tok)

    assert tokens[-2] is None, "Error, should be newline"
    assert tokens[-1] is None, "Error, no end marker"
    result = tokens[:-2]
    if None in result:
        return None
    return result


def can_tokenize_argrepr_single(argrepr):
    if argrepr.isidentifier():
        return True

    if argrepr.isdigit():
        return True

    if argrepr in {"==", "!=", "<", ">", "<=", ">="}:
        return True

    return False


def tokenize_argrepr_single(argrepr):
    if argrepr == "":
        return []

    argrepr = argrepr.strip()
    if not can_tokenize_argrepr_single(argrepr):
        return None

    return [argrepr]


def tokenize_argrepr(argrepr):
    if not (argrepr.startswith("(") and argrepr.endswith(")")):
        return None

    wrap = lambda x: ["("] + x + [")"]

    item = argrepr[1:-1].strip()
    result = tokenize_argrepr_co(item)
    if result is not None:
        return wrap(result)

    result = tokenize_argrepr_single(item)
    if result is not None:
        return wrap(result)

    result = tokenize_argrepr_python(item)
    if result is not None:
        return wrap(result)

    return None


def tokenize_instruction(line):
    if (
        re.fullmatch(
            r" *(\d+ +)?(--> +)?(>> +)?(\d+ +)([A-Z_]+ *)( +\d+( +\(.*\))?)?", line
        )
        is None
    ):
        return None

    part = line.partition("(")
    argrepr = part[1] + part[2]
    line = part[0].strip()

    tokens = list(filter(None, line.split(" ")))

    if argrepr != "":
        tokenized_argrepr = tokenize_argrepr(argrepr)
        if tokenized_argrepr is None:
            return None
        tokens += tokenized_argrepr
    return tokens


def tokenize_func(line):
    if not line.startswith("D"):
        return None

    regex = (
        r'Disassembly of <code object (.*) at (0x[a-f0-9]+), file "<dis>", line (\d+)>:'
    )
    match = re.fullmatch(regex, line)
    if match is None:
        return None

    parts = match.group(1, 2, 3)
    return [
        SpecialToken.CO_DEF_START,
        SpecialToken.CO_START,
        parts[0],
        SpecialToken.CO_MEMORY,
        parts[1],
        SpecialToken.CO_LINE,
        parts[2],
        SpecialToken.CO_END,
        SpecialToken.CO_DEF_END,
    ]


def tokenize_line(line):
    if line == "\n":
        return [SpecialToken.NEW_LINE]
    if line == "":
        return []

    result = tokenize_func(line)
    if result is not None:
        return result

    result = tokenize_instruction(line)
    if result is not None:
        return result

    return None


import json


def tokenize_dis_json(
    line, input_field="bytecode", output_field="bytecode_tok", **kwargs
):
    json_obj = json.loads(line)
    result = tokenize_dis(json_obj[input_field])
    json_obj[output_field] = result
    return json.dumps(json_obj) + "\n"


def detokenize_dis_json(
    line, input_field="bytecode_tok", output_field="bytecode_detok", **kwargs
):
    json_obj = json.loads(line)
    result = detokenize_dis(json_obj[input_field])
    json_obj[output_field] = result
    return json.dumps(json_obj) + "\n"


def cmp_json(
    line, expected_field="bytecode_tok", actual_field="bytecode_retok", **kwargs
):
    json_obj = json.loads(line)
    expected = json_obj[expected_field]
    actual = json_obj[actual_field]

    if expected == actual:
        return None

    return line


def unescape_token(token):
    for sp in SpecialToken:
        if token == sp.value[0]:
            return sp.value[2]
        if token == sp.value[2]:
            return sp

    if token.startswith(ESCAPE[1]):
        return ESCAPE[0] + token[len(ESCAPE[1]) :]

    return token


def is_escape(l, start_index=0, escape_char="\\"):
    result = False
    for i in range(start_index, len(l)):
        if l[-(1 + i)] == escape_char:
            result = not result
        else:
            return result

    return result


def detokenize_dis(tokens):
    if tokens is None:
        return None

    assert isinstance(tokens, str) or isinstance(tokens, list)
    if isinstance(tokens, str):
        tokens = list(filter(None, tokens.split(" ")))

    tokens = [unescape_token(token) for token in tokens]
    is_argrepr = False
    is_string = None
    was_special = True
    result = []
    for token in tokens:
        if token == "":
            continue

        if isinstance(token, SpecialToken):
            if token == SpecialToken.NEW_LINE:
                is_argrepr = False

            result += token.value[1]
            was_special = True
            continue

        if not was_special and not is_string:
            result += " "
        result += token

        if not is_argrepr and token == "(":
            is_argrepr = True
            is_string = None

        if is_argrepr:
            for i, c in enumerate(token):
                if not is_string:
                    if c == "'" or c == '"' and not is_escape(result, len(token) - i):
                        is_string = c
                else:
                    if c == is_string and not is_escape(result, len(token) - i):
                        is_string = None

        was_special = False

    return "".join(result)


def extract_functions_dis(tokens):
    if tokens is None:
        return None
    assert isinstance(tokens, str) or isinstance(tokens, list)
    if isinstance(tokens, str):
        tokens = tokens.split(" ")

    functions_standalone = []
    functions_class = []
    function = None
    co_count = 0

    for token in tokens:
        if token == SpecialToken.CO_DEF_START.value[2]:
            if function is not None:
                if co_count > 1:
                    functions_class.append(" ".join(function))
                else:
                    functions_standalone.append(" ".join(function))

            co_count = 0
            function = []

        if token == SpecialToken.CO_START.value[2]:
            co_count += 1

        if function is not None:
            function.append(token)

    if function is not None:
        if co_count > 1:
            functions_class.append(" ".join(function))
        else:
            functions_standalone.append(" ".join(function))

    return functions_standalone, functions_class


def get_function_name_dis(tokens):
    if tokens is None:
        return None
    assert isinstance(tokens, str) or isinstance(tokens, list)
    if isinstance(tokens, str):
        tokens = tokens.split(" ")

    return tokens[tokens.index(SpecialToken.CO_DEF_START.value[2]) + 2]
