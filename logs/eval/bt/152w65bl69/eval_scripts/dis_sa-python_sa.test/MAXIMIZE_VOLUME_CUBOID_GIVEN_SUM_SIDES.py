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
    maxvalue = 0
    i = 1
    for i in range ( s - 1 ) :
        j = 1
        for j in range ( s ) :
            k = s - i - j
            maxvalue = max ( maxvalue , i * j * k )
    return maxvalue


def f_filled ( s , maxvalue = 1 ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN given SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the STRNEWLINE SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN of STRNEWLINE SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN the SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN maxvalue SPACETOKEN in SPACETOKEN maxvalue SPACETOKEN max

if __name__ == '__main__':
    param = [
    (67,),
    (48,),
    (59,),
    (22,),
    (14,),
    (66,),
    (1,),
    (75,),
    (58,),
    (78,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))