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
def f_gold ( s ) :
    n = len ( s )
    for i in range ( 1 , n ) :
        if s [ i ] != s [ 0 ] :
            return False
    return True


def f_filled ( s ) :
    """
 Return a list of the given string in the given string string.

 Args:
 s: A list of strings to be converted to the string as a string.
 s: A list of strings to be converted to the string as a string.
 """
    return s


if __name__ == '__main__':
    param = [
    ('',),
    ('ggg',),
    ('11',),
    ('KoYIHns',),
    ('232',),
    ('10111000011101',),
    ('DDDD',),
    ('11',),
    ('11111',),
    ('ewJvixQzu',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))