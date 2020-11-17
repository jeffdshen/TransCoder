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
    maxPrime = - 1
    while n % 2 == 0 :
        maxPrime = 2
        n >>= 1
    for i in range ( 3 , int ( math.sqrt ( n ) ) + 1 , 2 ) :
        while n % i == 0 :
            maxPrime = i
            n = n / i
    if n > 2 :
        maxPrime = n
    return int ( maxPrime )


def f_filled ( n , maxPrime = - 1 ) :
    """
 Return a number of the maxPrime function to the number of the maxPrime function
 """
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = n - maxPrime
    maxPrime = maxPrime
    maxPrime = n - maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    maxPrime = maxPrime
    max

if __name__ == '__main__':
    param = [
    (98,),
    (8,),
    (78,),
    (65,),
    (55,),
    (10,),
    (10,),
    (37,),
    (39,),
    (15,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))