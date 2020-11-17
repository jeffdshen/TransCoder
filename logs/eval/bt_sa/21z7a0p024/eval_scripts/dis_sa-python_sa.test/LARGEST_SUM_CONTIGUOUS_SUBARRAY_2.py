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
def f_gold ( a , size ) :
    max_so_far = a [ 0 ]
    curr_max = a [ 0 ]
    for i in range ( 1 , size ) :
        curr_max = max ( a [ i ] , curr_max + a [ i ] )
        max_so_far = max ( max_so_far , curr_max )
    return max_so_far


def f_filled ( a , size ) :
    max_so_far = a [ size [ 0 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 2 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 2 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 0 ] ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 2 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 1 ] ]
    curr_max = a [ size [ 2 ] ]
    curr_max = a [ size ]
    return curr_

if __name__ == '__main__':
    param = [
    ([1, 3, 4, 7, 8, 8, 10, 12, 16, 19, 19, 20, 20, 21, 21, 22, 26, 27, 29, 34, 36, 38, 38, 39, 41, 43, 44, 47, 47, 49, 57, 57, 60, 62, 63, 65, 75, 77, 77, 78, 81, 82, 82, 83, 83, 84, 85, 98, 99],38,),
    ([-40, 14, 2, -70, 86, -90, -50, -54, -2, 90, 30],10,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],18,),
    ([60, 69, 41, 7, 77, 36, 36, 26, 35, 30, 64, 75, 3, 35, 60, 71, 29, 47, 15, 29, 43, 88, 56, 22, 9, 45, 40, 50, 52],25,),
    ([-96, -88, -80, -72, -64, -64, -60, -60, -60, -58, -56, -54, -54, -50, -50, -26, -26, -24, -20, -8, -2, 0, 4, 4, 12, 14, 18, 18, 24, 32, 42, 44, 44, 44, 48, 50, 50, 56, 60, 60, 70, 80, 88, 88, 90, 98],35,),
    ([0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0],22,),
    ([2, 4, 4, 5, 6, 7, 11, 12, 14, 18, 23, 24, 27, 28, 33, 36, 37, 38, 39, 40, 41, 41, 48, 48, 52, 61, 64, 66, 66, 77, 79, 82, 85, 88, 91, 94, 99],34,),
    ([-56, 0, 16, 12, 20, 36, 32, -52, -68, -36, -96, -46, -34, 56, 2, 78, 6, 30, -68, -48, 2, 44, -26, -36, -30, -20, -90, -66, 4, 94, 8, 4, -4, -32, -24],20,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],22,),
    ([39, 87, 27, 89, 26, 25, 80, 82, 21, 25, 55, 27, 20, 81, 47, 79, 26, 72, 10, 11, 90, 89],21,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))