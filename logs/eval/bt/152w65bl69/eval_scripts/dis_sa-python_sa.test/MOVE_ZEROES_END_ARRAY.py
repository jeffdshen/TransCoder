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
    count = 0
    for i in range ( n ) :
        if arr [ i ] != 0 :
            arr [ count ] = arr [ i ]
            count += 1
    while count < n :
        arr [ count ] = 0
        count += 1


def f_filled ( arr , n ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN array SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN count SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN count SPACETOKEN count SPACETOKEN in SPACETOKEN the STRNEWLINE SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN count SPACETOKEN in SPACETOKEN the SPACETOKEN count SPACETOKEN of SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count SPACETOKEN count

if __name__ == '__main__':
    param = [
    ([2, 5, 12, 13, 15, 16, 31, 34, 42, 42, 43, 44, 48, 52, 54, 56],16,),
    ([70, 50, 10, 52],4,),
    ([0, 0, -30, 0, 0, -10, 0, 0, 0, 12, 0, 0, 0, -5, 1],15,),
    ([51, 16, 1, 47, 67, 3, 97, 16, 2, 30, 1, 1, 25, 96, 13, 64, 73],17,),
    ([-78, -10, 62],3,),
    ([1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],12,),
    ([4, 11, 18, 19, 24, 28, 30, 31, 36, 38, 44, 49, 50, 51, 63, 63, 68, 69, 70, 77, 78, 88, 92, 92],21,),
    ([-72, 8, -86, -82, -90, 0, -94, -82, -62, -8, 52, -6, -6, 60, -94, 56, -20, -78, -58, 6, 52, 88],22,),
    ([1, 1, -4, 0, -1, 1, 0, 1, 0, 1, -3, 1],12,),
    ([69, 45, 44, 19, 56, 22, 7, 31, 19, 33, 71, 84, 55, 62, 6, 84, 36, 7, 40],15,)
        ]
    filled_function_param = [
    ([2, 5, 12, 13, 15, 16, 31, 34, 42, 42, 43, 44, 48, 52, 54, 56],16,),
    ([70, 50, 10, 52],4,),
    ([0, 0, -30, 0, 0, -10, 0, 0, 0, 12, 0, 0, 0, -5, 1],15,),
    ([51, 16, 1, 47, 67, 3, 97, 16, 2, 30, 1, 1, 25, 96, 13, 64, 73],17,),
    ([-78, -10, 62],3,),
    ([1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],12,),
    ([4, 11, 18, 19, 24, 28, 30, 31, 36, 38, 44, 49, 50, 51, 63, 63, 68, 69, 70, 77, 78, 88, 92, 92],21,),
    ([-72, 8, -86, -82, -90, 0, -94, -82, -62, -8, 52, -6, -6, 60, -94, 56, -20, -78, -58, 6, 52, 88],22,),
    ([1, 1, -4, 0, -1, 1, 0, 1, 0, 1, -3, 1],12,),
    ([69, 45, 44, 19, 56, 22, 7, 31, 19, 33, 71, 84, 55, 62, 6, 84, 36, 7, 40],15,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
