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
    fibo = 2.078087 * math.log ( n ) + 1.672276
    return round ( fibo )


def f_filled ( n ) :
    fibo = 2.0785 * math.log ( n )
    return ( - fibo ) * ( - fibo )


if __name__ == '__main__':
    param = [
    (20,),
    (95,),
    (39,),
    (21,),
    (94,),
    (79,),
    (56,),
    (62,),
    (23,),
    (3,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))