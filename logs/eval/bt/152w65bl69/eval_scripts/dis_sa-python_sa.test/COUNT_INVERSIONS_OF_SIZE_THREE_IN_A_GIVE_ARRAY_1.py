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
    invcount = 0
    for i in range ( 1 , n - 1 ) :
        small = 0
        for j in range ( i + 1 , n ) :
            if ( arr [ i ] > arr [ j ] ) :
                small += 1
        great = 0 ;
        for j in range ( i - 1 , - 1 , - 1 ) :
            if ( arr [ i ] < arr [ j ] ) :
                great += 1
        invcount += great * small
    return invcount


def f_filled ( arr , n ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN array SPACETOKEN of SPACETOKEN the SPACETOKEN invat SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN coefficients SPACETOKEN ordered SPACETOKEN from SPACETOKEN ` arr ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN ` arr ` SPACETOKEN and SPACETOKEN ` n ` SPACETOKEN is SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN coefficients STRNEWLINE SPACETOKEN ordered SPACETOKEN from SPACETOKEN ` arr ` SPACETOKEN to SPACETOKEN be SPACETOKEN converted SPACETOKEN to SPACETOKEN ` arr ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN ` arr ` SPACETOKEN and SPACETOKEN ` n ` SPACETOKEN is SPACETOKEN a SPACETOKEN list SPACETOKEN of STRNEWLINE SPACETOKEN coefficients SPACETOKEN ordered SPACETOKEN from SPACETOKEN ` arr ` SPACETOKEN to SPACETOKEN be SPACETOKEN converted SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN ` arr ` SPACETOKEN and SPACETOKEN ` n ` SPACETOKEN are SPACETOKEN not STRNEWLINE SPACETOKEN converted SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN the SPACETOKEN array SPACETOKEN of SPACETOKEN the SPACETOKEN coefficients SPACETOKEN ordered STRNEWLINE SPACETOKEN from SPACETOKEN the SPACETOKEN ` arr ` SPACETOKEN to SPACETOKEN be SPACETOKEN converted SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN ` n ` SPACETOKEN of SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN be SPACETOKEN converted SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN be SPACETOKEN converted SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN in SPACETOKEN ` n ` SPACETOKEN of SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to STRNEWLINE SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN ` n ` SPACETOKEN to SPACETOKEN `

if __name__ == '__main__':
    param = [
    ([4, 75, 89],1,),
    ([84, -66, -52, 34, -28, -6, 20, 22, -78, -26, 14, 24, -92, -18, 32, -94, -64, -38, 56, 4, -10, 58, -66, -58, -10, -8, -62, -60, -26],26,),
    ([0, 0, 0, 1, 1, 1, 1, 1],7,),
    ([18, 7, 43, 57, 94, 37, 38, 41, 59, 64, 97, 29, 51, 37, 64, 91, 42, 83, 13, 22, 68],17,),
    ([-94, -86, -84, -84, -82, -66, -62, -58, -52, -48, -44, -40, -38, -32, -22, -22, -22, -14, -8, -6, -6, 0, 2, 20, 20, 26, 32, 32, 52, 56, 66, 74, 76, 80, 80, 86, 88, 94],34,),
    ([0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],9,),
    ([4, 8, 15, 19, 24, 31, 33, 36, 38, 45, 45, 52, 54, 65, 73, 75, 83, 84, 90, 92, 93],19,),
    ([80, -30, -44, 76, -96, 2, 22, -30, 36, -6, 88, -60, -90, -52, 78, 90, -52],10,),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],7,),
    ([74, 71, 28, 45, 14, 31, 17, 10, 82, 27, 45, 73, 93, 87, 57, 58],10,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))