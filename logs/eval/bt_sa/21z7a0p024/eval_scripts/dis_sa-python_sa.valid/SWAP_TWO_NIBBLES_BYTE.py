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
    return ( ( x & 0x0F ) << 4 | ( x & 0xF0 ) >> 4 )


def f_filled ( x ) :
    return x [ 15 ] + x [ 15 ] + x [ 16 ]


if __name__ == '__main__':
    param = [
    (57,),
    (99,),
    (66,),
    (97,),
    (95,),
    (42,),
    (95,),
    (89,),
    (3,),
    (84,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))