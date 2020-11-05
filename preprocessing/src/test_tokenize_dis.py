# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

from preprocessing.src.code_tokenizer import tokenize_dis, detokenize_dis


TESTS = []
TESTS.append(
    (
        "  1           0 LOAD_NAME                0 (func)\n"
        "              2 LOAD_CONST               0 (20)\n"
        "              4 CALL_FUNCTION            1\n"
        "              6 POP_TOP\n"
        "\n"
        '  2           8 LOAD_CONST               1 (<code object func at 0x7f9712ea4930, file "<dis>", line 2>)\n'
        "             10 LOAD_CONST               2 ('func')\n"
        "             12 MAKE_FUNCTION            0\n"
        "             14 STORE_NAME               0 (func)\n"
        "             16 LOAD_CONST               3 (None)\n"
        "             18 RETURN_VALUE\n"
        "\n"
        'Disassembly of <code object func at 0x7f9712ea4930, file "<dis>", line 2>:\n'
        "  3           0 LOAD_FAST                0 (x)\n"
        "              2 LOAD_CONST               1 (10)\n"
        "              4 COMPARE_OP               4 (>)\n"
        "              6 POP_JUMP_IF_FALSE       12\n"
        "\n"
        "  4           8 LOAD_CONST               2 ('hello')\n"
        "             10 RETURN_VALUE\n"
        "\n"
        "  6     >>   12 LOAD_CONST               3 ('world')\n"
        "             14 RETURN_VALUE\n"
        "             16 LOAD_CONST               0 (None)\n"
        "             18 RETURN_VALUE\n",
        [
            "1",
            "0",
            "LOAD_NAME",
            "0",
            "(",
            "func",
            ")",
            "NEW_LINE",
            "2",
            "LOAD_CONST",
            "0",
            "(",
            "20",
            ")",
            "NEW_LINE",
            "4",
            "CALL_FUNCTION",
            "1",
            "NEW_LINE",
            "6",
            "POP_TOP",
            "NEW_LINE",
            "NEW_LINE",
            "2",
            "8",
            "LOAD_CONST",
            "1",
            "(",
            "CO_START",
            "func",
            "CO_MEMORY",
            "0x7f9712ea4930",
            "CO_LINE",
            "2",
            "CO_END",
            ")",
            "NEW_LINE",
            "10",
            "LOAD_CONST",
            "2",
            "(",
            "'",
            "func",
            "'",
            ")",
            "NEW_LINE",
            "12",
            "MAKE_FUNCTION",
            "0",
            "NEW_LINE",
            "14",
            "STORE_NAME",
            "0",
            "(",
            "func",
            ")",
            "NEW_LINE",
            "16",
            "LOAD_CONST",
            "3",
            "(",
            "None",
            ")",
            "NEW_LINE",
            "18",
            "RETURN_VALUE",
            "NEW_LINE",
            "NEW_LINE",
            "CO_DEF_START",
            "CO_START",
            "func",
            "CO_MEMORY",
            "0x7f9712ea4930",
            "CO_LINE",
            "2",
            "CO_END",
            "CO_DEF_END",
            "NEW_LINE",
            "3",
            "0",
            "LOAD_FAST",
            "0",
            "(",
            "x",
            ")",
            "NEW_LINE",
            "2",
            "LOAD_CONST",
            "1",
            "(",
            "10",
            ")",
            "NEW_LINE",
            "4",
            "COMPARE_OP",
            "4",
            "(",
            ">",
            ")",
            "NEW_LINE",
            "6",
            "POP_JUMP_IF_FALSE",
            "12",
            "NEW_LINE",
            "NEW_LINE",
            "4",
            "8",
            "LOAD_CONST",
            "2",
            "(",
            "'",
            "hello",
            "'",
            ")",
            "NEW_LINE",
            "10",
            "RETURN_VALUE",
            "NEW_LINE",
            "NEW_LINE",
            "6",
            ">>",
            "12",
            "LOAD_CONST",
            "3",
            "(",
            "'",
            "world",
            "'",
            ")",
            "NEW_LINE",
            "14",
            "RETURN_VALUE",
            "NEW_LINE",
            "16",
            "LOAD_CONST",
            "0",
            "(",
            "None",
            ")",
            "NEW_LINE",
            "18",
            "RETURN_VALUE",
            "NEW_LINE",
        ],
    ),
)

