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
    if ( n < 4 ) :
        return - 1
    rem = n % 4
    if ( rem == 0 ) :
        return n // 4
    if ( rem == 1 ) :
        if ( n < 9 ) :
            return - 1
        return ( n - 9 ) // 4 + 1
    if ( rem == 2 ) :
        return ( n - 6 ) // 4 + 1
    if ( rem == 3 ) :
        if ( n < 15 ) :
            return - 1
        return ( n - 15 ) // 4 + 2


def f_filled ( n ) :
    if n < 4 :
        return - 1
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = [ ]
    rem = rem [ : - 1 ]
    rem = [ ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ] - q = q
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    rem = rem [ : - 1 ]
    for i in range ( n - 1 ) :
        q = rem [ : - 1 ]
        rem [ i - 1 ] += q
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem [ : - 1 ] += q [ : - 1 ]
        rem = rem [ : - 1 ]
        rem = rem [ : - 1 ]
        return rem , rem
    

if __name__ == '__main__':
    param = [
    (55,),
    (35,),
    (24,),
    (75,),
    (5,),
    (7,),
    (50,),
    (28,),
    (67,),
    (59,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))