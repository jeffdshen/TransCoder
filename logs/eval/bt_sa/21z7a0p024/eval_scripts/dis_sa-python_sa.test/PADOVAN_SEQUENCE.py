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
    pPrevPrev , pPrev , pCurr , pNext = 1 , 1 , 1 , 1
    for i in range ( 3 , n + 1 ) :
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext
    return pNext ;


def f_filled ( n , tabtabtab0ee40 ) :
    ppecho = ( 1 , 1 , 1 , 1 )
    ppecho = ( 1 , 2 , 1 )
    for i in range ( 3 ) :
        ppecho = ( 1 , 2 )


if __name__ == '__main__':
    param = [
    (1,),
    (92,),
    (29,),
    (52,),
    (55,),
    (13,),
    (83,),
    (83,),
    (10,),
    (67,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))