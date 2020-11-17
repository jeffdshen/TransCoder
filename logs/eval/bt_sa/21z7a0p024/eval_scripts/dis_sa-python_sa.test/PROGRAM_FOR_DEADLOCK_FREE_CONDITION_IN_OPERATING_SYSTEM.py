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
def f_gold ( process , need ) :
    minResources = 0
    minResources = process * ( need - 1 ) + 1
    return minResources


def f_filled ( ) :
    minf_filled = 0
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled = minf_filled + 1
    minf_filled += 1
    minf_filled += 1
    minf_filled += 1
    minf_filled += 1


if __name__ == '__main__':
    param = [
    (38,37,),
    (82,3,),
    (2,26,),
    (38,72,),
    (31,85,),
    (80,73,),
    (11,9,),
    (2,31,),
    (26,59,),
    (37,67,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))