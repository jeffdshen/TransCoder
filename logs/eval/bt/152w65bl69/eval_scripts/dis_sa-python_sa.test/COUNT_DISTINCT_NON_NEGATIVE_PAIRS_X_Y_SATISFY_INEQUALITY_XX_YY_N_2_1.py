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
    x = 0
    res = 0
    yCount = 0
    while ( yCount * yCount < n ) :
        yCount = yCount + 1
    while ( yCount != 0 ) :
        res = res + yCount
        x = x + 1
        while ( yCount != 0 and ( x * x + ( yCount - 1 ) * ( yCount - 1 ) >= n ) ) :
            yCount = yCount - 1
    return res


def f_filled ( n ) :
    """
 Return the number of the input to a number of the input input input.
 """
    # We need to check the input input input input
    # for the input input input input input
    # for the input input input input input SPACETOKEN input SPACETOKEN input SPACETOKEN input
    # for the input input input input input SPACETOKEN input SPACETOKEN input SPACETOKEN input SPACETOKEN input SPACETOKEN input SPACETOKEN input SPACETOKEN input SPACETOKEN input
    # for input input input input.
    # for input input input input input input input input input input.
    # for input input input input input input.
    # for input input input input input input input input input input.
    # for input input input input input input input input input input input input.


if __name__ == '__main__':
    param = [
    (72,),
    (75,),
    (92,),
    (30,),
    (45,),
    (40,),
    (81,),
    (17,),
    (81,),
    (99,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))