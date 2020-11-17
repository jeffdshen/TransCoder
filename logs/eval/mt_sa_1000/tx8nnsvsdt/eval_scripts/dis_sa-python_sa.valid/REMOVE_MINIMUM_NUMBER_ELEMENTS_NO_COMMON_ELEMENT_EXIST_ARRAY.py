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
def f_gold ( a , b , n , m ) :
    countA = dict ( )
    countB = dict ( )
    for i in range ( n ) :
        countA [ a [ i ] ] = countA.get ( a [ i ] , 0 ) + 1
    for i in range ( n ) :
        countB [ b [ i ] ] = countB.get ( b [ i ] , 0 ) + 1
    res = 0
    for x in countA :
        if x in countB.keys ( ) :
            res += min ( countA [ x ] , countB [ x ] )
    return res


def f_filled ( a , b , n , n ) :
    countA = dict ( )
    countB = dict ( )
    for i in range ( n ) :
        countA [ a [ i ] ] = countA.get ( a [ i ] , 0 ) + 1
    for i in range ( n ) :
        countB [ b [ i ] ] = countB.get ( b [ i ] , 0 ) + 1
    res = 0
    for x in countA :
        if x in countB.keys ( ) :
            res += min ( countA [ x ] , countB [ x ] )
return res


if __name__ == '__main__':
    param = [
    ([4, 7, 10, 12, 12, 24, 29, 38, 45, 51, 53, 54, 59, 68, 72, 73, 85, 86, 88, 92, 92, 95],[7, 9, 17, 23, 25, 26, 29, 32, 35, 56, 56, 58, 59, 59, 62, 63, 72, 82, 85, 86, 95, 97],15,13,),
    ([-6, 48, -70, 14, -86, 56, 80, -64, 64, -88, -14, 78, 14, -18, 52, 2, 22, 88],[-62, -58, 60, -30, 42, 8, 66, -48, -18, 64, -76, -90, -48, -90, -24, 64, -88, -98],15,9,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],10,10,),
    ([10, 93, 2, 16, 36, 49, 36, 86, 6, 99, 95, 2],[99, 28, 7, 21, 62, 89, 82, 41, 43, 77, 8, 14],6,10,),
    ([-98, -96, -80, -64, -42, -30, -6, 10, 62, 66, 82],[-62, -50, -42, 24, 44, 46, 52, 54, 60, 72, 72],9,6,),
    ([1, 1, 0, 1, 1],[1, 1, 1, 0, 0],4,2,),
    ([7, 11, 13, 15, 21, 33, 36, 39, 66, 99],[23, 36, 42, 44, 62, 65, 70, 78, 82, 89],9,9,),
    ([-40],[-98],0,0,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],31,26,),
    ([79, 91, 31, 16, 28, 45, 37, 43, 73, 73, 76, 28, 71, 60, 64, 60, 99, 36, 47, 38, 65, 34, 22, 94, 84, 51, 72, 45, 71, 2],[58, 94, 12, 27, 98, 38, 75, 20, 94, 43, 32, 90, 23, 41, 88, 2, 62, 96, 53, 57, 48, 79, 6, 16, 11, 46, 73, 57, 67, 7],18,18,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))