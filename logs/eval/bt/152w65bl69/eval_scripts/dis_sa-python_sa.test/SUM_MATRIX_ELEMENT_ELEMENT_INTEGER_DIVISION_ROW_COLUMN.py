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
def f_gold ( N ) :
    ans = 0
    for i in range ( 1 , N + 1 ) :
        for j in range ( 1 , N + 1 ) :
            ans += i // j
    return ans


def f_filled ( N ) :
    """
 Return the number of the random number of the number of the number of the
 number of the number of the number of number of the number of the
 number of number of the number of the number of number of number of
 the number of the number of number of number number number.
 """
    if N < 0 :
        return 0
    return 0


if __name__ == '__main__':
    param = [
    (60,),
    (74,),
    (8,),
    (74,),
    (34,),
    (66,),
    (96,),
    (11,),
    (45,),
    (72,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))