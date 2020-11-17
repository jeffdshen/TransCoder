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
    m = 1 ;
    while ( x & m ) :
        x = x ^ m
        m <<= 1
    x = x ^ m
    return x


def f_filled ( x , m , n , n ) :
    m = 1
    for x in x :
        if x == n :
            return x
    return m


if __name__ == '__main__':
    param = [
    (96,),
    (66,),
    (67,),
    (13,),
    (75,),
    (78,),
    (1,),
    (83,),
    (27,),
    (65,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
