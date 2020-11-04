import re

from sacrebleu import tokenize_v14_international


def process_string(tok, char2tok, tok2char, is_comment):
    if is_comment:
        tok = re.sub(" +", " ", tok)
        tok = re.sub(r"(.)\1\1\1\1+", r"\1\1\1\1\1", tok)
        if len(re.sub(r"\W", "", tok)) < 2:
            return ""
    tok = tok.replace(" ", " ▁ ")
    for char, special_token in char2tok.items():
        tok = tok.replace(char, special_token)
    if tok.startswith(" STOKEN0"):
        if tok.endswith("\n"):
            tok = tok[:-1]
        tok += " ENDCOM"
    tok = tok.replace("\n", " STRNEWLINE ")
    tok = tok.replace("\t", " TABSYMBOL ")
    tok = re.sub(" +", " ", tok)
    tok = tokenize_v14_international(tok)
    tok = re.sub(" +", " ", tok)
    for special_token, char in tok2char.items():
        tok = tok.replace(special_token, char)
    tok = tok.replace("\r", "")

    return tok


def indent_lines(lines):
    prefix = ""
    for i, line in enumerate(lines):
        line = line.strip()
        if re.match("CB_COLON|CB_COMA|CB_", line):
            prefix = prefix[2:]
            line = prefix + line
        elif line.endswith("OB_"):
            line = prefix + line
            prefix += "  "
        else:
            line = prefix + line
        lines[i] = line
    untok_s = "\n".join(lines)
    return untok_s


class ind_iter(object):
    def __init__(self, len):
        self.i = 0
        self.len = len

    def next(self):
        self.i += 1
        if self.i > (self.len - 1):
            raise StopIteration

    def prev(self):
        self.i -= 1
        if self.i < 0:
            raise StopIteration


def get_first_token_before_first_parenthesis(s):
    assert isinstance(s, str) or isinstance(s, list)
    if isinstance(s, str):
        s = s.split()
    return s[s.index("(") - 1]


def extract_arguments_using_parentheses(f):
    f = f.split(" ")
    types = []
    names = []
    par = 0
    arguments = []
    f = f[f.index("(") :]
    for tok in f:
        if tok == "(":
            par += 1
        elif tok == ")":
            par -= 1
        arguments.append(tok)
        if par == 0:
            break
    arguments = " ".join(arguments[1:-1])
    if arguments == "":
        return ["None"], ["None"]
    arguments = arguments.split(",")
    for arg in arguments:
        bracks = re.findall("\[ \]", arg)
        bracks = " ".join(bracks)
        arg = arg.replace(bracks, "")
        arg = arg.strip()
        arg = re.sub(" +", " ", arg)
        t = " ".join(arg.split(" ")[:-1] + [bracks])
        n = arg.split(" ")[-1]
        types.append(t)
        names.append(n)
    return types, names
