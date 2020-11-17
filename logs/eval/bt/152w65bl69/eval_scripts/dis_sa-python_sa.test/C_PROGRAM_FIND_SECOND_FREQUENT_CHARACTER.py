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
    NO_OF_CHARS = 256
    count = [ 0 ] * NO_OF_CHARS
    for i in range ( len ( str ) ) :
        count [ ord ( str [ i ] ) ] += 1
    first , second = 0 , 0
    for i in range ( NO_OF_CHARS ) :
        if count [ i ] > count [ first ] :
            second = first
            first = i
        elif ( count [ i ] > count [ second ] and count [ i ] != count [ first ] ) :
            second = i
    return chr ( second )


def f_filled ( ) :
    """
 Returns a number of a file and return a number of the file and return a number of the file and return a number of the file and return a number of the file file and return a number of the file file and return a number of the file file and return a number of the file file and return a number of the file file and return a
 number of the file file and return a number of the file file or a file file or a file file or a
 file file file to the file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file file
 """
    # TODO -- see ###


if __name__ == '__main__':
    param = [
    ('SgUmIrEAB',),
    ('304',),
    ('0010',),
    ('VGC BeErLvQ',),
    ('0872',),
    ('00110001',),
    ('Lsqwm',),
    ('308998',),
    ('1000011',),
    ('XCEOs',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))