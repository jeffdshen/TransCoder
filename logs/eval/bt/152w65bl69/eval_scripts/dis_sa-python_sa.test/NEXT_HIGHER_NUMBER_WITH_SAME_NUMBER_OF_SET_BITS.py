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
    next = 0
    if ( x ) :
        rightOne = x & - ( x )
        nextHigherOneBit = x + int ( rightOne )
        rightOnesPattern = x ^ int ( nextHigherOneBit )
        rightOnesPattern = ( int ( rightOnesPattern ) / int ( rightOne ) )
        rightOnesPattern = int ( rightOnesPattern ) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next


def f_filled ( x , next , depth , depth , depth , depth , depth , depth ) :
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 0 ]
    depth = depth [ 1 ]
    depth = depth [ 2 ]
    depth = depth [ 3 ]
    depth = depth [ 4 ]
    depth = depth [ 5 ]
    depth = depth [ 6 ]
    depth = depth [ 7 ]
    depth = depth [ 8 ]
    depth = depth [ 9 ]
    depth = depth [ 10 ]
    depth = depth [ 11 ]
    depth = depth [ 12 ]
    depth = depth [ 13 ]
    depth = depth [ 14 ]
    depth = depth [ 15 ]
    depth = depth [ 16 ]
    depth = depth [ 18 ]
    depth = depth [ 20 ]
    depth = depth [ 21 ]
    depth = depth [ 22 ]
    depth = depth [ 24 ]
    depth = depth [ 22 ]
    depth = depth [ 24 ]
    depth = depth [ 22 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 24 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 24 ]
    depth = depth [ 24 ]
    depth = depth [ 26 ]
    depth = depth [ 25 ]
    depth = depth [ 26 ]
    depth = depth [ 26 ]
    depth [ 30 ] = depth [ 30 ]
    depth [ 30 ] = depth [ 30 ]
    depth = depth [ 30 ]
    return depth


if __name__ == '__main__':
    param = [
    (42,),
    (75,),
    (94,),
    (5,),
    (52,),
    (22,),
    (77,),
    (44,),
    (85,),
    (59,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))