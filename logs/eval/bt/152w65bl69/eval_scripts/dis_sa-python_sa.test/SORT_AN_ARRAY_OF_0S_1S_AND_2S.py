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
def f_gold ( a , arr_size ) :
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi :
        if a [ mid ] == 0 :
            a [ lo ] , a [ mid ] = a [ mid ] , a [ lo ]
            lo = lo + 1
            mid = mid + 1
        elif a [ mid ] == 1 :
            mid = mid + 1
        else :
            a [ mid ] , a [ hi ] = a [ hi ] , a [ mid ]
            hi = hi - 1


def f_filled ( a , arr_size = 0 , size = 1 ) :
    """
 Returns a list of a given size of a given size and the given size of the
 size is a list of the given size of the given size of the size size to the size of the
 size is the size of the size size size size size.

 Returns:
 a list of the size size size size (i.e.size size)
 """
    for i in range ( arr_size ) :
        if size < size :
            size = i
    return a


if __name__ == '__main__':
    param = [
    ([5, 6, 8, 15, 42, 47, 49, 52, 53, 54, 55, 58, 58, 60, 60, 68, 70, 86, 94, 96, 97, 99],18,),
    ([-87, 14, 24, 6, 58, 47, 45, 20, -37, -81, -8, -42, 83, -10, 17, -38],14,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],4,),
    ([1, 16, 61, 64, 63, 69, 22, 93, 67, 76, 26, 16, 51, 86, 57, 29, 78, 92, 69, 47, 94, 62, 69, 76, 16, 90, 90, 48, 85, 39, 33, 94, 23, 10, 69, 34, 52, 95, 10, 19],20,),
    ([-98, -96, -84, -76, -20],2,),
    ([1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],15,),
    ([7, 8, 10, 12, 21, 23, 24, 24, 26, 29, 34, 36, 36, 36, 37, 49, 55, 58, 62, 64, 68, 73, 74, 75, 81, 82, 87, 89, 90, 90, 93, 96, 96, 99, 99],29,),
    ([-1, 5, -70, -83, 13, -38, -16, 12, -14, 41, 87, -81, 77, 0, 40, 89, 47, -24, -91, 99, -72, 28, -48],13,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([29, 37, 38, 83, 8],2,)
        ]
    filled_function_param = [
    ([5, 6, 8, 15, 42, 47, 49, 52, 53, 54, 55, 58, 58, 60, 60, 68, 70, 86, 94, 96, 97, 99],18,),
    ([-87, 14, 24, 6, 58, 47, 45, 20, -37, -81, -8, -42, 83, -10, 17, -38],14,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],4,),
    ([1, 16, 61, 64, 63, 69, 22, 93, 67, 76, 26, 16, 51, 86, 57, 29, 78, 92, 69, 47, 94, 62, 69, 76, 16, 90, 90, 48, 85, 39, 33, 94, 23, 10, 69, 34, 52, 95, 10, 19],20,),
    ([-98, -96, -84, -76, -20],2,),
    ([1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],15,),
    ([7, 8, 10, 12, 21, 23, 24, 24, 26, 29, 34, 36, 36, 36, 37, 49, 55, 58, 62, 64, 68, 73, 74, 75, 81, 82, 87, 89, 90, 90, 93, 96, 96, 99, 99],29,),
    ([-1, 5, -70, -83, 13, -38, -16, 12, -14, 41, 87, -81, 77, 0, 40, 89, 47, -24, -91, 99, -72, 28, -48],13,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],24,),
    ([29, 37, 38, 83, 8],2,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))