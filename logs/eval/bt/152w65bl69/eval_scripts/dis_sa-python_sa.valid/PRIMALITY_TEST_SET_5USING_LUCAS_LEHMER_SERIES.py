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
def f_gold ( p ) :
    checkNumber = 2 ** p - 1
    nextval = 4 % checkNumber
    for i in range ( 1 , p - 1 ) :
        nextval = ( nextval * nextval - 2 ) % checkNumber
    if ( nextval == 0 ) : return True
    else : return False


def f_filled ( p , checkNumber ) :
    return ( p.shape [ 1 ] == 2 )


if __name__ == '__main__':
    param = [
    (11,),
    (27,),
    (31,),
    (47,),
    (3,),
    (14,),
    (41,),
    (72,),
    (39,),
    (22,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))