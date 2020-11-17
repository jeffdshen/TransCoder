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
import math

def f_gold ( n ) :
    result = 0
    for i in range ( 2 , ( int ) ( math.sqrt ( n ) ) + 1 ) :
        if ( n % i == 0 ) :
            if ( i == ( n / i ) ) :
                result = result + i
            else :
                result = result + ( i + n // i )
    return ( result + n + 1 )


def f_filled ( n ) :
    result = [ ]
    result = [ ]
    for i in range ( n ) :
        result.append ( result )
    return result


if __name__ == '__main__':
    param = [
    (76,),
    (21,),
    (4,),
    (49,),
    (35,),
    (55,),
    (43,),
    (39,),
    (36,),
    (5,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))