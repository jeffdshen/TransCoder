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
def f_gold ( x ) :
    return ( x << 1 ) + x + ( x >> 1 )


def f_filled WithPoint3Point5 ( x , y , z ) :
    if x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return x
    elif x == y :
        return

if __name__ == '__main__':
    param = [
    (58,),
    (16,),
    (82,),
    (33,),
    (88,),
    (51,),
    (81,),
    (38,),
    (79,),
    (89,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))