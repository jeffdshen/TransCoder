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
def f_gold ( x ) :
    if ( x == 0 or x == 1 ) :
        return x
    start = 1
    end = x
    while ( start <= end ) :
        mid = ( start + end ) // 2
        if ( mid * mid == x ) :
            return mid
        if ( mid * mid < x ) :
            start = mid + 1
            ans = mid
        else :
            end = mid - 1
    return ans


def f_filled ( x , start = 0 , end = None ) :
    if start == 0 :
        return x
    start = start
    end = start
    end = start
    end = end + 1
    start = end + 1
    end = end + 1
    end = end + 1


if __name__ == '__main__':
    param = [
    (40,),
    (10,),
    (46,),
    (54,),
    (1,),
    (67,),
    (64,),
    (10,),
    (75,),
    (11,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))