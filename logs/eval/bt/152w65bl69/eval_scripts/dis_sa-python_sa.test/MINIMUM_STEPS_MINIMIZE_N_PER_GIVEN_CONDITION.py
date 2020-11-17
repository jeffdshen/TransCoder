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
    table = [ 0 ] * ( n + 1 )
    for i in range ( n + 1 ) :
        table [ i ] = n - i
    for i in range ( n , 0 , - 1 ) :
        if ( not ( i % 2 ) ) :
            table [ i // 2 ] = min ( table [ i ] + 1 , table [ i // 2 ] )
        if ( not ( i % 3 ) ) :
            table [ i // 3 ] = min ( table [ i ] + 1 , table [ i // 3 ] )
    return table [ 1 ]


def f_filled ( n ) :
    """
 Return the number of the given n in the given n of the given n in the given n in the given n is a
 number of the number of the number of the number of the number of the number of the number of
 the number of the number of the number of numbers
 """
    n = 0
    for n in n :
        n = n
        n = n
        n = n
        n = n
        n = n
        n = n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
        n = n % n
    return n


if __name__ == '__main__':
    param = [
    (59,),
    (7,),
    (90,),
    (78,),
    (49,),
    (15,),
    (45,),
    (56,),
    (7,),
    (70,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))