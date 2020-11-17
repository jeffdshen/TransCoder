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
def f_gold ( n ) :
    A = [ 0 ] * ( n + 1 )
    B = [ 0 ] * ( n + 1 )
    A [ 0 ] = 1
    A [ 1 ] = 0
    B [ 0 ] = 0
    B [ 1 ] = 1
    for i in range ( 2 , n + 1 ) :
        A [ i ] = A [ i - 2 ] + 2 * B [ i - 1 ]
        B [ i ] = A [ i - 1 ] + B [ i - 2 ]
    return A [ n ]


def f_filled ( n ) :
    """
 Return the list of the given n in the given n of the given n is a
 list of numbers in numbers and the given n is a
 list of numbers in numbers of numbers in numbers

 """
    # We do some numbers are not in numbers
    # numbers of numbers in numbers
    # numbers are not in numbers of numbers
    # numbers are not in numbers of numbers
    # numbers are not in numbers in numbers of numbers
    # numbers are not in numbers of numbers SPACETOKEN numbers SPACETOKEN are SPACETOKEN in SPACETOKEN numbers
    # numbers are not in numbers of numbers
    # numbers are not in numbers of numbers SPACETOKEN numbers
    # numbers are not in numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are in numbers numbers
    # numbers numbers are not in numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers
    # numbers are not in numbers
    # numbers numbers
    # numbers are not in numbers
    # numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers are not in numbers SPACETOKEN numbers
    # numbers SPACETOKEN are SPACETOKEN in SPACETOKEN numbers
    # numbers numbers are not in numbers
    # numbers are not in numbers
    # numbers SPACETOKEN are SPACETOKEN in SPACETOKEN numbers
    # numbers numbers SPACETOKEN are SPACETOKEN in SPACETOKEN numbers
    # numbers numbers


if __name__ == '__main__':
    param = [
    (29,),
    (13,),
    (25,),
    (65,),
    (27,),
    (42,),
    (19,),
    (50,),
    (59,),
    (13,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))