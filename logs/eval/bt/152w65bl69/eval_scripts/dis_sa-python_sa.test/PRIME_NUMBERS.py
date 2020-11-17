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
    if ( n <= 1 ) :
        return False
    for i in range ( 2 , n ) :
        if ( n % i == 0 ) :
            return False
    return True


def f_filled ( n ) :
    n = n % n
    n = n % n
    return n % n


if __name__ == '__main__':
    param = [
    (2,),
    (74,),
    (46,),
    (38,),
    (51,),
    (48,),
    (6,),
    (14,),
    (31,),
    (10,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))