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
    i = 0
    ans = 0
    while ( ( 1 << i ) <= n ) :
        k = 0
        change = 1 << i
        for j in range ( 0 , n + 1 ) :
            ans += k
            if change == 1 :
                k = not k
                change = 1 << i
            else :
                change -= 1
        i += 1
    return ans


def f_filled ( n ) :
    """
 Return the value of the given value in the given value of the given value
 """
    for i in range ( n ) :
        if n <= 0 :
            return n
    return None


if __name__ == '__main__':
    param = [
    (90,),
    (56,),
    (43,),
    (31,),
    (77,),
    (35,),
    (43,),
    (66,),
    (15,),
    (95,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))