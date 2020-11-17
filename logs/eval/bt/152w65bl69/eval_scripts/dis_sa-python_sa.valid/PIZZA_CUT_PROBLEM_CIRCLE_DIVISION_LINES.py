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
    return int ( 1 + n * ( n + 1 ) / 2 )


def f_filled ( n ) :
    return int ( n )


if __name__ == '__main__':
    param = [
    (46,),
    (68,),
    (4,),
    (12,),
    (56,),
    (14,),
    (81,),
    (29,),
    (26,),
    (40,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))