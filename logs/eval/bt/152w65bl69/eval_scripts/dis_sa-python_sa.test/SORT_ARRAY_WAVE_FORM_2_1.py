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
    for i in range ( 0 , n , 2 ) :
        if ( i > 0 and arr [ i ] < arr [ i - 1 ] ) :
            arr [ i ] , arr [ i - 1 ] = arr [ i - 1 ] , arr [ i ]
        if ( i < n - 1 and arr [ i ] < arr [ i + 1 ] ) :
            arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]


def f_filled ( arr , n ) :
    for i in range ( n ) :
        if n [ i ] == n [ i ] :
            return i
    return None


if __name__ == '__main__':
    param = [
    ([78, 81],1,),
    ([-44, -6, -7, -16, -15, 89, -78, -65, -84, -50, 22, 28, 13, 71, -83, -20, 86, 30, 32, -15, 67, -6, 34, -19, -31],16,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,),
    ([97, 18, 71, 65, 97, 1, 88, 4, 4, 82, 27, 43, 59, 32, 33, 28, 55, 60, 70, 62, 80, 34, 87, 88, 56, 13, 56, 18, 54, 77, 43, 39, 61, 42, 81, 79, 18, 23, 54, 30, 98, 58, 68, 67, 71, 18],32,),
    ([-60, -51, -48, -32, -30, 14, 93],5,),
    ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],22,),
    ([1, 14, 17, 18, 19, 22, 22, 29, 30, 30, 31, 35, 37, 38, 41, 42, 44, 52, 56, 56, 57, 62, 65, 67, 70, 75, 79, 84, 85, 87, 89, 93, 93, 98, 98],17,),
    ([-79],0,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([44, 53, 71, 79, 34, 46, 68],4,)
        ]
    filled_function_param = [
    ([78, 81],1,),
    ([-44, -6, -7, -16, -15, 89, -78, -65, -84, -50, 22, 28, 13, 71, -83, -20, 86, 30, 32, -15, 67, -6, 34, -19, -31],16,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,),
    ([97, 18, 71, 65, 97, 1, 88, 4, 4, 82, 27, 43, 59, 32, 33, 28, 55, 60, 70, 62, 80, 34, 87, 88, 56, 13, 56, 18, 54, 77, 43, 39, 61, 42, 81, 79, 18, 23, 54, 30, 98, 58, 68, 67, 71, 18],32,),
    ([-60, -51, -48, -32, -30, 14, 93],5,),
    ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],22,),
    ([1, 14, 17, 18, 19, 22, 22, 29, 30, 30, 31, 35, 37, 38, 41, 42, 44, 52, 56, 56, 57, 62, 65, 67, 70, 75, 79, 84, 85, 87, 89, 93, 93, 98, 98],17,),
    ([-79],0,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],14,),
    ([44, 53, 71, 79, 34, 46, 68],4,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))