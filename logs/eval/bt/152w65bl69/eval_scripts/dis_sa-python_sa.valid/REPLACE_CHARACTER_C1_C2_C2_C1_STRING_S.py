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
def f_gold ( s , c1 , c2 ) :
    l = len ( s )
    for i in range ( l ) :
        if ( s [ i ] == c1 ) :
            s = s [ 0 : i ] + c2 + s [ i + 1 : ]
        elif ( s [ i ] == c2 ) :
            s = s [ 0 : i ] + c1 + s [ i + 1 : ]
    return s


def f_filled ( s ) :
    """
 Returns a string representing the given string in the given string and
 f_filled the string of the string to the string in the string string.

 Parameters
 -----
 s : str
 The string string to f_filled the string string to f_filled the string in the
 string string to f_filled the string string.

 Returns
 -----
 out : str
 The string string to f_filled the string to f_filled the string.

 Returns
 -----
 out : ndarray
 The string to f_filled the string string in the string.

 Returns
 -----
 out : ndarray
 The string to f_filled the string string to f_filled the string.

 """
    return s


if __name__ == '__main__':
    param = [
    ('IZTSMw j','W','k',),
    ('7288334','6','9',),
    ('010110000','1','1',),
    ('b gJX','t','P',),
    ('734','4','4',),
    ('1','1','1',),
    ('xCaUKdhA','X','S',),
    ('4370992644981','5','6',),
    ('01010','0','1',),
    ('ZNIFGshaWA','Q','x',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))