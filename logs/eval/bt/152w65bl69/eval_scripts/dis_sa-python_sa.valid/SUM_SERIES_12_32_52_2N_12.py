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
    for i in range ( 1 , n + 1 ) :
        sum = sum + ( 2 * i - 1 ) * ( 2 * i - 1 )
    return sum


def f_filled ( n ) :
    """
 Return the sum of the given n in a list of numbers
 """
    for i in range ( n ) :
        if i < 0 :
            return n
    return None


if __name__ == '__main__':
    param = [
    (14,),
    (61,),
    (37,),
    (86,),
    (47,),
    (98,),
    (70,),
    (24,),
    (76,),
    (24,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))