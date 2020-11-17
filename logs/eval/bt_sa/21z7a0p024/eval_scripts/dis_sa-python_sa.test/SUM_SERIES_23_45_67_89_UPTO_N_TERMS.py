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
    i = 1 ;
    res = 0.0 ;
    sign = True ;
    while ( n > 0 ) :
        n = n - 1 ;
        if ( sign ) :
            sign = False ;
            res = res + ( i + 1 ) / ( i + 2 ) ;
            i = i + 2 ;
        else :
            sign = True ;
            res = res - ( i + 1 ) / ( i + 2 ) ;
            i = i + 2 ;
    return res ;


def f_filled ( n ) :
    i = 1
    while i < n :
        i = 1
        while i < n :
            i += 1
            while i < n :
                i += 1
                if i > n :
                    i += 1
        return i
    

if __name__ == '__main__':
    param = [
    (49,),
    (4,),
    (60,),
    (90,),
    (96,),
    (29,),
    (86,),
    (47,),
    (77,),
    (87,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if abs(1 - (0.0000001 + abs(f_gold(*parameters_set))) / (abs(f_filled(*parameters_set)) + 0.0000001)) < 0.001:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))