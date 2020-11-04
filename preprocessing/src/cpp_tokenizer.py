import random
import re

import clang
from clang.cindex import TokenKind

from preprocessing.src.timeout import timeout, TimeoutError
from preprocessing.src.tokenizer_utils import (
    process_string,
    ind_iter,
    indent_lines,
    get_first_token_before_first_parenthesis,
    extract_arguments_using_parentheses,
)

# pylint: disable=no-member


CPP_TOKEN2CHAR = {
    "STOKEN0": "//",
    "STOKEN1": "/*",
    "STOKEN2": "*/",
    "STOKEN3": "/**",
    "STOKEN4": "**/",
    "STOKEN5": '"""',
    "STOKEN6": "\\n",
}
CPP_CHAR2TOKEN = {
    "//": " STOKEN0 ",
    "/*": " STOKEN1 ",
    "*/": " STOKEN2 ",
    "/**": " STOKEN3 ",
    "**/": " STOKEN4 ",
    '"""': " STOKEN5 ",
    "\\n": " STOKEN6 ",
}

TOK_NO_SPACE_BEFORE = {",", ";"}
clang.cindex.Config.set_library_file("/usr/lib/llvm-7/lib/libclang.so")
STRINGS_AND_COMMENTS_TOKEN_KINDS = {TokenKind.LITERAL, TokenKind.COMMENT}

try:
    idx = clang.cindex.Index.create()
except:
    idx = None


@timeout(10)
def get_cpp_tokens_and_types(s):
    tokens = []
    assert isinstance(s, str)
    s = s.replace(r"\r", "")
    hash = str(random.getrandbits(128))
    parsed_code = idx.parse(
        hash + "_tmp.cpp",
        args=["-std=c++11"],
        unsaved_files=[(hash + "_tmp.cpp", s)],
        options=0,
    )
    for tok in parsed_code.get_tokens(extent=parsed_code.cursor.extent):
        tokens.append((tok.spelling, tok.kind))
    return tokens


def tokenize_cpp(s, keep_comments=False):
    tokens = []
    assert isinstance(s, str)
    try:
        tokens_and_types = get_cpp_tokens_and_types(s)
        for tok, typ in tokens_and_types:
            if not keep_comments and typ == TokenKind.COMMENT:
                continue
            if typ in STRINGS_AND_COMMENTS_TOKEN_KINDS:
                if typ == TokenKind.COMMENT:
                    com = process_string(tok, CPP_CHAR2TOKEN, CPP_TOKEN2CHAR, True)
                    if len(com) > 0:
                        tokens.append(com)
                else:
                    tokens.append(
                        process_string(tok, CPP_CHAR2TOKEN, CPP_TOKEN2CHAR, False)
                    )
            else:
                tokens.append(tok)
        return tokens
    except KeyboardInterrupt:
        raise
    except TimeoutError:
        return []
    except:
        return []


def detokenize_cpp(s):
    assert isinstance(s, str) or isinstance(s, list)
    if isinstance(s, list):
        s = " ".join(s)
    # the ▁ character created bugs in the cpp tokenizer
    s = s.replace("ENDCOM", "\n").replace("▁", " SPACETOKEN ")
    try:
        tokens_and_types = get_cpp_tokens_and_types(s)
    except:
        return ""
    new_tokens = []
    i = 0
    while i < len(tokens_and_types):
        token, type = tokens_and_types[i]
        if type in STRINGS_AND_COMMENTS_TOKEN_KINDS:
            new_tokens.append(
                token.replace("STRNEWLINE", "\n")
                .replace("TABSYMBOL", "\t")
                .replace(" ", "")
                .replace("SPACETOKEN", " ")
            )
            if type == TokenKind.COMMENT:
                new_tokens.append("NEW_LINE")
        elif token == "}":
            if i < len(tokens_and_types) - 1 and tokens_and_types[i + 1][0] == ";":
                new_tokens += ["CB_COLON", "NEW_LINE"]
                i += 2
                continue
            if i < len(tokens_and_types) - 1 and tokens_and_types[i + 1][0] == ",":
                new_tokens += ["CB_COMA", "NEW_LINE"]
                i += 2
                continue
            new_tokens += ["CB_", "NEW_LINE"]
        elif token == "{":
            new_tokens += ["OB_", "NEW_LINE"]
        elif token == "*/":
            new_tokens += ["*/", "NEW_LINE"]
        elif token == ";":
            new_tokens += [";", "NEW_LINE"]
        else:
            new_tokens.append(token)

        if (
            i < len(tokens_and_types) - 1
            and tokens_and_types[i + 1][0] in TOK_NO_SPACE_BEFORE
        ):
            next_token = tokens_and_types[i + 1][0]
            new_tokens[len(new_tokens) - 1] += next_token
            if next_token == ";":
                new_tokens.append("NEW_LINE")
            i += 2
            continue
        i += 1

    lines = re.split("NEW_LINE", " ".join(new_tokens))

    untok_s = indent_lines(lines)
    untok_s = (
        untok_s.replace("CB_COLON", "};")
        .replace("CB_COMA", "},")
        .replace("CB_", "}")
        .replace("OB_", "{")
    )
    return untok_s


