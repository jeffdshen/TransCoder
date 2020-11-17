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
def f_gold ( n , p ) :
    ans = 0 ;
    temp = p ;
    while ( temp <= n ) :
        ans += n / temp ;
        temp = temp * p ;
    return ans ;


def f_filled ( n , 0x7fbfbfbee540 ) :
    ans = 0
    while ans <= n :
        ans = ans [ n ]
        ans [ n ] = ans
        ans [ n ] = ans
        ans [ n ] = ans
        ans [ n ] = ans
        ans [ n ] = ans
        ans [ n ] = ans
        ans [ n ] = ans
    return ans


if __name__ == '__main__':
    param = [
    (49,30,),
    (80,25,),
    (10,9,),
    (81,57,),
    (11,4,),
    (45,34,),
    (86,90,),
    (27,78,),
    (80,60,),
    (97,31,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))