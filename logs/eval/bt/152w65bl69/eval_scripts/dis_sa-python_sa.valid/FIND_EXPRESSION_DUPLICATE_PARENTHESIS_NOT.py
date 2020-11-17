import numpy as np 
import math
from math import *
import collections
from collections import *
import heapq
import itertools
import random
import sys

# Copyright (c) 2019-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
def f_gold ( string ) :
    Stack = [ ]
    for ch in string :
        if ch == ')' :
            top = Stack.pop ( )
            elementsInside = 0
            while top != '(' :
                elementsInside += 1
                top = Stack.pop ( )
            if elementsInside < 1 :
                return True
        else :
            Stack.append ( ch )
    return False


def f_filled ( string ) :
    """
 Return the Stack of the Stack characters in the string of the string.

 Args:
 string (str): The Stack characters to the string.
 string: The string to be None.

 Returns:
 The Stack of the string to the string to the string.
 """
    for line in string :
        if line.startswith ( ' ' ) :
            return line.strip ( )
    return string


if __name__ == '__main__':
    param = [
    ("((a+b)+((c+d)))",),
    ("(((a+(b)))+(c+d))",),
    ("(((a+(b))+c+d))",),
    ("((a+b)+(c+d))",),
    ("(8582007)",),
    ("((a+(b))+(c+d))",),
    ("(PylsShEdKAE)",),
    ('886980680541',),
    ('001',),
    ('jsVmFeOq',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))