TESTS.append(
    (
        (
            "  1           0 LOAD_NAME                0 (func)\n"
            "              2 LOAD_CONST               0 ((0, 1, 5, 'a', 'b', 'd', 7, 9))\n"
            "              4 CALL_FUNCTION            1\n"
            "              6 POP_TOP\n"
            "\n"
            '  2           8 LOAD_CONST               1 (<code object func at 0x7f970fa2dae0, file "<dis>", line 2>)\n'
            "             10 LOAD_CONST               2 ('func')\n"
            "             12 MAKE_FUNCTION            0\n"
            "             14 STORE_NAME               0 (func)\n"
            "             16 LOAD_CONST               3 (None)\n"
            "             18 RETURN_VALUE\n"
            "\n"
            'Disassembly of <code object func at 0x7f970fa2dae0, file "<dis>", line 2>:\n'
            "  3           0 LOAD_GLOBAL              0 (len)\n"
            "              2 LOAD_FAST                0 (x)\n"
            "              4 CALL_FUNCTION            1\n"
            "              6 LOAD_CONST               1 (10)\n"
            "              8 COMPARE_OP               4 (>)\n"
            "             10 POP_JUMP_IF_FALSE       16\n"
            "\n"
            "  4          12 LOAD_CONST               2 ('hello')\n"
            "             14 RETURN_VALUE\n"
            "\n"
            "  6     >>   16 LOAD_CONST               3 ('world')\n"
            "             18 RETURN_VALUE\n"
            "             20 LOAD_CONST               0 (None)\n"
            "             22 RETURN_VALUE\n"
        ),
        [
            "1",
            "0",
            "LOAD_NAME",
            "0",
            "(",
            "func",
            ")",
            "NEW_LINE",
            "2",
            "LOAD_CONST",
            "0",
            "(",
            "(",
            "0",
            ",",
            "1",
            ",",
            "5",
            ",",
            "'",
            "a",
            "'",
            ",",
            "'",
            "b",
            "'",
            ",",
            "'",
            "d",
            "'",
            ",",
            "7",
            ",",
            "9",
            ")",
            ")",
            "NEW_LINE",
            "4",
            "CALL_FUNCTION",
            "1",
            "NEW_LINE",
            "6",
            "POP_TOP",
            "NEW_LINE",
            "NEW_LINE",
            "2",
            "8",
            "LOAD_CONST",
            "1",
            "(",
            "CO_START",
            "func",
            "CO_MEMORY",
            "0x7f970fa2dae0",
            "CO_LINE",
            "2",
            "CO_END",
            ")",
            "NEW_LINE",
            "10",
            "LOAD_CONST",
            "2",
            "(",
            "'",
            "func",
            "'",
            ")",
            "NEW_LINE",
            "12",
            "MAKE_FUNCTION",
            "0",
            "NEW_LINE",
            "14",
            "STORE_NAME",
            "0",
            "(",
            "func",
            ")",
            "NEW_LINE",
            "16",
            "LOAD_CONST",
            "3",
            "(",
            "None",
            ")",
            "NEW_LINE",
            "18",
            "RETURN_VALUE",
            "NEW_LINE",
            "NEW_LINE",
            "CO_DEF_START",
            "CO_START",
            "func",
            "CO_MEMORY",
            "0x7f970fa2dae0",
            "CO_LINE",
            "2",
            "CO_END",
            "CO_DEF_END",
            "NEW_LINE",
            "3",
            "0",
            "LOAD_GLOBAL",
            "0",
            "(",
            "len",
            ")",
            "NEW_LINE",
            "2",
            "LOAD_FAST",
            "0",
            "(",
            "x",
            ")",
            "NEW_LINE",
            "4",
            "CALL_FUNCTION",
            "1",
            "NEW_LINE",
            "6",
            "LOAD_CONST",
            "1",
            "(",
            "10",
            ")",
            "NEW_LINE",
            "8",
            "COMPARE_OP",
            "4",
            "(",
            ">",
            ")",
            "NEW_LINE",
            "10",
            "POP_JUMP_IF_FALSE",
            "16",
            "NEW_LINE",
            "NEW_LINE",
            "4",
            "12",
            "LOAD_CONST",
            "2",
            "(",
            "'",
            "hello",
            "'",
            ")",
            "NEW_LINE",
            "14",
            "RETURN_VALUE",
            "NEW_LINE",
            "NEW_LINE",
            "6",
            ">>",
            "16",
            "LOAD_CONST",
            "3",
            "(",
            "'",
            "world",
            "'",
            ")",
            "NEW_LINE",
            "18",
            "RETURN_VALUE",
            "NEW_LINE",
            "20",
            "LOAD_CONST",
            "0",
            "(",
            "None",
            ")",
            "NEW_LINE",
            "22",
            "RETURN_VALUE",
            "NEW_LINE",
        ],
    )
)

