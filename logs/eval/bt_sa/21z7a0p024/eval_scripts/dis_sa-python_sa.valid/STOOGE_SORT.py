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
def f_gold ( arr , l , h ) :
    if l >= h :
        return
    if arr [ l ] > arr [ h ] :
        t = arr [ l ]
        arr [ l ] = arr [ h ]
        arr [ h ] = t
    if h - l + 1 > 2 :
        t = ( int ) ( ( h - l + 1 ) / 3 )
        f_gold ( arr , l , ( h - t ) )
        f_gold ( arr , l + t , ( h ) )
        f_gold ( arr , l , ( h - t ) )


def f_filled ( arr , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l , l ,

if __name__ == '__main__':
    param = [
    ([6, 25, 42, 52, 53, 54, 58, 66, 67, 70],6,6,),
    ([-13, -98, 50, -63, 48, 3, -76, 12, -35, 93, 29, 17, 16, 5, -97, -54, -45, -25],16,14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],28,24,),
    ([7, 49, 26, 33, 48, 79, 2, 71, 32, 4, 20, 36],9,10,),
    ([88],0,0,),
    ([1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],20,28,),
    ([2, 2, 4, 5, 7, 12, 12, 14, 14, 16, 17, 29, 29, 31, 32, 39, 41, 47, 48, 49, 51, 54, 58, 58, 59, 60, 73, 78, 80, 81, 82, 83, 84, 85, 90, 95, 97, 99, 99],28,29,),
    ([-31, -55, 6, 37, 77, 61, 0, 46, -91, -38, 85, -71, 25, 14, 53, 43, 34],15,11,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],12,17,),
    ([77, 68, 78, 97, 92, 52, 37, 8, 44, 98, 5, 69, 31, 45, 9, 32, 33, 67, 30, 76, 29, 3, 90, 57, 30, 9, 26, 2, 62, 3, 46, 68, 25, 51, 13, 44, 35, 55],27,20,)
        ]
    filled_function_param = [
    ([6, 25, 42, 52, 53, 54, 58, 66, 67, 70],6,6,),
    ([-13, -98, 50, -63, 48, 3, -76, 12, -35, 93, 29, 17, 16, 5, -97, -54, -45, -25],16,14,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],28,24,),
    ([7, 49, 26, 33, 48, 79, 2, 71, 32, 4, 20, 36],9,10,),
    ([88],0,0,),
    ([1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],20,28,),
    ([2, 2, 4, 5, 7, 12, 12, 14, 14, 16, 17, 29, 29, 31, 32, 39, 41, 47, 48, 49, 51, 54, 58, 58, 59, 60, 73, 78, 80, 81, 82, 83, 84, 85, 90, 95, 97, 99, 99],28,29,),
    ([-31, -55, 6, 37, 77, 61, 0, 46, -91, -38, 85, -71, 25, 14, 53, 43, 34],15,11,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],12,17,),
    ([77, 68, 78, 97, 92, 52, 37, 8, 44, 98, 5, 69, 31, 45, 9, 32, 33, 67, 30, 76, 29, 3, 90, 57, 30, 9, 26, 2, 62, 3, 46, 68, 25, 51, 13, 44, 35, 55],27,20,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))