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
def f_gold ( arr , n , k ) :
    result = + 2147483647
    arr.sort ( )
    for i in range ( n - k + 1 ) :
        result = int ( min ( result , arr [ i + k - 1 ] - arr [ i ] ) )
    return result


def f_filled ( arr , n , num ) :
    result = 2147483647
    result = arr.sort ( )
    for i in range ( n , n - 1 , num - 1 ) :
        result [ i ] = 0
    return result


if __name__ == '__main__':
    param = [
    ([1, 1, 2, 7, 8, 14, 16, 20, 20, 23, 24, 24, 29, 30, 32, 34, 35, 37, 38, 43, 44, 46, 50, 52, 55, 57, 61, 71, 79, 86, 86, 89, 91, 91, 95],33,17,),
    ([78, -4, 76, 0, -62, 54, -70, 62, 90, -80, -68, 90, -34, -66, -46, 34, -18, -74, -66, 34, 34, -28, 6, 80, 58, -50, -60, 54, 8, -52, -60, 68, 42, 16, 42, 72, 54, 88, 44, 46, 84, -34],33,33,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],8,13,),
    ([32],0,0,),
    ([-96, -78, -76, -72, -72, -70, -54, -46, -40, -34, -30, -26, -24, -22, -18, -16, -6, -4, -4, 2, 6, 14, 16, 18, 30, 30, 36, 54, 54, 58, 66, 72, 78, 80, 80, 82, 88, 98],26,25,),
    ([0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],39,41,),
    ([3, 13, 14, 18, 23, 32, 67, 72, 75, 76, 87, 95],10,8,),
    ([8, 30],1,1,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],27,33,),
    ([31, 15, 19, 41, 73, 29, 67, 36, 87, 74, 95, 27, 36, 83, 37, 33, 30, 86, 94, 93, 9, 42, 3, 95, 3, 69, 67, 63, 16, 53, 35, 52, 2, 57, 57, 25, 21, 7, 72, 52, 78, 40],36,37,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))