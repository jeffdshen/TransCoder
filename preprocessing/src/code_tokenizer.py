# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import argparse
import io
import os
import sys

import preprocessing.src.dis_tokenizer as dis_tokenizer
from preprocessing.src.javalang_tokenizer import (
    tokenize_java,
    detokenize_java,
    extract_functions_java,
    get_function_name_java,
    extract_arguments_java,
)
from preprocessing.src.cpp_tokenizer import (
    tokenize_cpp,
    detokenize_cpp,
    extract_functions_cpp,
    get_function_name_cpp,
    extract_arguments_cpp,
)
from preprocessing.src.python_tokenizer import (
    tokenize_python,
    detokenize_python,
    extract_functions_python,
    get_function_name_python,
)


def tokenize_dis(s, keep_comments=False):
    result = dis_tokenizer.tokenize_dis(s)
    if result is not None:
        return result
    return []


def detokenize_dis(s):
    result = dis_tokenizer.detokenize_dis(s)
    if result is not None:
        return result
    return ""


def extract_functions_dis(s):
    result = dis_tokenizer.extract_functions_dis(s)
    if result is not None:
        return result
    return [], []


def get_function_name_dis(s):
    return dis_tokenizer.get_function_name_dis(s)


if __name__ == "__main__":
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file", default="", help="The file to strip comments from."
    )
    parser.add_argument(
        "--l",
        default="python",
        choices=["python", "java", "cpp", "dis"],
        help="language of input code",
    )
    args = parser.parse_args()
    assert args.input_file == "" or os.path.isfile(args.input_file)

    # read from standard input, or from input file
    if args.input_file == "":
        source = sys.stdin.read()
    else:
        with io.open(args.input_file, encoding="utf-8") as f:
            source = f.read()

    tokenize = globals()[f"tokenize_{args.l}"]
    # tokenize
    print(tokenize(source), end="")
