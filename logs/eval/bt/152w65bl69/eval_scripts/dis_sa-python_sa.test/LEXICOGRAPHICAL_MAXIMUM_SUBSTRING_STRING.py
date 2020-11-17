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
    mx = ""
    for i in range ( len ( str ) ) :
        mx = max ( mx , str [ i : ] )
    return mx


def f_filled ( str ) :
    """
 Return the string of the given string and returns the string of the string and returns the
 string of the string and returns the string of the string and returns the
 string of the string string and returns the string string and returns the string string string.
 """
    for i in range ( len ( str ) ) :
        if i < len ( str ) :
            return str ( str ( str ( i ) ) )
    return str ( str ( str ( i ) ) )


if __name__ == '__main__':
    param = [
    ('HCoAefoaan',),
    ('80336005',),
    ('01111111110',),
    ('qIH',),
    ('4210598472796',),
    ('10101',),
    ('imqmKdatcgXjs',),
    ('950509666021',),
    ('10111101101',),
    ('wasqgYFvz',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))