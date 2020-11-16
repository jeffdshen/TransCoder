import src.dis_assembler as dis_asm
import argparse
import json
import os

# test file imports
import numpy as np
import math
from math import *
import collections
from collections import *
import heapq
import itertools
import random
import sys


def run_dis_script():
    """
    run a dis script
    """
    # parse parameters
    parser = argparse.ArgumentParser(description="Take dis script and run it")

    # model
    parser.add_argument("--script_path", type=str,
                        default="", help="Script path")

    params = parser.parse_args()
    with open(params.script_path) as f:
        lines = f.readlines()

    info = json.loads(lines[0])
    script = info["script"]
    ref = info["ref"]
    bytecode = ''.join(lines[1:])

    co = compile(ref, "<dis>", "exec")
    mco = dis_asm.co_to_mutable_co(co)
    fco = None
    for const in mco.co_consts:
        if isinstance(const, dis_asm.MutableCodeObject):
            fco = const
            break
    
    script = script.replace("#TOFILL", "f_filled = " + fco.co_name)
    co_code, co_nlocals, co_varnames, co_names, co_consts, co_linestarts = dis_asm.parse(bytecode)
    fco.co_code = co_code
    fco.co_nlocals = co_nlocals
    fco.co_varnames = co_varnames
    fco.co_names = co_names
    fco.co_constants = co_consts
    fco.co_lnotab = co_linestarts
    hyp_co = mco.to_co()
    return hyp_co, compile(script, "main.py", "exec")


if __name__ == '__main__':
    for item in run_dis_script():
        exec(item)