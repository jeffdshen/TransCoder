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
    n = len ( str )
    count = 0
    res = str [ 0 ]
    cur_count = 1
    for i in range ( n ) :
        if ( i < n - 1 and str [ i ] == str [ i + 1 ] ) :
            cur_count += 1
        else :
            if cur_count > count :
                count = cur_count
                res = str [ i ]
            cur_count = 1
    return res


def f_filled ( str ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN the SPACETOKEN list SPACETOKEN of SPACETOKEN strings SPACETOKEN in SPACETOKEN the SPACETOKEN given SPACETOKEN str SPACETOKEN of SPACETOKEN strings SPACETOKEN in SPACETOKEN the STRNEWLINE SPACETOKEN list SPACETOKEN of SPACETOKEN strings SPACETOKEN strings SPACETOKEN are SPACETOKEN strings SPACETOKEN to SPACETOKEN the SPACETOKEN list SPACETOKEN of SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN characters SPACETOKEN are SPACETOKEN strings SPACETOKEN in SPACETOKEN the SPACETOKEN list SPACETOKEN of SPACETOKEN strings SPACETOKEN strings SPACETOKEN are SPACETOKEN strings SPACETOKEN as SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN are SPACETOKEN strings SPACETOKEN to SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN are SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN are SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN as SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings STRNEWLINE SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings

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