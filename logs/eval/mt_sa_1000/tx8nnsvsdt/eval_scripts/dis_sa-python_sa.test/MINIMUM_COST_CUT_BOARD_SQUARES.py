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
def f_gold ( X , Y , m , n ) :
    res = 0
    X.sort ( reverse = True )
    Y.sort ( reverse = True )
    hzntl = 1 ; vert = 1
    i = 0 ; j = 0
    while ( i < m and j < n ) :
        if ( X [ i ] > Y [ j ] ) :
            res += X [ i ] * vert
            hzntl += 1
            i += 1
        else :
            res += Y [ j ] * hzntl
            vert += 1
            j += 1
    total = 0
    while ( i < m ) :
        total += X [ i ]
        i += 1
    res += total * vert
    total = 0
    while ( j < n ) :
        total += Y [ j ]
        j += 1
    res += total * hzntl
    return res


def f_filled ( X , Y , m , n ) :
    res = 0
    X.sort ( reverse = True )
    Y.sort ( reverse = True )
    hzntl += 1
    i = 0
    j = 0
    while i < m and j < n :
        if X [ i ] > Y [ j ] :
            res += X [ i ] * vert
            hzntl += 1
            i += 1
        else :
            res += Y [ j ] * hzntl
            vert += 1
            j += 1
    total = 0
    while m < m :
        if i < m [ i ] < j :
            res += 1
if total < 0 :
    total += 1
return res


if __name__ == '__main__':
    param = [
    ([1, 9, 9, 16, 18, 20, 22, 22, 23, 25, 25, 26, 28, 32, 33, 33, 33, 34, 37, 40, 44, 46, 46, 52, 53, 56, 58, 58, 59, 60, 61, 67, 67, 69, 70, 70, 73, 75, 77, 83, 87, 87, 87, 90, 90, 93, 97, 98],[2, 3, 9, 10, 13, 16, 17, 19, 20, 23, 25, 27, 29, 30, 30, 35, 37, 39, 39, 45, 47, 50, 55, 55, 55, 56, 59, 60, 62, 63, 67, 70, 70, 71, 72, 73, 73, 74, 77, 86, 87, 88, 91, 92, 95, 96, 97, 99],25,27,),
    ([-52, 66, 66, -4, -74, 78, 52, -72],[-40, 30, -34, -76, 84, 88, -78, 72],6,7,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],15,19,),
    ([58, 78, 48, 44, 63, 37, 89, 76, 66, 83, 52, 97, 19, 28, 67, 38, 54, 77, 2, 96, 28, 87],[37, 36, 26, 5, 83, 75, 33, 33, 72, 63, 91, 94, 75, 92, 9, 19, 79, 29, 40, 47, 63, 36],13,14,),
    ([-84, -78, -76, -72, -68, -62, -62, -60, -58, -44, -34, -10, -8, -4, -2, -2, 14, 16, 20, 26, 26, 32, 70, 78, 86, 90, 96],[-98, -98, -86, -82, -76, -62, -60, -48, -32, -32, -24, -18, -10, -4, 0, 16, 16, 26, 36, 42, 48, 50, 64, 66, 78, 92, 98],15,24,),
    ([0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],25,26,),
    ([30, 75],[10, 39],1,1,),
    ([70, 78, -60, -10, -8, 46, 38, 60, -54, -68, 16, 10, 36, -10, 38, -96, -52, -82, -56, 22, -56, 0, 96, -60, 24, 70, 40, 62, -20, -36, 74, 32, 44, 14, -18, 50, 58],[64, -42, -50, -76, 46, 32, -66, 86, -6, 46, 94, 70, -62, 90, 78, 4, 6, -20, 92, -18, -34, -96, 92, -24, -90, -94, 62, 40, -14, -28, 80, -86, -86, -56, 40, -92, -22],19,19,),
    ([0, 0, 0, 1],[0, 1, 1, 1],2,2,),
    ([81, 40, 29, 74, 13, 67, 10, 25, 24, 81, 90],[51, 45, 23, 7, 53, 14, 49, 58, 25, 75, 74],8,10,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))