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
def f_gold ( n , k ) :
    res = ""
    for i in range ( k ) :
        res = res + chr ( ord ( 'a' ) + i )
    count = 0
    for i in range ( n - k ) :
        res = res + chr ( ord ( 'a' ) + count )
        count += 1
        if ( count == k ) :
            count = 0 ;
    return res


def f_filled ( n ) :
    """
 Returns the string of a string to a string in the string of numbers
 """
    for i in range ( n ) :
        if i < 0 :
            return n
    return n


if __name__ == '__main__':
    param = [
    (60,71,),
    (56,17,),
    (16,16,),
    (42,60,),
    (55,56,),
    (64,59,),
    (68,24,),
    (88,2,),
    (64,94,),
    (42,79,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))