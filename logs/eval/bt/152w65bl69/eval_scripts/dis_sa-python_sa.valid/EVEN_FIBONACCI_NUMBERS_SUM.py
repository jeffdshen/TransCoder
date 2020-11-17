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
def f_gold ( limit ) :
    if ( limit < 2 ) :
        return 0
    ef1 = 0
    ef2 = 2
    sm = ef1 + ef2
    while ( ef2 <= limit ) :
        ef3 = 4 * ef2 + ef1
        if ( ef3 > limit ) :
            break
        ef1 = ef2
        ef2 = ef3
        sm = sm + ef2
    return sm


def f_filled ( limit , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef1 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , ef2 , e

if __name__ == '__main__':
    param = [
    (67,),
    (89,),
    (12,),
    (94,),
    (96,),
    (25,),
    (49,),
    (8,),
    (33,),
    (59,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))