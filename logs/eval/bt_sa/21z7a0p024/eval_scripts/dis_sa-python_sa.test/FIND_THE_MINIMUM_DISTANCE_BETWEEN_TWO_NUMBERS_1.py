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
import sys

def f_gold ( arr , n , x , y ) :
    min_dist = sys.maxsize
    for i in range ( n ) :
        if arr [ i ] == x or arr [ i ] == y :
            prev = i
            break
    while i < n :
        if arr [ i ] == x or arr [ i ] == y :
            if arr [ prev ] != arr [ i ] and ( i - prev ) < min_dist :
                min_dist = i - prev
                prev = i
            else :
                prev = i
        i += 1
    return min_dist


def f_filled ( arr , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n , n ,

if __name__ == '__main__':
    param = [
    ([4, 7, 7, 8, 11, 14, 16, 25, 34, 35, 36, 36, 38, 40, 41, 43, 45, 47, 57, 60, 64, 72, 73, 74, 75, 82, 83, 83, 84, 84, 84, 92],22,7,40,),
    ([96, 70, 88, -64, -42, 58, 92, 66, -14, 90, -66, 12, 88, -12, 48, -4, 90, 24, 98, 14, 32, 38, 98, 78, 2, 26, 12, -36, 90, 80, 40, 58, 88, 64, 16],25,58,70,),
    ([0, 0, 1],1,1,1,),
    ([46, 96, 82, 73, 30, 36, 56, 20, 5, 36, 4, 7, 89, 63, 54, 97, 80, 56, 93, 34, 90, 56, 25, 27, 75, 68, 14, 90],26,54,82,),
    ([-96, -88, -82, -66, -62, -52, -52, -46, -46, -40, -40, -28, -24, -12, 0, 4, 10, 24, 42, 46, 48, 48, 50, 60, 62, 64, 64, 70, 92, 98],24,0,4,),
    ([0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],10,0,1,),
    ([1, 2, 2, 6, 10, 14, 15, 18, 19, 22, 23, 29, 30, 37, 40, 40, 41, 41, 42, 42, 44, 46, 46, 54, 56, 72, 73, 81, 83, 83, 86, 88, 93],27,1,42,),
    ([46, 86, -52, 18, -32, 86, 2, 38, 72, 72, -60, 70, -58, 66, -66, -72, -74, 58, 52, 58, 16, 64, 62, -62, 80, -70, -96, -44, -20, -74, -10, 14, -32, 48, 30, 76, -16, 80, 66, -46, -92, 26, -86, 28, -76, -24, -98, 54, 50],30,25,45,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],38,0,0,),
    ([32, 65, 10, 72, 17, 58, 79, 28, 67, 36, 18, 35],7,10,7,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))