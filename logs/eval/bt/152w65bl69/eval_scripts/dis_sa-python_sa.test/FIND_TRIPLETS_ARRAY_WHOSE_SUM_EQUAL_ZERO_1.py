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
    found = False
    for i in range ( n - 1 ) :
        s = set ( )
        for j in range ( i + 1 , n ) :
            x = - ( arr [ i ] + arr [ j ] )
            if x in s :
                print ( x , arr [ i ] , arr [ j ] )
                found = True
            else :
                s.add ( arr [ j ] )
    if found == False :
        print ( "No Triplet Found" )


def f_filled ( arr , n = None ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN the SPACETOKEN number SPACETOKEN of SPACETOKEN the SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN for SPACETOKEN a SPACETOKEN range SPACETOKEN of SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN for SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN for SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN of SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN for SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN of SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN of SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN of SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN in SPACETOKEN ` ` n ` ` SPACETOKEN of STRNEWLINE SPACETOKEN ` ` n

if __name__ == '__main__':
    param = [
    ([1, 7, 12, 18, 18, 25, 26, 28, 29, 33, 33, 37, 39, 39, 53, 54, 55, 59, 61, 63, 63, 65, 66, 68, 68, 71, 71, 77, 81, 85, 90, 93, 94, 95, 97],18,),
    ([38, 68, 16, 96, -10, 6, 86, -42, -66, -2, -10, 48, 16, -28, 92, -24, 0, 46, -58, -58, 56, -70, 10, -2, -92, -80, 14, -78, 16, -84, -88, 42, -24, 6, 86, 82, 84],19,),
    ([0, 0, 0, 0, 1, 1, 1, 1],6,),
    ([45],0,),
    ([-80, -68, -54, -44, -40, -38, -32, -28, -22, -18, -12, -10, 14, 24, 38, 38, 40, 42, 46, 46, 64, 64, 66, 68, 68, 68, 70, 96],20,),
    ([0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],13,),
    ([1, 3, 4, 6, 8, 9, 10, 10, 11, 17, 17, 21, 22, 22, 25, 32, 34, 38, 46, 46, 48, 51, 58, 59, 62, 63, 64, 65, 70, 70, 72, 72, 72, 74, 77, 78, 81, 82, 83, 89, 90, 92, 95, 97],43,),
    ([-70, 78, 70, 20, -52, 36, -42, 34, -56, -94],9,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],7,),
    ([72, 50, 10, 44, 66, 67, 76, 19, 3, 24, 76, 56, 53, 42, 15, 50, 86, 43, 77, 28, 42, 65, 92, 73, 60, 86, 52, 65],21,)
        ]
    filled_function_param = [
    ([1, 7, 12, 18, 18, 25, 26, 28, 29, 33, 33, 37, 39, 39, 53, 54, 55, 59, 61, 63, 63, 65, 66, 68, 68, 71, 71, 77, 81, 85, 90, 93, 94, 95, 97],18,),
    ([38, 68, 16, 96, -10, 6, 86, -42, -66, -2, -10, 48, 16, -28, 92, -24, 0, 46, -58, -58, 56, -70, 10, -2, -92, -80, 14, -78, 16, -84, -88, 42, -24, 6, 86, 82, 84],19,),
    ([0, 0, 0, 0, 1, 1, 1, 1],6,),
    ([45],0,),
    ([-80, -68, -54, -44, -40, -38, -32, -28, -22, -18, -12, -10, 14, 24, 38, 38, 40, 42, 46, 46, 64, 64, 66, 68, 68, 68, 70, 96],20,),
    ([0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],13,),
    ([1, 3, 4, 6, 8, 9, 10, 10, 11, 17, 17, 21, 22, 22, 25, 32, 34, 38, 46, 46, 48, 51, 58, 59, 62, 63, 64, 65, 70, 70, 72, 72, 72, 74, 77, 78, 81, 82, 83, 89, 90, 92, 95, 97],43,),
    ([-70, 78, 70, 20, -52, 36, -42, 34, -56, -94],9,),
    ([0, 0, 0, 0, 1, 1, 1, 1, 1],7,),
    ([72, 50, 10, 44, 66, 67, 76, 19, 3, 24, 76, 56, 53, 42, 15, 50, 86, 43, 77, 28, 42, 65, 92, 73, 60, 86, 52, 65],21,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        f_filled(*(filled_function_param[i]))
        f_gold(*parameters_set)
        if parameters_set == filled_function_param[i]:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))