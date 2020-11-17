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
def f_gold ( n ) :
    i = 0
    j = len ( n )
    pos = 0
    while ( i < j ) :
        if ( n [ i ] == '4' ) :
            pos = pos * 2 + 1
        if ( n [ i ] == '7' ) :
            pos = pos * 2 + 2
        i = i + 1
    return pos


def f_filled ( n ) :
    i = 0
    j = 0
    j = len ( n )
    j = 0
    while i < j :
        j += 1
        j += 1
        j += 1
        j += 1
    j += 1
return j


if __name__ == '__main__':
    param = [
    ('7',),
    ('305745689',),
    ('444',),
    ('4',),
    ('2074',),
    ('27',),
    ('447',),
    ('255',),
    ('10000111111011',),
    ('fAKcSDRTNz',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))