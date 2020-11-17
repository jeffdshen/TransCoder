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
def f_gold ( num ) :
    if ( num < 0 ) :
        return False
    sum , n = 0 , 1
    while ( sum <= num ) :
        sum = sum + n
        if ( sum == num ) :
            return True
        n += 1
    return False


def f_filled ( num ) :
    if num < 0 :
        return False
    else :
        return True


if __name__ == '__main__':
    param = [
    (97,),
    (97,),
    (32,),
    (40,),
    (18,),
    (14,),
    (90,),
    (39,),
    (1,),
    (57,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))