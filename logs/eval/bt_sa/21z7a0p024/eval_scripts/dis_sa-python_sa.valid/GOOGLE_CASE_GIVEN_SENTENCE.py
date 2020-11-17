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
def f_gold ( s ) :
    n = len ( s )
    s1 = ""
    s1 = s1 + s [ 0 ].lower ( )
    i = 1
    while i < n :
        if ( s [ i ] == ' ' and i <= n ) :
            s1 = s1 + " " + ( s [ i + 1 ] ).lower ( )
            i = i + 1
        else :
            s1 = s1 + ( s [ i ] ).upper ( )
        i = i + 1
    return s1


def f_filled ( s ) :
    n = len ( s )
    s1 = ''
    s1 = s1 [ 0 ].lower ( )
    s1 [ 1 ] = s1 [ 0 ].lower ( )
    s1 [ 1 ] = s1 [ 0 ].lower ( )
    s1 [ 1 ] = s1 [ 1 ]
    s1 [ 2 ] = s1 [ 1 ]
    s1 [ 2 ] = s1 [ 1 ]
    s1 [ 2 ] = s1 [ 2 ]
    s1 [ 2 ] = s1 [ 3 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 5 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 5 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 7 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 7 ]
    s1 [ 2 ] = s1 [ 8 ]
    s1 [ 2 ] = s1 [ 4 ]
    s1 [ 2 ] = s1 [ 5 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 7 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 7 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 7 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
    s1 [ 2 ] = s1 [ 6 ]
return s1


if __name__ == '__main__':
    param = [
    ('TEYndweqZA',),
    ('01865',),
    ('11001100',),
    ('CzwznJmQet',),
    ('318305446',),
    ('0000001111110',),
    ('yzT',),
    ('38630230',),
    ('01101',),
    ('zoizI',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))