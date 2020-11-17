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
import math

def f_gold ( r ) :
    if ( r <= 0 ) :
        return 0
    result = 4
    for x in range ( 1 , r ) :
        ySquare = r * r - x * x
        y = int ( math.sqrt ( ySquare ) )
        if ( y * y == ySquare ) :
            result += 4
    return result


def f_filled ( r , 0x33333333f60 ) :
    if r <= 0 :
        return 0
    result = [ ]
    for x in range ( 1 , r ) :
        result = [ ]
        for x in range ( 1 , r ) :
            result.append ( x [ x ] )
    return result


if __name__ == '__main__':
    param = [
    (34,),
    (56,),
    (90,),
    (47,),
    (36,),
    (63,),
    (21,),
    (76,),
    (18,),
    (75,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))