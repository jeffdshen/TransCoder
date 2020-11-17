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
def f_gold ( x ) :
    return ( - ( ~ x ) ) ;


def f_filled ( x ) :
    return x * x + x


if __name__ == '__main__':
    param = [
    (20,),
    (68,),
    (52,),
    (61,),
    (3,),
    (88,),
    (41,),
    (78,),
    (94,),
    (18,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))