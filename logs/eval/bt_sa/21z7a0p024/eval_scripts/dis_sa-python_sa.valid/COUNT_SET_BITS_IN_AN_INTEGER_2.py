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
    count = 0
    while ( n ) :
        n &= ( n - 1 )
        count += 1
    return count


def f_filled ( n ) :
    count = 0
    count = 0
    for n in n :
        count += n
        count += n
        count += 1
        count += 1
        count += 1
    return count


if __name__ == '__main__':
    param = [
    (32,),
    (94,),
    (33,),
    (99,),
    (17,),
    (64,),
    (80,),
    (42,),
    (12,),
    (86,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))