def clean_hashtags_functions_cpp(function):
    function = re.sub('[#][ ][i][n][c][l][u][d][e][ ]["].*?["]', "", function)
    function = re.sub("[#][ ][i][n][c][l][u][d][e][ ][<].*?[>]", "", function)
    function = re.sub("[#][ ][i][f][n][d][e][f][ ][^ ]*", "", function)
    function = re.sub("[#][ ][i][f][d][e][f][ ][^ ]*", "", function)
    function = re.sub(
        "[#][ ][d][e][f][i][n][e][ ][^ ]*[ ][(][ ].*?[ ][)][ ][(][ ].*[ ][)]",
        "",
        function,
    )
    function = re.sub(
        "[#][ ][d][e][f][i][n][e][ ][^ ]*[ ][(][ ].*?[ ][)][ ][{][ ].*[ ][}]",
        "",
        function,
    )
    function = re.sub(
        '[#][ ][d][e][f][i][n][e][ ][^ ]*[ ]([(][ ])?["].*?["]([ ][)])?', "", function
    )
    function = re.sub(
        "[#][ ][d][e][f][i][n][e][ ][^ ]*[ ]([(][ ])?\d*\.?\d*([ ][+-/*][ ]?\d*\.?\d*)?([ ][)])?",
        "",
        function,
    )
    function = re.sub("[#][ ][d][e][f][i][n][e][ ][^ ]", "", function)
    function = re.sub(
        "[#][ ][i][f][ ][d][e][f][i][n][e][d][ ][(][ ].*?[ ][)]", "", function
    )
    function = re.sub("[#][ ][i][f][ ][^ ]*", "", function)
    function = function.replace("# else", "")
    function = function.replace("# endif", "")
    function = function.strip()
    return function


def extract_functions_cpp(s):
    try:
        s = clean_hashtags_functions_cpp(s)
        s = s.replace("ENDCOM", "\n").replace("▁", "SPACETOKEN")
        tokens = get_cpp_tokens_and_types(s)
    except:
        return [], []
    i = ind_iter(len(tokens))
    functions_standalone = []
    functions_class = []
    try:
        token, token_type = tokens[i.i]
    except:
        return [], []
    while True:
        try:
            # detect function
            if token == ")" and (
                (tokens[i.i + 1][0] == "{" and tokens[i.i + 2][0] != "}")
                or (
                    tokens[i.i + 1][0] == "throw"
                    and tokens[i.i + 4][0] == "{"
                    and tokens[i.i + 5][0] == "}"
                )
            ):
                # go previous until the start of function
                while token not in {";", "}", "{"}:
                    try:
                        i.prev()
                    except StopIteration:
                        break
                    token = tokens[i.i][0]

                i.next()
                token, token_type = tokens[i.i]
                if token_type == TokenKind.COMMENT:
                    token = token.strip()
                    token += " ENDCOM"
                function = [token]
                token_types = [token_type]
                while token != "{":
                    i.next()
                    token, token_type = tokens[i.i]
                    if token_type == TokenKind.COMMENT:
                        token = token.strip()
                        token += " ENDCOM"
                    function.append(token)
                    token_types.append(token_type)

                if token_types[function.index("(") - 1] != TokenKind.IDENTIFIER:
                    continue
                if token == "{":
                    number_indent = 1
                    while not (token == "}" and number_indent == 0):
                        try:
                            i.next()
                            token, token_type = tokens[i.i]
                            if token == "{":
                                number_indent += 1
                            elif token == "}":
                                number_indent -= 1
                            if token_type == TokenKind.COMMENT:
                                token = token.strip()
                                token += " ENDCOM"
                            function.append(token)
                        except StopIteration:
                            break
                    if (
                        "static" in function[0 : function.index("{")]
                        or "::" not in function[0 : function.index("(")]
                    ):
                        function = " ".join(function)
                        function = clean_hashtags_functions_cpp(function)
                        function = function.strip()
                        function = function.replace("\n", "ENDCOM").replace(
                            "SPACETOKEN", "▁"
                        )
                        if (
                            not re.sub(
                                "[^ ]*[ ][(][ ]\w*([ ][,][ ]\w*)*[ ][)]",
                                "",
                                function[: function.index("{")],
                            )
                            .strip()
                            .startswith("{")
                            and not function.startswith("#")
                        ):
                            functions_standalone.append(function)
                    else:
                        function = " ".join(function)
                        function = clean_hashtags_functions_cpp(function)
                        function = function.strip()
                        function = function.replace("\n", "ENDCOM").replace(
                            "SPACETOKEN", "▁"
                        )
                        if (
                            not re.sub(
                                "[^ ]*[ ][(][ ]\w*([ ][,][ ]\w*)*[ ][)]",
                                "",
                                function[: function.index("{")],
                            )
                            .strip()
                            .startswith("{")
                            and not function.startswith("#")
                        ):
                            functions_class.append(function)
            i.next()
            token = tokens[i.i][0]
        except:
            break
    return functions_standalone, functions_class


def get_function_name_cpp(s):
    return get_first_token_before_first_parenthesis(s)


def extract_arguments_cpp(f):
    return extract_arguments_using_parentheses(f)
