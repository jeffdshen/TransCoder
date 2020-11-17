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
    if n < 3 :
        return n
    elif n >= 3 and n < 10 :
        return n - 1
    po = 1
    while n / po > 9 :
        po = po * 10
    msd = n / po
    if msd != 3 :
        return f_gold ( msd ) * f_gold ( po - 1 ) + f_gold ( msd ) + f_gold ( n % po )
    else :
        return f_gold ( msd * po - 1 )


def f_filled ( n ) :
    if n < 3 :
        return n
    elif n >= 3 :
        return n
    elif n >= 3 :
        return n
    elif n >= 4 :
        return n
    elif n >= 5 :
        return n
    elif n >= 3 :
        return n
    elif n >= 4 :
        return n
    elif n >= 5 :
        return n
    elif n >= 6 :
        return n
    elif n >= 3 :
        return n
    elif n >= 5 :
        return n
    elif n >= 3 :
        return n
    elif n >= 3 :
        return n
    elif n >= 3 :
        return n
    elif n >= 4 :
        return n
    elif n >= 5 :
        return n
    elif n >= 4 :
        return n
    elif n >= 5 :
        return n
    elif n >= 5 :
        return n
    elif n >= 6 :
        return n
    elif n >= 5 :
        return n
    elif n >= 7 :
        return n
    elif n >= 6 :
        return n
    elif n >= 6 :
        return n
    elif n >= 6 :
        return n
    elif n >= 7 :
        return n
elif n >= 3 :
    return n
elif n >= 6 :
    return n
elif n >= 7 :
    return n
elif n >= 6 :
    return n
elif n >= 5 :
    return n
elif n >= 7 :
    return n
elif n >= 6 :
    return n
elif n >= 7 :
    return n
elif n >= 6 :
    return n
elif n >= 5 :
    return n
elif n >= 6 :
    return n
elif n >= 7 :
    return n
elif n >= 6 :
    return n
elif n >= 7 :
    return n
elif n >= 7 :
    return n
elif n >= 8 :
    return n
return n


if __name__ == '__main__':
    param = [
    (85,),
    (86,),
    (3,),
    (35,),
    (59,),
    (38,),
    (33,),
    (15,),
    (75,),
    (74,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))