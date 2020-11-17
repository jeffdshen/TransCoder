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
def f_gold ( s , K ) :
    n = len ( s )
    c1 = 0
    c2 = 0
    C = 0
    for i in range ( n ) :
        if s [ i ] == 'a' :
            c1 += 1
        if s [ i ] == 'b' :
            c2 += 1
            C += c1
    return C * K + ( K * ( K - 1 ) / 2 ) * c1 * c2


def f_filled ( s ) :
    """
 Returns a list of a list of a list of list of strings
 """
    # We are only the list of strings strings
    # we are only in the list of strings
    # and we are only in the list of strings strings are only in the list of strings
    # and the list of strings strings are in strings
    # strings strings as strings strings strings as strings
    # strings strings as strings strings strings strings as strings
    # strings strings strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings SPACETOKEN strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings
    # strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings SPACETOKEN strings
    # strings strings strings strings strings strings
    # strings strings strings strings strings strings
    # strings strings strings strings strings strings strings
    # strings strings strings strings strings strings strings strings strings strings strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings SPACETOKEN strings
    # strings strings strings


if __name__ == '__main__':
    param = [
   ('abbc',96,),
('abahk',7,),
('hugbabab',5,),
('abadbc',60,),
('nkg9',8,),
('jh7dab',41,),
('abd',87,),
('aabb8yk',4,),
('1111',18,),
('PFXAhr',8,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))
