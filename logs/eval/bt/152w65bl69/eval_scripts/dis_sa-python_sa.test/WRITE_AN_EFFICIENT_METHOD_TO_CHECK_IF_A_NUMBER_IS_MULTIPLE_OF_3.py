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
    odd_count = 0
    even_count = 0
    if ( n < 0 ) :
        n = - n
    if ( n == 0 ) :
        return 1
    if ( n == 1 ) :
        return 0
    while ( n ) :
        if ( n & 1 ) :
            odd_count += 1
        if ( n & 2 ) :
            even_count += 1
        n = n >> 2
    return f_gold ( abs ( odd_count - even_count ) )


def f_filled ( n ) :
    """
 Returns the list of the offset of the offset of the offset of the offset in the offset
 of the offset of the offset of the offset in the offset
 of the offset of the offset of the offset of the offset
 of the offset of the offset of the offset in the offset
 offset.
 """
    n = 0
    while n < 0 :
        n -= 1
    return n


if __name__ == '__main__':
    param = [
    (94,),
    (94,),
    (79,),
    (39,),
    (16,),
    (90,),
    (64,),
    (76,),
    (83,),
    (47,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))