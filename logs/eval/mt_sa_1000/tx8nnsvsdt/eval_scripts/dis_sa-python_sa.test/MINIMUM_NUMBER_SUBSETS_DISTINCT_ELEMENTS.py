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
def f_gold ( ar , n ) :
    res = 0
    ar.sort ( )
    for i in range ( 0 , n ) :
        count = 1
        for i in range ( n - 1 ) :
            if ar [ i ] == ar [ i + 1 ] :
                count += 1
            else :
                break
        res = max ( res , count )
    return res


def f_filled ( ar , n ) :
    res = 0
    ar.sort ( )
    for i in range ( 0 , n ) :
        count = 1
        for i in range ( n - 1 ) :
            if ar [ i ] == ar [ i + 1 ] :
                count += 1
            else :
                break
    res = max ( res , count )
return res


if __name__ == '__main__':
    param = [
    ([1, 2, 5, 8, 16, 21, 21, 22, 23, 26, 26, 27, 27, 29, 31, 33, 36, 37, 37, 38, 42, 45, 47, 50, 57, 58, 60, 60, 62, 63, 66, 66, 76, 84, 84, 88, 96, 99],25,),
    ([-30, -60, 34, 4, 86, 80, -96, -94, 52, 46, 8, 82, -94, -96, 78, 82, -22, -36, 78, 50, -46, -36, 80, 24, -14, 94, -46, -38, 82, 4, -24, 2, 4, -82, -82, -18, -62, 12, 8, 92, 70, -10],35,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],34,),
    ([38, 47, 84, 49, 48, 62, 48, 41, 38, 48, 92, 16, 99],6,),
    ([-88, -64, -40, -38, -38, -16, 16, 20, 28, 40, 56, 58, 60, 68, 74, 92],12,),
    ([1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],29,),
    ([14, 24, 82, 87, 95],3,),
    ([-34, 62, 40, -84, 52, -76, 2, -58, 94, 22, 2, -18, -88, 62, -14, 46, 50, -58, -80, 68, -64, 90, -58, 12, 76, -40, 40, -46, 8, -80, 4, -90, 14, -10, 64, -68],34,),
    ([0, 1, 1, 1],3,),
    ([43, 41, 90, 5, 6, 17, 68, 68, 86, 89],7,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))