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
    i = 0
    j = n - 1
    while ( i < j ) :
        print ( arr [ j ] , end = " " )
        j -= 1
        print ( arr [ i ] , end = " " )
        i += 1
    if ( n % 2 != 0 ) :
        print ( arr [ i ] )


def f_filled ( arr , n ) :
    if n < 0 :
        return 0
    arr = arr [ 0 ]
    while arr < 0 :
        arr = arr [ 0 ]
        arr [ 1 : ] = arr [ 0 ]
        arr [ 1 : ] = arr [ 0 ]
        arr [ 1 : ] = arr [ 0 ]
    return arr


if __name__ == '__main__':
    param = [
    ([1, 4, 5, 8, 8, 10, 11, 13, 14, 15, 16, 19, 20, 20, 23, 31, 33, 34, 37, 41, 42, 43, 43, 44, 46, 46, 50, 55, 55, 61, 63, 65, 66, 67, 68, 79, 79, 84, 84, 84, 86, 89, 92, 96, 96],42,),
    ([64, 32, -48, -98, 74, -10, 36, 18, 28, 94, -52, 30, 94, -52, 90, -12, -78, 4, -78, 66, -92, -18, -44, -6, -38, -22, 62, 8, -84, -60, -26, 72, -78, 12, 34],19,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],13,),
    ([61, 41, 24, 22, 96, 75, 48, 83, 22, 93, 85, 67, 37, 48, 98, 13, 58, 89, 56, 99, 14, 55, 7, 3, 11, 68, 50, 16],22,),
    ([-92, -80, -80, -78, -76, -72, -70, -60, -58, -58, -56, -44, -34, -32, -32, -26, -20, -14, -10, -8, -6, 0, 6, 6, 6, 10, 16, 18, 28, 30, 36, 36, 38, 46, 48, 52, 56, 56, 60, 68, 92, 96],31,),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],15,),
    ([4, 10, 12, 13, 15, 17, 24, 26, 30, 31, 36, 41, 41, 45, 49, 56, 57, 57, 66, 75, 75, 78, 85, 93, 94],14,),
    ([-94, 66, -12, 20, 74, 10, -18, 50, -58, -88, -14, 68, 72, 64, 90, -14, -72, -44, -6, 86, 18, 50, -68, 62, -16, -68, 46, 6, 30, -26, -74, -22, 14, -70, -78, -12, -32, 96, 52, -16, 22, -2],40,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([16, 13, 96, 14, 49, 26],4,)
        ]
    filled_function_param = [
    ([1, 4, 5, 8, 8, 10, 11, 13, 14, 15, 16, 19, 20, 20, 23, 31, 33, 34, 37, 41, 42, 43, 43, 44, 46, 46, 50, 55, 55, 61, 63, 65, 66, 67, 68, 79, 79, 84, 84, 84, 86, 89, 92, 96, 96],42,),
    ([64, 32, -48, -98, 74, -10, 36, 18, 28, 94, -52, 30, 94, -52, 90, -12, -78, 4, -78, 66, -92, -18, -44, -6, -38, -22, 62, 8, -84, -60, -26, 72, -78, 12, 34],19,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],13,),
    ([61, 41, 24, 22, 96, 75, 48, 83, 22, 93, 85, 67, 37, 48, 98, 13, 58, 89, 56, 99, 14, 55, 7, 3, 11, 68, 50, 16],22,),
    ([-92, -80, -80, -78, -76, -72, -70, -60, -58, -58, -56, -44, -34, -32, -32, -26, -20, -14, -10, -8, -6, 0, 6, 6, 6, 10, 16, 18, 28, 30, 36, 36, 38, 46, 48, 52, 56, 56, 60, 68, 92, 96],31,),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],15,),
    ([4, 10, 12, 13, 15, 17, 24, 26, 30, 31, 36, 41, 41, 45, 49, 56, 57, 57, 66, 75, 75, 78, 85, 93, 94],14,),
    ([-94, 66, -12, 20, 74, 10, -18, 50, -58, -88, -14, 68, 72, 64, 90, -14, -72, -44, -6, 86, 18, 50, -68, 62, -16, -68, 46, 6, 30, -26, -74, -22, 14, -70, -78, -12, -32, 96, 52, -16, 22, -2],40,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([16, 13, 96, 14, 49, 26],4,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))