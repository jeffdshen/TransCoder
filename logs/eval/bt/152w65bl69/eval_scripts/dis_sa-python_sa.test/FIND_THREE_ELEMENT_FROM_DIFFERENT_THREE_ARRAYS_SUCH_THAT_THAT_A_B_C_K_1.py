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
def f_gold ( a1 , a2 , a3 , n1 , n2 , n3 , sum ) :
    s = set ( )
    for i in range ( n1 ) :
        s.add ( a1 [ i ] )
    for i in range ( n2 ) :
        for j in range ( n3 ) :
            if sum - a2 [ i ] - a3 [ j ] in s :
                return True
    return False


def f_filled let ( a1 , n1 , n1 , n1 , n1 , n1 ) :
    """ STRNEWLINE SPACETOKEN set SPACETOKEN of SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two STRNEWLINE SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two STRNEWLINE SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two STRNEWLINE SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two STRNEWLINE SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two SPACETOKEN two

if __name__ == '__main__':
    param = [
    ([6, 7, 10, 15, 28, 30, 30, 35, 38, 43, 44, 44, 54, 55, 64, 68, 69, 73, 75, 75, 86, 87, 92, 93, 94],[11, 17, 18, 24, 26, 26, 33, 35, 38, 41, 55, 60, 63, 63, 69, 73, 78, 81, 82, 87, 90, 91, 93, 94, 99],[3, 3, 8, 22, 24, 24, 28, 30, 32, 32, 34, 39, 40, 45, 46, 50, 54, 59, 75, 78, 79, 90, 95, 95, 97],21,16,17,18,),
    ([-72, -90, -92, 4, 22, 14, -50, 16, -56, -66, 62, -32, 82, 8, 12, -24, 92, -98, -94, 56, -74, -66, 26, -98, 10, -74, -14, 2, 60, -88, -84, 34, 82, 28, -86, -90, -92, 52, 72, 90, 92, -20, -86, 74, -96, -46, 28],[50, -20, 26, 32, -46, 38, 36, 0, -96, 60, -70, -36, -12, 50, 64, -70, 22, -22, 32, 60, -94, 98, -58, -86, -16, 40, -68, 2, -50, 6, -36, -28, -68, 44, -98, -38, -46, 68, 4, 60, -36, 28, -38, 4, 50, -84, -12],[-28, 20, -62, -84, 14, 10, 28, -10, 94, -2, 52, 66, 38, -50, 48, -88, -28, 92, -48, 86, 4, -16, 26, 26, -82, 44, 70, 72, -6, -98, 80, 56, 38, 42, -20, 64, 36, 80, 12, 4, -50, 54, 22, 98, -30, -52, 4],41,42,34,32,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],26,20,30,16,),
    ([85, 34, 78, 64, 22, 94, 52, 71, 44, 48, 46, 88, 59, 95, 4, 55, 21, 83, 56, 19, 85, 6, 87, 13],[58, 45, 14, 13, 73, 82, 34, 78, 83, 84, 39, 34, 65, 84, 84, 61, 26, 67, 48, 51, 41, 46, 89, 10],[46, 1, 2, 90, 31, 49, 62, 10, 28, 4, 48, 84, 87, 51, 88, 74, 99, 15, 35, 24, 32, 66, 10, 66],15,16,23,15,),
    ([-98, -98, -96, -94, -90, -90, -84, -36, -34, -34, -32, 16, 26, 26, 56, 74, 80],[-92, -70, -70, -56, -54, -48, -38, -14, -10, 0, 4, 30, 34, 70, 72, 76, 78],[-92, -88, -70, -56, -50, -50, -48, -36, -20, -10, -8, 2, 16, 22, 48, 70, 78],15,10,15,15,),
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1],[0, 0, 1, 0, 0, 1, 0, 1, 0, 1],[1, 1, 1, 1, 0, 1, 1, 1, 0, 1],5,7,9,6,),
    ([4, 4, 25, 27, 35, 39, 50, 60, 60, 63, 67, 73, 75, 81, 84, 85, 91, 98],[20, 21, 23, 25, 37, 41, 51, 57, 62, 66, 74, 77, 77, 79, 80, 87, 88, 95],[2, 3, 9, 10, 10, 18, 24, 40, 41, 47, 68, 69, 70, 86, 90, 95, 96, 98],12,17,13,9,),
    ([54, -64, 76, 78, 24, 40, 44, -56, 80, -10, -12, -8, -18, 42, 70, 14, -70, 48, -68, -98, -74, -40, -16, -90, 48, 92, -64, 58, -98, 60, -10, -10],[88, -66, -50, 74, -44, -32, -58, -24, -40, 62, 52, 88, -48, -2, -46, 38, 30, -56, 76, 56, 60, 52, -32, 36, 90, 92, -74, 88, -36, -14, -16, -14],[38, -96, 16, 38, -48, -22, -52, -78, 42, 94, -26, -20, 12, -10, 72, 16, -8, -2, -36, -76, -6, -92, 10, 34, -76, -54, -20, 20, -76, -46, 24, 44],23,18,29,19,),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],38,22,40,32,),
    ([28, 88, 75, 86, 51, 82, 2, 20, 22, 18, 96, 11],[62, 54, 79, 88, 27, 13, 48, 94, 86, 28, 86, 60],[49, 14, 18, 61, 94, 54, 12, 56, 97, 59, 85, 44],6,6,8,9,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))