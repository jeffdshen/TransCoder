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
def f_gold ( str ) :
    stack = [ ]
    for i in range ( len ( str ) ) :
        stack.append ( str [ i ] )
    for i in range ( len ( str ) ) :
        str [ i ] = stack.pop ( )


def f_filled Reverse ( str ) :
    stack = [ ]
    for i in range ( len ( stack ) ) :
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )
        stack.append ( i )


if __name__ == '__main__':
    param = [
    ([' ', 'G', 'I', 'N', 'O', 'S', 'S', 'c', 'e', 'j', 'l', 'm', 'p'],),
    (['6', '4', '7', '9', '9', '3', '1', '2', '7', '6', '1', '5', '8', '3', '8', '1', '1', '8', '6', '6', '0', '5', '6', '5', '5', '1'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['j', 'o', 'P', 'V', 'R', 'r', 'w', 'G', 'p', 'L', 'I', 'H', 'B', 'b', 'D', 'm', 'O', 'p', 'e', 'B', ' ', 'M', 'S', 't', 'x', 'A', 'D', 'S', 'A', 'z', 'g'],),
    (['0', '0', '0', '0', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '6', '6', '6', '6', '7', '8', '8', '8', '9', '9', '9', '9'],),
    (['1', '1'],),
    (['E', 'E', 'J', 'K', 'L', 'Q', 'R', 'S', 'T', 'U', 'U', 'V', 'W', 'W', 'X', 'Z', 'a', 'b', 'c', 'c', 'e', 'e', 'f', 'h', 'j', 'j', 'l', 'm', 'o', 'p', 'p', 'p', 'u', 'u', 'u', 'z', 'z', 'z'],),
    (['5', '9', '9', '5', '8', '7', '7', '0', '4', '6', '5', '4', '7', '2', '5', '4', '7', '3', '7', '9', '1', '8', '8', '9', '9', '5', '3'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['x', 'm', 'z', 'C', 'Y', 'W', 'Q', 'B', 'B', 'h', 'w', 'C', 'e', 'P', 'g', 'P', 'J', 'O', 'A', 'T', 'b', 'y', 'i', ' ', 'A', 'a', 'w'],)
        ]
    filled_function_param = [
    ([' ', 'G', 'I', 'N', 'O', 'S', 'S', 'c', 'e', 'j', 'l', 'm', 'p'],),
    (['6', '4', '7', '9', '9', '3', '1', '2', '7', '6', '1', '5', '8', '3', '8', '1', '1', '8', '6', '6', '0', '5', '6', '5', '5', '1'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['j', 'o', 'P', 'V', 'R', 'r', 'w', 'G', 'p', 'L', 'I', 'H', 'B', 'b', 'D', 'm', 'O', 'p', 'e', 'B', ' ', 'M', 'S', 't', 'x', 'A', 'D', 'S', 'A', 'z', 'g'],),
    (['0', '0', '0', '0', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '4', '5', '5', '5', '5', '5', '6', '6', '6', '6', '7', '8', '8', '8', '9', '9', '9', '9'],),
    (['1', '1'],),
    (['E', 'E', 'J', 'K', 'L', 'Q', 'R', 'S', 'T', 'U', 'U', 'V', 'W', 'W', 'X', 'Z', 'a', 'b', 'c', 'c', 'e', 'e', 'f', 'h', 'j', 'j', 'l', 'm', 'o', 'p', 'p', 'p', 'u', 'u', 'u', 'z', 'z', 'z'],),
    (['5', '9', '9', '5', '8', '7', '7', '0', '4', '6', '5', '4', '7', '2', '5', '4', '7', '3', '7', '9', '1', '8', '8', '9', '9', '5', '3'],),
    (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1'],),
    (['x', 'm', 'z', 'C', 'Y', 'W', 'Q', 'B', 'B', 'h', 'w', 'C', 'e', 'P', 'g', 'P', 'J', 'O', 'A', 'T', 'b', 'y', 'i', ' ', 'A', 'a', 'w'],)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
