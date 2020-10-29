import re

def flatten(lis):
  return [item for sublist in lis for item in sublist]

def interleave(*args):
  return [item for t in zip(*args) for item in t]

def split_and_keep(s, sep):
  t = s.split(sep)
  result = interleave(t, [sep] * len(t))
  if len(result) > 0:
    result.pop()
  return result

def tokenize_dis(bytecode):
  split_bytecode = split_and_keep(bytecode,"\n")
  lines = [tokenize_line(line) for line in split_bytecode]
  if all(x is None for x in lines):
    return None

  tokens = flatten(lines)
  tokens = ["NEW_LINE" if token == "\n" else token for token in tokens]
  return tokens

def tokenize_instruction(line):
  if re.fullmatch(r"( *\d*) (-->|   ) (>>|  ) ( *\d*) ([A-Z_]+ *)( *\d*( \(.*\))?)?", line) is None:
    return None

  part = line.partition("(")
  argrepr = part[1] + part[2]
  line = part[0].strip()

  tokens = list(filter(None, line.split(" ")))

  if argrepr is not None:
    tokens.append(argrepr)
  return tokens

def tokenize_func(line):
  if not line.startswith("Disassembly of "):
    return None

  part = line.partition(" of ")
  part = [part[0], part[1].strip(), part[2][:-1], part[2][-1:]]
  return part

def tokenize_line(line):
  if line == "\n":
    return [line]
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
def python_to_bytecode_line(
    line, **kwargs
):
    json_obj = json.loads(line)
    result = tokenize_dis(json_obj['bytecode'])
    if result is None:
      raise RuntimeError(line, json_obj['bytecode'])

    return ' '.join(result) + "\n"
