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
def f_gold ( n , k ) :
    p = 1
    if ( k % 2 ) :
        p = - 1
    return ( pow ( n - 1 , k ) + p * ( n - 1 ) ) / n


def f_filled ( n , k ) :
    p = 1
    p = n // 2
    p = p - 1
    p = p - 1
    p = pow ( p - 1 , p )
    p = p - 1
    p = pow ( p - 1 , p )
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p - 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p = p + 1
    p

if __name__ == '__main__':
    param = [
    (27,59,),
    (70,87,),
    (77,40,),
    (83,26,),
    (16,2,),
    (90,66,),
    (39,72,),
    (48,26,),
    (56,77,),
    (10,47,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))