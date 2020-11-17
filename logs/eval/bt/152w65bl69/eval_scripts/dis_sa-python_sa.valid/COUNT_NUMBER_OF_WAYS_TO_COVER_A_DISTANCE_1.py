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
def f_gold ( dist ) :
    count = [ 0 ] * ( dist + 1 )
    count [ 0 ] = 1
    count [ 1 ] = 1
    count [ 2 ] = 2
    for i in range ( 3 , dist + 1 ) :
        count [ i ] = ( count [ i - 1 ] + count [ i - 2 ] + count [ i - 3 ] )
    return count [ dist ] ;


def f_filled ( dist , count = - 1 ) :
    """
 Return the given of the given dist in a given dist of the given dist in a given dist in a given dist in a
 given dist is given a list of dist in a given dist in a given dist in a
 given dist is given in dist of the given dist in dist
 """
    if count is None :
        count = count - count
    return count


if __name__ == '__main__':
    param = [
    (37,),
    (82,),
    (87,),
    (80,),
    (92,),
    (58,),
    (98,),
    (53,),
    (11,),
    (58,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))