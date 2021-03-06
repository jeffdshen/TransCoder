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
    result = 0
    for i in range ( len ( str ) ) :
        if ( ( i == ord ( str [ i ] ) - ord ( 'a' ) ) or ( i == ord ( str [ i ] ) - ord ( 'A' ) ) ) :
            result += 1
    return result


def f_filled ( str ) :
    result = 0
    while True :
        if len ( str ) > len ( str ) :
            result = 0
        if len ( result ) > 1 :
            result += 1
        return result
    return result


if __name__ == '__main__':
    param = [
    ('lLkhFeZGcb',),
    ('ABcED',),
    ('geeksforgeeks',),
    ('Alphabetical',),
    ('abababab',),
    ('bcdefgxyz',),
    ('cBzaqx L',),
    (' bcd',),
    ('11',),
    ('MqqKY',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))