TESTS2 = []
TESTS2.append(
    (
        "  2           0 LOAD_CONST               0 (' module with one class and one function\n')\n"
        "              2 STORE_NAME               0 (__doc__)\n"
        "\n"
        "  3           4 LOAD_CONST               1 (0)\n"
        "              6 LOAD_CONST               2 (None)\n"
        "              8 IMPORT_NAME              1 (torch)\n"
        "             10 STORE_NAME               1 (torch)\n"
        "\n"
        "  4          12 LOAD_CONST               3 (2)\n"
        "             14 LOAD_CONST               4 (('jjj',))\n"
        "             16 IMPORT_NAME              2 (src.nnnn)\n"
        "             18 IMPORT_FROM              3 (jjj)\n"
        "             20 STORE_NAME               3 (jjj)\n"
        "             22 POP_TOP\n"
        "\n"
        "  5          24 LOAD_CONST               5 (1)\n"
        "             26 LOAD_CONST               6 (('a',))\n"
        "             28 IMPORT_NAME              4 (knpon.module)\n"
        "             30 IMPORT_FROM              5 (a)\n"
        "             32 STORE_NAME               5 (a)\n"
        "             34 POP_TOP\n"
        "\n"
        "  7          36 LOAD_BUILD_CLASS\n"
        '             38 LOAD_CONST               7 (<code object myclass at 0x7f9712eaa300, file "<dis>", line 7>)\n'
        "             40 LOAD_CONST               8 ('myclass')\n"
        "             42 MAKE_FUNCTION            0\n"
        "             44 LOAD_CONST               8 ('myclass')\n"
        "             46 CALL_FUNCTION            2\n"
        "             48 STORE_NAME               6 (myclass)\n"
        "             50 LOAD_CONST               2 (None)\n"
        "             52 RETURN_VALUE\n"
        "\n"
        'Disassembly of <code object myclass at 0x7f9712eaa300, file "<dis>", line 7>:\n'
        "  7           0 LOAD_NAME                0 (__name__)\n"
        "              2 STORE_NAME               1 (__module__)\n"
        "              4 LOAD_CONST               0 ('myclass')\n"
        "              6 STORE_NAME               2 (__qualname__)\n"
        "\n"
        ' 10           8 LOAD_CONST               1 (<code object geometric_suite at 0x7f9712eaa810, file "<dis>", line 10>)\n'
        "             10 LOAD_CONST               2 ('myclass.geometric_suite')\n"
        "             12 MAKE_FUNCTION            0\n"
        "             14 STORE_NAME               3 (geometric_suite)\n"
        "             16 LOAD_CONST               3 (None)\n"
        "             18 RETURN_VALUE\n"
        "\n"
        'Disassembly of <code object geometric_suite at 0x7f9712eaa810, file "<dis>", line 10>:\n'
        " 11           0 LOAD_CONST               1 (0)\n"
        "              2 STORE_FAST               0 (i)\n"
        "\n"
        " 12           4 LOAD_CONST               2 (1)\n"
        "              6 STORE_FAST               1 (j)\n"
        "\n"
        " 13           8 SETUP_LOOP              48 (to 58)\n"
        "             10 LOAD_GLOBAL              0 (range)\n"
        "             12 LOAD_CONST               3 (2)\n"
        "             14 CALL_FUNCTION            1\n"
        "             16 GET_ITER\n"
        "        >>   18 FOR_ITER                36 (to 56)\n"
        "             20 STORE_FAST               0 (i)\n"
        "\n"
        " 15          22 LOAD_FAST                0 (i)\n"
        "             24 LOAD_CONST               2 (1)\n"
        "             26 INPLACE_ADD\n"
        "             28 STORE_FAST               0 (i)\n"
        "\n"
        " 16          30 LOAD_FAST                1 (j)\n"
        "             32 LOAD_CONST               4 (3)\n"
        "             34 INPLACE_ADD\n"
        "             36 STORE_FAST               1 (j)\n"
        "\n"
        " 17          38 LOAD_GLOBAL              1 (module)\n"
        "             40 LOAD_METHOD              2 (function)\n"
        "             42 CALL_METHOD              0\n"
        "             44 STORE_FAST               2 (l)\n"
        "\n"
        " 18          46 LOAD_GLOBAL              3 (print)\n"
        "             48 LOAD_CONST               5 ('Hello Word\nI am boby !')\n"
        "             50 CALL_FUNCTION            1\n"
        "             52 POP_TOP\n"
        "             54 JUMP_ABSOLUTE           18\n"
        "        >>   56 POP_BLOCK\n"
        "\n"
        " 19     >>   58 LOAD_FAST                0 (i)\n"
        "             60 LOAD_FAST                1 (j)\n"
        "             62 BUILD_TUPLE              2\n"
        "             64 RETURN_VALUE\n"
    )
)


def test_dis_tokenizer():
    for i, (x, y) in enumerate(TESTS):
        y_ = tokenize_dis(x)
        if y_ != y:
            line_diff = [
                j for j, (line, line_) in enumerate(zip(y, y_)) if line != line_
            ]
            line_diff = line_diff[-1] if len(line_diff) > 0 else -1
            raise Exception(
                f"Difference at {line_diff}\nExpected:\n==========\n{y}\nbut found:\n==========\n{y_}"
            )


def test_dis_detokenizer():
    for i, x in enumerate([x[0] for x in TESTS] + TESTS2):
        tokens = tokenize_dis(x)
        x_ = detokenize_dis(tokens)
        tokens_ = tokenize_dis(x_)
        if tokens != tokens:
            line_diff = [
                j
                for j, (line, line_) in enumerate(zip(tokens, tokens_))
                if line != line_
            ]
            raise Exception(
                f"Difference at {line_diff}\n========== Original:\n{x}\n========== Tokenized {tokens} \n Detokenized:\n{x_} \n Retokenized {tokens_}"
            )
