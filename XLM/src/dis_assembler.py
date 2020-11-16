import types
import sys
from collections import namedtuple
import dis
import re
import ast


class MutableCodeObject:
    def __init__(
        self,
        co_argcount,
        co_kwonlyargcount,
        co_nlocals,
        co_stacksize,
        co_flags,
        co_code,
        co_consts,
        co_names,
        co_varnames,
        co_filename,
        co_name,
        co_firstlineno,
        co_lnotab,
        co_freevars,
        co_cellvars,
    ):
        self.co_argcount = co_argcount
        self.co_kwonlyargcount = co_kwonlyargcount
        self.co_nlocals = co_nlocals
        self.co_stacksize = co_stacksize
        self.co_flags = co_flags
        self.co_code = co_code
        self.co_consts = co_consts
        self.co_names = co_names
        self.co_varnames = co_varnames
        self.co_filename = co_filename
        self.co_name = co_name
        self.co_firstlineno = co_firstlineno
        self.co_lnotab = co_lnotab
        self.co_freevars = co_freevars
        self.co_cellvars = co_cellvars

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"co_argcount={self.co_argcount!r}, "
            f"co_kwonlyargcount={self.co_kwonlyargcount!r}, "
            f"co_nlocals={self.co_nlocals!r}, "
            f"co_stacksize={self.co_stacksize!r}, "
            f"co_flags={self.co_flags!r}, "
            f"co_code={self.co_code!r}, "
            f"co_consts={self.co_consts!r}, "
            f"co_names={self.co_names!r}, "
            f"co_varnames={self.co_varnames!r}, "
            f"co_filename={self.co_filename!r}, "
            f"co_name={self.co_name!r}, "
            f"co_firstlineno={self.co_firstlineno!r}, "
            f"co_lnotab={self.co_lnotab!r}, "
            f"co_freevars={self.co_freevars!r}, "
            f"co_cellvars={self.co_cellvars!r})"
        )

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        raise TypeError

    def to_co(self, hexversion=50792944):
        assert sys.hexversion == hexversion, "Hex version does not match"

        co_consts = []
        for c in self.co_consts:
            if isinstance(c, MutableCodeObject):
                co_consts.append(c.to_co(hexversion))
            else:
                co_consts.append(c)

        return types.CodeType(
            self.co_argcount,
            self.co_kwonlyargcount,
            self.co_nlocals,
            self.co_stacksize,
            self.co_flags,
            self.co_code,
            tuple(co_consts),
            self.co_names,
            self.co_varnames,
            self.co_filename,
            self.co_name,
            self.co_firstlineno,
            self.co_lnotab,
            self.co_freevars,
            self.co_cellvars,
        )


def co_to_mutable_co(co, hexversion=50792944):
    """
    hex_version=50792944 is Python 3.7.9, aka
    sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
    """
    assert sys.hexversion == hexversion, "Hex version does not match"

    co_consts = []
    for c in co.co_consts:
        if isinstance(c, types.CodeType):
            co_consts.append(co_to_mutable_co(c))
        else:
            co_consts.append(c)

    return MutableCodeObject(
        co_argcount=co.co_argcount,
        co_kwonlyargcount=co.co_kwonlyargcount,
        co_nlocals=co.co_nlocals,
        co_stacksize=co.co_stacksize,
        co_flags=co.co_flags,
        co_code=co.co_code,
        co_consts=co_consts,
        co_names=co.co_names,
        co_varnames=co.co_varnames,
        co_filename=co.co_filename,
        co_name=co.co_name,
        co_firstlineno=co.co_firstlineno,
        co_lnotab=co.co_lnotab,
        co_freevars=co.co_freevars,
        co_cellvars=co.co_cellvars,
    )


def get_instruction(line):
    if (
        re.fullmatch(
            r" *(\d+ +)?(--> +)?(>> +)?(\d+ +)([A-Z_]+ *)( +\d+( +\(.*\))?)?", line
        )
        is None
    ):
        return None

    part = line.partition("(")
    argrepr = part[1] + part[2]
    argrepr = argrepr.strip()
    if argrepr.startswith("(") and argrepr.endswith(")"):
        argrepr = argrepr[1:-1].strip()
    else:
        argrepr = None

    tokens = list(filter(None, part[0].strip().split(" ")))
    if len(tokens) >= 1 and tokens[-1].isdigit():
        arg = int(tokens[-1])
        tokens = tokens[:-1]
    else:
        arg = 0

    if len(tokens) >= 1:
        op = tokens[-1]
        tokens = tokens[:-1]
    else:
        op = None

    if len(tokens) >= 1 and tokens[-1].isdigit():
        offset = int(tokens[-1])
        tokens = tokens[:-1]
    else:
        offset = None

    if len(tokens) >= 1 and tokens[0].isdigit():
        line_no = int(tokens[0])
    else:
        line_no = None

    return line_no, offset, op, arg, argrepr


def parse(bytecode, hexversion=50792944):
    """
    hex_version=50792944 is Python 3.7.9, aka
    sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
    """
    lines = list(filter(None, bytecode.split("\n")))
    code = bytearray()
    varnames = {}
    names = {}
    constants = {}

    # don't handle line numbers
    co_lnotab = b"\x00\x01"

    for line in lines:
        if line.startswith("Disassembly of "):
            continue

        line_tuple = get_instruction(line)
        if line_tuple is None:
            return None

        line_no, offset, op, arg, argrepr = line_tuple

        if op not in dis.opmap:
            return None

        opname = op
        op = dis.opmap[op]

        if op in dis.hasconst:
            constants[arg] = ast.literal_eval(argrepr)
        elif op in dis.hasname:
            names[arg] = argrepr
        elif op in dis.hasjrel:
            if (
                argrepr.startswith("to")
                and argrepr[2:].strip().isdigit()
                and offset is not None
            ):
                arg = int(argrepr[2:].strip().isdigit()) - offset - 2
        elif op in dis.haslocal:
            varnames[arg] = argrepr
        elif op in dis.hascompare:
            pass
        elif op in dis.hasfree:
            # can't handle closures or globals
            return None
        elif op == dis.FORMAT_VALUE:
            pass

        code.append(op)
        code.append(arg)

    co_code = bytes(code)

    co_nlocals = max(varnames, default=-1) + 1
    co_varnames = []

    varnames_values = set(varnames.values())
    for i in range(0, co_nlocals * 2):
        if len(co_varnames) == co_nlocals:
            break
        unused = "unused_varname_" + str(i)
        if unused in varnames_values:
            continue
        co_varnames.append(unused)

    for i, n in varnames.items():
        co_varnames[i] = n

    co_nnames = max(names, default=-1) + 1
    co_names = []
    names_values = set(names.values())
    for i in range(0, co_nnames * 2):
        if len(co_names) == co_nnames:
            break
        unused = "unused_name_" + str(i)
        if unused in names_values:
            continue
        co_names.append(unused)

    for i, n in names.items():
        co_names[i] = n

    co_constants = [None] * (max(constants, default=-1) + 1)
    for i, n in constants.items():
        co_constants[i] = n

    return (
        co_code,
        co_nlocals,
        tuple(co_varnames),
        tuple(co_names),
        tuple(co_constants),
        co_lnotab,
    )
