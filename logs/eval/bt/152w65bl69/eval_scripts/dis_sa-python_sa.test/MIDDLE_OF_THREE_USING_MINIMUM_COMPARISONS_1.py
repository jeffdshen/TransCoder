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
def f_gold ( a , b , c ) :
    if a > b :
        if ( b > c ) :
            return b
        elif ( a > c ) :
            return c
        else :
            return a
    else :
        if ( a > c ) :
            return a
        elif ( b > c ) :
            return c
        else :
            return b


def f_filled ( a , b , c , c , c , c , c ) :
    if c is None :
        c = c
    else :
        c = c
    if c is None :
        c = c
    return c


if __name__ == '__main__':
    param = [
    (43,24,7,),
    (76,54,66,),
    (57,5,40,),
    (10,13,4,),
    (59,47,56,),
    (92,14,50,),
    (49,62,65,),
    (16,95,12,),
    (33,41,90,),
    (66,63,46,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))