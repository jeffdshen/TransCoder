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
    num = n ;
    dec_value = 0 ;
    base = 1 ;
    temp = num ;
    while ( temp ) :
        last_digit = temp % 10 ;
        temp = int ( temp / 10 ) ;
        dec_value += last_digit * base ;
        base = base * 8 ;
    return dec_value ;


def f_filled ( n , num ) :
    n = n % n
    num = n % n
    num = n % n
    num = n % n
    num = n % n
    num = n % n
    num = n % n
    num = num % n
    num = num % num
    num = num % n
    num = num % n
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    num = num % num
    return num


if __name__ == '__main__':
    param = [
    (37,),
    (25,),
    (63,),
    (66,),
    (32,),
    (5,),
    (41,),
    (82,),
    (54,),
    (5,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))