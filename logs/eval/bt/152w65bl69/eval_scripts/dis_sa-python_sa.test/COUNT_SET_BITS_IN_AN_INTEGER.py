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
        count += n & 1
        n >>= 1
    return count


def f_filled ( n ) :
    count = 0
    count = 0
    count = 0
    count = count
    count = count
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
    count += 1
return count


if __name__ == '__main__':
    param = [
    (58,),
    (92,),
    (73,),
    (52,),
    (24,),
    (14,),
    (58,),
    (11,),
    (8,),
    (52,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))