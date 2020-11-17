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
def f_gold ( str ) :
    l = len ( str )
    count = 0
    res = str [ 0 ]
    for i in range ( l ) :
        cur_count = 1
        for j in range ( i + 1 , l ) :
            if ( str [ i ] != str [ j ] ) :
                break
            cur_count += 1
        if cur_count > count :
            count = cur_count
            res = str [ i ]
    return res


def f_filled ( str ) :
    l = len ( l )
    count = 0
    count = 0
    while count != 0 :
        if l [ 0 ] == '-' :
            count += 1
        else :
            count += 1
    return count


if __name__ == '__main__':
    param = [
    ('geeekk',),
    ('3786868',),
    ('110',),
    ('aaaabbcbbb',),
    ('11',),
    ('011101',),
    ('WoHNyJYLC',),
    ('3141711779',),
    ('10111101101',),
    ('aabbabababcc',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))