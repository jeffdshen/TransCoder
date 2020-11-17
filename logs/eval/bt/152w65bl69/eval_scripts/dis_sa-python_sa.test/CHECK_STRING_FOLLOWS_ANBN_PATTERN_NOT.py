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
    n = len ( str )
    for i in range ( n ) :
        if ( str [ i ] != 'a' ) :
            break
    if ( i * 2 != n ) :
        return False
    for j in range ( i , n ) :
        if ( str [ j ] != 'b' ) :
            return False
    return True


def f_filled ( str ) :
    """
 Returns a list of numbers in a list of numbers

 Parameters
 -----
 str
 The list of numbers to be converted to the list of numbers
 str.
 str : str
 The list of numbers to be converted to the list of numbers
 numbers are returned as a list of numbers

 Returns
 -----
 str.The list of numbers are returned.

 Returns
 -----
 str.The list of numbers are returned.

 """
    return str ( str ( str ( str ) ) )


if __name__ == '__main__':
    param = [
    ('ba',),
    ('aabb',),
    ('abab',),
    ('aaabb',),
    ('aabbb',),
    ('abaabbaa',),
    ('abaababb',),
    ('bbaa',),
    ('11001000',),
    ('ZWXv te',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))