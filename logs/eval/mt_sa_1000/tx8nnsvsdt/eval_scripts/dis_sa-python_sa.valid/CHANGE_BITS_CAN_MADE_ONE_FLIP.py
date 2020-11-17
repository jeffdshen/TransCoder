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
    zeros = 0
    ones = 0
    for i in range ( 0 , len ( str ) ) :
        ch = str [ i ] ;
        if ( ch == '0' ) :
            zeros = zeros + 1
        else :
            ones = ones + 1
    return ( zeros == 1 or ones == 1 ) ;


def f_filled ( str ) :
    zeros = 0
    ones = 0
    for i in range ( 0 , len ( str ) ) :
        ch = str [ i ]
        if ch == '0' :
            zeros = zeros + 1
        else :
            ones = ones + 1
    return zeros == 1 or ones == 1


if __name__ == '__main__':
    param = [
    ("00001",),
    ("0000",),
    ("11",),
    ("111110",),
    ("1",),
    ("111010111010",),
    ("hUInqJXNdbfP",),
    ("5191",),
    ("1110101101",),
    ('NupSrU xz',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))