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
def f_gold ( a , b ) :
    res = 0
    while ( b > 0 ) :
        if ( b & 1 ) :
            res = res + a
        a = a << 1
        b = b >> 1
    return res


def f_filled ( a , b ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN given SPACETOKEN list SPACETOKEN of SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN coefficients SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN coefficients STRNEWLINE SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN from SPACETOKEN lowest SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered STRNEWLINE SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered SPACETOKEN ordered

if __name__ == '__main__':
    param = [
    (4,33,),
    (36,67,),
    (65,52,),
    (55,37,),
    (35,76,),
    (69,98,),
    (84,62,),
    (5,80,),
    (15,36,),
    (67,84,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))