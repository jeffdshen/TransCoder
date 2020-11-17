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
    res = n
    for j in range ( len ( n ) - 1 , - 1 , - 1 ) :
        res += n [ j ]
    return res


def f_filled ( n ) :
    res = [ ]
    res = res [ - 1 ]
    while res < 0 :
        res = res [ - 1 ]
        res = res [ - 1 ]
    return res


if __name__ == '__main__':
    param = [
    ('lSUhEvxcgfI',),
    ('77329283',),
    ('010111111',),
    ('Stazb',),
    ('0702',),
    ('01111111',),
    ('a',),
    ('359118754930',),
    ('11011010010',),
    ('rznb',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))