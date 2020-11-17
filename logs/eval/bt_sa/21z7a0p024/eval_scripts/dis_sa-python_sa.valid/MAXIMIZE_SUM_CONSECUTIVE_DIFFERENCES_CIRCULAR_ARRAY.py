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
def f_gold ( arr , n ) :
    sum = 0
    arr.sort ( )
    for i in range ( 0 , int ( n / 2 ) ) :
        sum -= ( 2 * arr [ i ] )
        sum += ( 2 * arr [ n - i - 1 ] )
    return sum


def f_filled ( arr , n ) :
    sum = 0
    sum = arr.sort ( )
    for i in range ( 0 , n + 1 ) :
        sum += 1
    return sum


if __name__ == '__main__':
    param = [
    ([8, 9, 12, 13, 17, 21, 24, 29, 37, 37, 39, 40, 41, 45, 49, 50, 53, 54, 56, 59, 60, 60, 70, 71, 72, 74, 77, 77, 78, 85, 89, 89, 90, 90, 95, 98, 98],34,),
    ([0, 48, -32, 28, -84, 14, 30, -80, 92, 76, -52, -20, 52, 78, 20, 32, 96, 66, 48, 26, 88, 6, 94, 32, -40, 44, -84, 54, -84, -80, -80, -64, -92, -84, -16, -18],24,),
    ([0, 0, 0, 1, 1, 1],3,),
    ([47, 7, 84, 96, 59, 53, 80],5,),
    ([-88, -80, -68, -62, -60, -60, -48, -46, -44, -38, -16, -16, 0, 0, 2, 8, 20, 36, 40, 40, 44, 54, 60, 68, 70, 82, 82, 84, 92, 94, 96],29,),
    ([1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],32,),
    ([2, 5, 10, 11, 13, 14, 15, 17, 17, 23, 23, 24, 27, 27, 28, 29, 30, 40, 42, 43, 46, 47, 51, 52, 57, 64, 65, 73, 74, 75, 76, 77, 81, 81, 82, 87, 89, 93, 95, 95, 99],35,),
    ([-72, -84, 84, 2, -76, 48, 12, -72, -92, -72, 38, 26, -38, 26, 50, 2, 20, 26, -48, 30, 24, -12, -84, -54, 20, -16, -94, 26, -22, 86],21,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],37,),
    ([57, 74, 53, 52, 80, 31, 27, 53, 8, 57, 46, 73, 46, 56, 73, 84, 37, 7, 97],13,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))