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

def f_gold ( num ) :
    result = 0
    i = 2
    while i <= ( math.sqrt ( num ) ) :
        if ( num % i == 0 ) :
            if ( i == ( num / i ) ) :
                result = result + i ;
            else :
                result = result + ( i + num / i ) ;
        i = i + 1
    return ( result + 1 ) ;


def f_filled ( num ) :
    result = 0
    result = 0
    for i in math.sqrt ( num ) :
        if num <= math.sqrt ( num ) :
            result += 1
    return result


if __name__ == '__main__':
    param = [
    (2,),
    (57,),
    (28,),
    (43,),
    (38,),
    (29,),
    (45,),
    (47,),
    (44,),
    (3,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))