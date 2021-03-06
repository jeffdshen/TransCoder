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
    sum = 0
    for row in range ( n ) :
        sum = sum + ( 1 << row )
    return sum


def f_filled ( n ) :
    """
 Return the maximum value of the maximum value to the maximum value
 """
    for i in range ( n ) :
        if i < 0 :
            return 0
    return sum ( n * len ( n ) )


if __name__ == '__main__':
    param = [
    (21,),
    (4,),
    (31,),
    (79,),
    (38,),
    (75,),
    (36,),
    (32,),
    (23,),
    (65,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))