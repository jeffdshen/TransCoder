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
import math

def f_gold ( x , y ) :
    x = x % 10
    if y != 0 :
        y = y % 4 + 4
    return ( ( ( int ) ( math.pow ( x , y ) ) ) % 10 )


def f_filled ( x ) :
    y = x [ 10 : 10 ]
    if x != 0 :
        return x [ 10 : 4 ]
    else :
        return x


if __name__ == '__main__':
    param = [
    (37,17,),
    (70,52,),
    (26,23,),
    (9,96,),
    (82,71,),
    (95,36,),
    (43,40,),
    (7,27,),
    (19,56,),
    (49,28,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))