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
def f_gold ( a , b , x , y ) :
    if a == 0 :
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1
    gcd = f_gold ( b % a , a , x1 , y1 )
    x = y1 - ( b / a ) * x1
    y = x1
    return gcd


def f_filled ( a , b , c , c ) :
    if c == 0 :
        x = 0
        y = 0
    else :
        x = 0
        y = c
    if c == 1 :
        return 1
    x = c
    y = c [ 0 ]
    z = c [ 1 ]
    y = c [ 2 ]
    z = c [ 1 ]
    z = c [ 2 ]
    z = c [ 2 ]
    z = c [ 2 ]
    z = c [ 2 ]
    z = c [ 3 ]
    z = c [ 4 ]
    z = c [ 5 ]
    z = c [ 6 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 6 ]
    z = c [ 10 ]
    z = c [ 6 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 10 ]
    z = c [ 6 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 6 ]
    z = c [ 8 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 6 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 6 ]
    z = c [ 7 ]
    z = c [ 8 ]
    z = c [ 9 ]
    z = c [ 10 ]
    z = c [ 10 ]
    z = c [ 11 ]
    z = c [ 12 ]
    z = c [ 13 ]
    z = c [ 14 ]
    z = c [ 14 ]
    z = c [ 14 ]
    z = c [ 14 ]
    z = c [ 16 ]
    z = c [ 16 ]
    z = c [ 16 ]
    z = c [ 16 ]
    z = z [ 18 ]
    z = c [ 16 ]
    z += z
    z += z
    return z


if __name__ == '__main__':
    param = [
    (44,17,10,65,),
    (33,81,67,20,),
    (39,77,21,34,),
    (52,96,23,97,),
    (64,48,17,33,),
    (45,32,89,3,),
    (53,88,24,74,),
    (86,19,29,21,),
    (57,67,30,32,),
    (11,86,96,81,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))