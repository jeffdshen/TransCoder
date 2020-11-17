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
def f_gold ( arr1 , arr2 , m , n , x ) :
    count , l , r = 0 , 0 , n - 1
    while ( l < m and r >= 0 ) :
        if ( ( arr1 [ l ] + arr2 [ r ] ) == x ) :
            l += 1
            r -= 1
            count += 1
        elif ( ( arr1 [ l ] + arr2 [ r ] ) < x ) :
            l += 1
        else :
            r -= 1
    return count


def f_filled ( arr1 , arr2 , order = 0 , order = 1 , order = 1 ) :
    count = 0
    while order < order :
        r = ( ( order - order ) * order )
        if r <= order :
            break
    if order >= order :
        if order >= order :
            return ( ( ( order - order ) ) )
        if order >= order :
            return ( ( ( order - order ) ) )
        return ( ( ( order - order ) ) / ( ( order - order ) )
    

if __name__ == '__main__':
    param = [
    ([5, 5, 7, 10, 14, 14, 17, 21, 32, 34, 37, 40, 40, 40, 46, 46, 50, 50, 51, 55, 57, 62, 65, 67, 67, 69, 70, 70, 72, 73, 76, 77, 77, 78, 84, 85, 85, 86, 87, 88, 88, 89, 89, 90, 93, 99],[2, 5, 8, 8, 10, 12, 13, 15, 17, 18, 20, 20, 21, 27, 28, 31, 34, 37, 40, 46, 48, 52, 53, 54, 54, 58, 59, 60, 66, 68, 68, 69, 70, 71, 72, 73, 77, 77, 80, 84, 84, 92, 92, 95, 97, 97],28,29,23,),
    ([-84, 52, -34, 96, 16, 92, -64, -74],[-22, 26, -12, -54, 66, 86, 38, 76],6,5,7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],37,26,42,),
    ([60, 92, 42, 83, 55, 76, 29, 62],[71, 2, 74, 42, 80, 71, 26, 76],4,7,7,),
    ([-94, -94, -58, -40, -40, -26, -24, -22, -22, -22, -2, 0, 4, 8, 12, 16, 16, 18, 22, 32, 42, 44, 50, 58, 64, 78, 80, 90],[-86, -84, -78, -76, -72, -70, -62, -58, -54, -54, -50, -46, -44, -40, -30, -28, -16, -10, 10, 36, 36, 48, 70, 84, 84, 90, 94, 98],17,27,17,),
    ([0, 0, 1, 1, 1, 0, 0, 1, 1, 1],[1, 1, 1, 0, 1, 1, 0, 0, 0, 0],5,8,9,),
    ([1, 5, 7, 7, 7, 14, 15, 16, 17, 18, 18, 19, 20, 25, 27, 31, 36, 42, 47, 51, 56, 56, 56, 58, 58, 59, 63, 63, 63, 65, 66, 67, 76, 83, 93, 94, 97],[2, 3, 7, 8, 9, 10, 17, 18, 21, 28, 29, 29, 33, 35, 46, 47, 47, 49, 49, 49, 53, 56, 58, 59, 59, 60, 65, 67, 70, 78, 81, 85, 85, 87, 90, 92, 96],28,34,31,),
    ([78, -74, 52, 56, -8, 92, 14, 56, -72, -92, 32, -94, -26, -8, -66, 72, -24, 36, -84, -4, -68, 14, 78, 40, -82, -10, 16, 56, 6, -16, 30, 24, -32],[-74, 22, -14, -2, 36, 86, -70, -20, -76, -84, -40, -36, 42, 22, -60, -94, -18, 8, -14, -42, -68, 62, -60, 2, 40, -66, 68, 96, 70, 98, -38, -74, -92],16,30,24,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],25,33,33,),
    ([17, 50, 65, 4, 19, 10, 45, 70, 76, 81, 28, 97, 55, 70, 38, 2, 40, 67, 36, 33, 6, 85, 25],[78, 92, 65, 23, 7, 94, 18, 4, 2, 53, 31, 58, 98, 18, 46, 16, 17, 92, 80, 92, 43, 70, 50],16,22,22,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))