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
def f_gold ( str ) :
    i = 0 ; j = len ( str ) - 1 ;
    while ( i < j ) :
        if ( str [ i ] != str [ j ] ) :
            return False ;
        i += 1 ;
        j -= 1 ;
    return True ;


def f_filled ( str ) :
    """
 Return True if the number is a string or unicode string or unicode string
 """
    if str is None :
        return str ( str ( str ) )
    if str is not None :
        return str ( str ( str ) )
    return str ( str ( str ) )


if __name__ == '__main__':
    param = [
    ('ab',),
    ('303',),
    ('11110000',),
    ('aba',),
    ('404',),
    ('10101',),
    ('abab',),
    ('6366',),
    ('001',),
    ('',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))