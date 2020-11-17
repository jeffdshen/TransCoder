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
def f_gold ( n , d ) :
    return ( n & ( d - 1 ) )


def f_filled ( n , d ) :
    return ( d , d - 1 )


if __name__ == '__main__':
    param = [
    (54,59,),
    (39,84,),
    (35,81,),
    (9,60,),
    (62,68,),
    (16,16,),
    (93,96,),
    (32,38,),
    (39,62,),
    (63,16,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))