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
    return ( n != 0 and ( ( n & ( n - 1 ) ) == 0 ) and not ( n & 0xAAAAAAAA ) ) ;


def f_filled ( n ) :
    return n [ 0 ] != n [ 0 ] and n [ 1 ] != n [ 0 ] and n [ 1 ] != n [ 1 ] and n [ 2 ] != n [ 3 ] and n [ 4 ] != n [ 5 ] and n [ 6 ] != n [ 7 ] and n [ 8 ] != n [ 8 ] and n [ 9 ] != n [ 10 ] and n [ 12 ] != n [ 13 ] and n [ 14 ] != n [ 14 ] and n [ 16 ] != n [ 18 ] and n [ 16 ] != n [ 18 ] and n [ 20 ] != n [ 19 ] and n [ 20 ] != n [ 20 ] and n [ 20 ] != n [ 19 ] and n [ 21 ] != n [ 21 ] and n [ 20 ] != n [ 21 ] and n [ 20 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ] and n [ 21 ] != n [ 21 ]


if __name__ == '__main__':
    param = [
    (1,),
    (4,),
    (64,),
    (-64,),
    (128,),
    (1024,),
    (97,),
    (86,),
    (14,),
    (99,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))