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
def f_gold ( p ) :
    first = 1
    second = 1
    number = 2
    next = 1
    while ( next ) :
        next = ( first + second ) % p
        first = second
        second = next
        number = number + 1
    return number


def f_filled ( p , first = True ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN first SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first STRNEWLINE SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first STRNEWLINE SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first STRNEWLINE SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first STRNEWLINE SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first STRNEWLINE SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first SPACETOKEN first first SPACETOKEN first SPACETOKEN first SPACETOKEN first first SPACETOKEN first first SPACETOKEN first first SPACETOKEN first first SPACETOKEN first SPACETOKEN first first SPACETOKEN first first first first SPACETOKEN first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first first

if __name__ == '__main__':
    param = [
    (51,),
    (40,),
    (68,),
    (7,),
    (8,),
    (32,),
    (93,),
    (75,),
    (71,),
    (15,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))