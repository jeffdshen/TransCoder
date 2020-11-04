import tokenize

import re
from io import BytesIO
from preprocessing.src.tokenizer_utils import process_string

PYTHON_TOKEN2CHAR = {
    "STOKEN0": "#",
    "STOKEN1": "\\n",
    "STOKEN2": '"""',
    "STOKEN3": "'''",
}

PYTHON_CHAR2TOKEN = {
    "#": " STOKEN0 ",
    "\\n": " STOKEN1 ",
    '"""': " STOKEN2 ",
    "'''": " STOKEN3 ",
}


def tokenize_python(s, keep_comments=False):
    try:
        assert isinstance(s, str)
        s = s.replace(r"\r", "")
        tokens = []

        try:
            iterator = tokenize.tokenize(BytesIO(s.encode("utf-8")).readline)
        except SyntaxError as excep:
            raise SyntaxError(excep)

        removed_docstr = 0
        while True:
            try:
                toktype, tok, _, _, line = next(iterator)
            except (
                tokenize.TokenError,
                IndentationError,
                SyntaxError,
                UnicodeDecodeError,
            ):
                raise Exception(
                    f'Impossible to parse tokens because icorrect source code "{s[0:30]}" ...'
                )
            except StopIteration:
                raise Exception(f"End of iterator before ENDMARKER token.")

            if toktype == tokenize.ENCODING or toktype == tokenize.NL:
                continue

            elif toktype == tokenize.NEWLINE:
                if removed_docstr == 1:
                    removed_docstr = 0
                    continue
                tokens.append("NEW_LINE")

            elif toktype == tokenize.COMMENT:
                if keep_comments:
                    com = process_string(
                        tok, PYTHON_CHAR2TOKEN, PYTHON_TOKEN2CHAR, True
                    )
                    if len(com) > 0:
                        tokens.append(com)
                else:
                    continue

            elif toktype == tokenize.STRING:
                if tok == line.strip():  # docstring
                    if not keep_comments:
                        removed_docstr = 1
                        continue
                    else:
                        coms = process_string(
                            tok, PYTHON_CHAR2TOKEN, PYTHON_TOKEN2CHAR, True
                        )
                        if len(coms) > 0:
                            tokens.append(coms)
                        else:
                            removed_docstr = 1
                else:
                    tokens.append(
                        process_string(tok, PYTHON_CHAR2TOKEN, PYTHON_TOKEN2CHAR, False)
                    )

            elif toktype == tokenize.INDENT:
                tokens.append("INDENT")

            elif toktype == tokenize.DEDENT:
                # empty block
                if tokens[-1] == "INDENT":
                    tokens = tokens[:-1]
                else:
                    tokens.append("DEDENT")

            elif toktype == tokenize.ENDMARKER:
                tokens.append("ENDMARKER")
                break

            else:
                tokens.append(tok)

        assert tokens[-1] == "ENDMARKER", "Error, no end marker"
        return tokens[:-1]
    except KeyboardInterrupt:
        raise
    except:
        return []


def detokenize_python(s):
    try:
        assert isinstance(s, str) or isinstance(s, list)
        if isinstance(s, list):
            s = " ".join(s)
        s = s.replace("ENDCOM", "NEW_LINE")
        s = s.replace("▁", "SPACETOKEN")

        lines = s.split("NEW_LINE")
        tabs = ""
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith("INDENT "):
                tabs += "    "
                line = line.replace("INDENT ", tabs)
            elif line.startswith("DEDENT"):
                number_dedent = line.count("DEDENT")
                tabs = tabs[4 * number_dedent :]
                line = line.replace("DEDENT", "")
                line = line.strip()
                line = tabs + line
            elif line == "DEDENT":
                line = ""
            else:
                line = tabs + line
            lines[i] = line
        untok_s = "\n".join(lines)

        # find string and comment with parser and detokenize string correctly
        try:
            for toktype, tok, _, _, line in tokenize.tokenize(
                BytesIO(untok_s.encode("utf-8")).readline
            ):
                if toktype == tokenize.STRING or toktype == tokenize.COMMENT:
                    tok_ = (
                        tok.replace("STRNEWLINE", "\n")
                        .replace("TABSYMBOL", "\t")
                        .replace(" ", "")
                        .replace("SPACETOKEN", " ")
                    )
                    untok_s = untok_s.replace(tok, tok_)
        except KeyboardInterrupt:
            raise
        except:
            pass

        # detokenize imports
        untok_s = (
            untok_s.replace(". ", ".")
            .replace(" .", ".")
            .replace("import.", "import .")
            .replace("from.", "from .")
        )
        untok_s = untok_s.replace("> >", ">>").replace("< <", "<<")
        return untok_s
    except KeyboardInterrupt:
        raise
    except:
        return ""


def extract_functions_python(s):
    tokens = iter(s.split())
    functions_standalone = []
    functions_class = []
    number_indent = 0
    try:
        token = next(tokens)
    except StopIteration:
        return [], []
    while True:
        try:
            if token == "def":
                function = ["def"]
                while not (token == "DEDENT" and number_indent == 0):
                    token = next(tokens)
                    if token == "INDENT":
                        number_indent += 1
                    elif token == "DEDENT":
                        number_indent -= 1
                    function.append(token)
                try:
                    if function[function.index("(") + 1] == "self":
                        function = " ".join(function)
                        if function is not None:
                            functions_class.append(function)
                    else:
                        function = " ".join(function)
                        if function is not None:
                            functions_standalone.append(function)
                except:
                    print(function)
                    token = next(tokens)
            else:
                token = next(tokens)
        except StopIteration:
            break
    return functions_standalone, functions_class


def get_function_name_python(s):
    assert isinstance(s, str) or isinstance(s, list)
    if isinstance(s, str):
        s = s.split()
    return s[s.index("def") + 1]
