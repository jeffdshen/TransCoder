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
    arr.sort ( )
    for i in range ( 0 , n - 1 , 2 ) :
        arr [ i ] , arr [ i + 1 ] = arr [ i + 1 ] , arr [ i ]


def f_filled ( arr , n ) :
    if n is None :
        return 0
    arr = arr.sort ( )
    for i in range ( n ) :
        arr [ i ] = arr [ i ]
    return arr


if __name__ == '__main__':
    param = [
    ([5, 11, 14, 14, 17, 20, 30, 35, 43, 44, 44, 45, 51, 56, 56, 61, 63, 65, 70, 71, 83],20,),
    ([52, 80, -10, 54, 58, -78, -30, -98],6,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1],5,),
    ([26, 83, 21, 22, 58, 42, 4, 14, 11, 53, 33, 3, 92, 44],10,),
    ([-94, -78, -76, -42, -26, -16, -10, 4, 16, 38, 60, 86, 98],9,),
    ([1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],8,),
    ([5, 12, 20, 26, 30, 35, 39, 44, 54, 56, 70, 72, 74, 74, 79, 80, 88, 95, 95, 98],10,),
    ([-80, 22, 36, 90, -22, -10, 40, -10, -68, 88, 48, 22, 8, 2, -76, -88, -2, 66, -84, 42, 0],12,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1],4,),
    ([61, 79, 82, 75, 51, 64, 20, 42, 57, 70, 9, 22, 64, 38, 60, 53, 53, 56, 24, 37, 52, 67, 47, 2, 59, 89, 82, 11, 22],20,)
        ]
    filled_function_param = [
    ([5, 11, 14, 14, 17, 20, 30, 35, 43, 44, 44, 45, 51, 56, 56, 61, 63, 65, 70, 71, 83],20,),
    ([52, 80, -10, 54, 58, -78, -30, -98],6,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1],5,),
    ([26, 83, 21, 22, 58, 42, 4, 14, 11, 53, 33, 3, 92, 44],10,),
    ([-94, -78, -76, -42, -26, -16, -10, 4, 16, 38, 60, 86, 98],9,),
    ([1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],8,),
    ([5, 12, 20, 26, 30, 35, 39, 44, 54, 56, 70, 72, 74, 74, 79, 80, 88, 95, 95, 98],10,),
    ([-80, 22, 36, 90, -22, -10, 40, -10, -68, 88, 48, 22, 8, 2, -76, -88, -2, 66, -84, 42, 0],12,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1],4,),
    ([61, 79, 82, 75, 51, 64, 20, 42, 57, 70, 9, 22, 64, 38, 60, 53, 53, 56, 24, 37, 52, 67, 47, 2, 59, 89, 82, 11, 22],20,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))