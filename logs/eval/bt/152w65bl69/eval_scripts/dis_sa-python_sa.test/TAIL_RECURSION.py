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
    if ( n == 0 ) :
        return 1
    return n * f_gold ( n - 1 )


def f_filled ( n ) :
    return n % 2


if __name__ == '__main__':
    param = [
    (77,),
    (62,),
    (42,),
    (16,),
    (82,),
    (37,),
    (29,),
    (32,),
    (82,),
    (91,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))