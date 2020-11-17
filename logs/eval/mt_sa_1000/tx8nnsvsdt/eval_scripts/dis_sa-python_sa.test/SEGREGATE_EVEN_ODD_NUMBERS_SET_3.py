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
    i = - 1
    j = 0
    while ( j != n ) :
        if ( arr [ j ] % 2 == 0 ) :
            i = i + 1
            arr [ i ] , arr [ j ] = arr [ j ] , arr [ i ]
        j = j + 1
    for i in arr :
        print ( str ( i ) + " " , end = '' )


def f_filled ( arr , n ) :
    i = - 1
    j = 0
    while j != n :
        if arr [ j ] % 2 == 0 :
            i = i + 1
            arr [ i ] , arr [ i ] = arr [ j ] , arr [ i ]
        j = j + 1
for i in arr :
    print ( str ( i ) + "" , end = "" )


if __name__ == '__main__':
    param = [
    ([20, 67],1,),
    ([-54, 22, -42, -22, -48, -20, 34, -50, -22, -30, -94, 62, -24, 70, -54, -38, 84],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([62, 45, 87, 31, 67, 53, 61, 9, 20, 8, 99, 18, 69, 54, 99, 64, 35, 88, 85, 74, 58, 93, 65, 30, 96, 4, 77, 24, 54, 88, 43, 84, 62, 34, 93],28,),
    ([-28, -6, 18, 42, 98],2,),
    ([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],21,),
    ([10, 42, 46],2,),
    ([88, 4, -88, 2, -16, -74, -18, -60, 86, 88, -2, 82, -8, 54, -84, -4, 32, 20],17,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],35,),
    ([80, 52, 9, 56, 68, 69, 48, 40, 64, 73, 44, 4, 97, 20, 25, 66, 46, 64, 72, 79, 24],15,)
        ]
    filled_function_param = [
    ([20, 67],1,),
    ([-54, 22, -42, -22, -48, -20, 34, -50, -22, -30, -94, 62, -24, 70, -54, -38, 84],11,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],20,),
    ([62, 45, 87, 31, 67, 53, 61, 9, 20, 8, 99, 18, 69, 54, 99, 64, 35, 88, 85, 74, 58, 93, 65, 30, 96, 4, 77, 24, 54, 88, 43, 84, 62, 34, 93],28,),
    ([-28, -6, 18, 42, 98],2,),
    ([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],21,),
    ([10, 42, 46],2,),
    ([88, 4, -88, 2, -16, -74, -18, -60, 86, 88, -2, 82, -8, 54, -84, -4, 32, 20],17,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],35,),
    ([80, 52, 9, 56, 68, 69, 48, 40, 64, 73, 44, 4, 97, 20, 25, 66, 46, 64, 72, 79, 24],15,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))