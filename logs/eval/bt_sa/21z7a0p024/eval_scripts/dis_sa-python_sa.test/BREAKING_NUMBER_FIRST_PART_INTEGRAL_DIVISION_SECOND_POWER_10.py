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
def f_gold ( N ) :
    length = len ( N )
    l = int ( ( length ) / 2 )
    count = 0
    for i in range ( l + 1 ) :
        s = N [ 0 : 0 + i ]
        l1 = len ( s )
        t = N [ i : l1 + i ]
        try :
            if s [ 0 ] == '0' or t [ 0 ] == '0' :
                continue
        except :
            continue
        if s == t :
            count += 1
    return count


def f_filled ( N , size = 1 , size = 0 , size = None ) :
    length = len ( N )
    l = int ( size / 2 )
    l = l [ : size ]
    l = l [ : size ]
    l = l [ : size ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l = l [ size : size + 1 ]
    l += 1
    l += 1
    l += 1
    l += 1
    l [ size : size + 1 ] = l
    l [ size : size + 1 ] += l
    l += 1
    l [ size : size + 1 ] += l
    l += 1
    l [ size : size + 1 ] += l
    l += 1
    l += 1
l += 1
return l


if __name__ == '__main__':
    param = [
    ('ZCoQhuM',),
    ('2674377254',),
    ('11',),
    ('LbuGlvRyWAPBpo',),
    ('26382426486138',),
    ('111010111010',),
    ('hUInqJXNdbfP',),
    ('5191',),
    ('1110101101',),
    ('2202200',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))