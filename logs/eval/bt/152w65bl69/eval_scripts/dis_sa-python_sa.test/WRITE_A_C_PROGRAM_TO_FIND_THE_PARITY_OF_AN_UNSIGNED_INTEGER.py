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
def f_gold ( n ) :
    parity = 0
    while n :
        parity = ~ parity
        n = n & ( n - 1 )
    return parity


def f_filled ( n ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN given SPACETOKEN n SPACETOKEN of SPACETOKEN the SPACETOKEN given SPACETOKEN n SPACETOKEN in SPACETOKEN the SPACETOKEN given SPACETOKEN n SPACETOKEN of SPACETOKEN n SPACETOKEN in SPACETOKEN the SPACETOKEN given SPACETOKEN n SPACETOKEN n SPACETOKEN is SPACETOKEN a STRNEWLINE SPACETOKEN number SPACETOKEN of SPACETOKEN n SPACETOKEN n SPACETOKEN in SPACETOKEN the SPACETOKEN given SPACETOKEN n SPACETOKEN n SPACETOKEN is SPACETOKEN a SPACETOKEN number SPACETOKEN of SPACETOKEN n SPACETOKEN n SPACETOKEN n.STRNEWLINE STRNEWLINE SPACETOKEN Parameters STRNEWLINE SPACETOKEN - - - - - STRNEWLINE SPACETOKEN n SPACETOKEN : SPACETOKEN int STRNEWLINE SPACETOKEN Number SPACETOKEN of SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n n SPACETOKEN n n SPACETOKEN n n n SPACETOKEN n n n n n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n n SPACETOKEN n SPACETOKEN n n n n n n n n n SPACETOKEN n n STRNEWLINE STRNEWLINE

if __name__ == '__main__':
    param = [
    (63,),
    (64,),
    (85,),
    (36,),
    (20,),
    (63,),
    (42,),
    (19,),
    (62,),
    (97,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))