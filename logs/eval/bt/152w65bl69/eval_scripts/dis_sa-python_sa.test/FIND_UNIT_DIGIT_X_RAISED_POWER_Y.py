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
def f_gold ( x , y ) :
    res = 1
    for i in range ( y ) :
        res = ( res * x ) % 10
    return res


def f_filled ( x , y , y , z ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN given SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number STRNEWLINE SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN of SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number STRNEWLINE SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number STRNEWLINE SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number STRNEWLINE SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number STRNEWLINE SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number SPACETOKEN number

if __name__ == '__main__':
    param = [
    (33,55,),
    (95,7,),
    (21,63,),
    (3,62,),
    (40,53,),
    (64,24,),
    (17,23,),
    (58,74,),
    (44,13,),
    (27,54,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))