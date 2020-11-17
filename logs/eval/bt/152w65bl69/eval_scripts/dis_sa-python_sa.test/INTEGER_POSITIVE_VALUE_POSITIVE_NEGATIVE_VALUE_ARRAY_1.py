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
def f_gold ( arr , n ) :
    neg = 0
    pos = 0
    sum = 0
    for i in range ( 0 , n ) :
        sum += arr [ i ]
        if ( arr [ i ] < 0 ) :
            neg += 1
        else :
            pos += 1
    return ( sum / abs ( neg - pos ) )


def f_filled ( arr , n ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN array SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the STRNEWLINE SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of STRNEWLINE SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN the SPACETOKEN neg SPACETOKEN of SPACETOKEN ` ` n ` ` STRNEWLINE SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN neg SPACETOKEN of

if __name__ == '__main__':
    param = [
    ([49, 98],1,),
    ([82, 66, -68, 24, -10],2,),
    ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],8,),
    ([56, 3, 18, 5, 20, 56, 47, 29, 60, 98, 60, 40, 42, 2, 54, 56, 91, 8, 93, 14, 31, 27, 61, 49, 23, 12, 71],25,),
    ([-94, -94, -92, -86, -50, -48, -6, 8, 28, 40, 44, 58, 62, 72, 94],12,),
    ([0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],36,),
    ([16, 56, 56],1,),
    ([74, -90, -92, 30, -18, 66, -66, 22],5,),
    ([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],7,),
    ([21, 64, 82, 78, 30, 34, 35],5,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))