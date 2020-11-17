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
def f_gold ( x , y ) :
    while ( y != 0 ) :
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


def f_filled ( x , y , y , carry , carry ) :
    for x in y :
        y = x
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y = y
        y.append ( y )
        y = y
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )
        y.append ( y )


if __name__ == '__main__':
    param = [
    (56,60,),
    (17,44,),
    (73,96,),
    (75,3,),
    (27,54,),
    (61,1,),
    (65,63,),
    (22,19,),
    (61,9,),
    (97,23,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))