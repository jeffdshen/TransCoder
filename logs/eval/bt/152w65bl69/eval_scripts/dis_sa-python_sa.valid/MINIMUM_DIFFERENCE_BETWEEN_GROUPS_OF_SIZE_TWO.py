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
def f_gold ( a , n ) :
    a.sort ( ) ;
    s = [ ] ;
    i = 0 ;
    j = n - 1 ;
    while ( i < j ) :
        s.append ( ( a [ i ] + a [ j ] ) ) ;
        i += 1 ;
        j -= 1 ;
    mini = min ( s ) ;
    maxi = max ( s ) ;
    return abs ( maxi - mini ) ;


def f_filled ( a , n , n , n ) :
    if n < n :
        return 0
    n = 0
    for i in range ( n ) :
        n = n [ i ]
        n += n
    return n


if __name__ == '__main__':
    param = [
    ([11, 12, 14, 15, 20, 21, 28, 28, 30, 33, 39, 39, 42, 43, 44, 45, 48, 53, 53, 58, 59, 67, 68, 70, 70, 72, 74, 76, 76, 81, 87, 91],31,),
    ([28, -42, -14, 0, -56, 42, 14, 52, 58, 58, 92, -62, -14, -12, -84, -30, -94, -70, 18, -44, 88, -60],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],19,),
    ([90, 8, 24, 31, 70, 61, 78, 67, 49, 28, 31, 4, 64, 66, 21, 61, 6, 49, 10, 46, 34, 31, 48, 28, 78, 70, 44, 9, 38, 2, 4, 36, 76, 37, 32, 97, 46, 85, 76],37,),
    ([-98, -78, -68, -58, -26, -10, 32, 42, 90, 96],8,),
    ([1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],35,),
    ([8, 17, 23, 25, 29, 32, 35, 35, 52, 56, 57, 59, 70, 71, 77, 88, 96],16,),
    ([62, -10, 82, 18, 46],3,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([42, 71, 12, 33, 3, 58, 60, 60, 5, 52, 46, 53, 43, 50, 98, 53, 16, 82, 39, 93, 70, 13, 93, 69, 7, 92, 76, 11, 61, 48, 27, 28, 20, 76, 44, 24, 52, 56, 21, 82, 49, 5, 61, 76, 67],40,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))