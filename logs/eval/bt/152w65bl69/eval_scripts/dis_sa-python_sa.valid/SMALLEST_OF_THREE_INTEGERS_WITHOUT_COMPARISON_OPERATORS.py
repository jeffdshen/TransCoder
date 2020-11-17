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
def f_gold ( x , y , z ) :
    c = 0
    while ( x and y and z ) :
        x = x - 1
        y = y - 1
        z = z - 1
        c = c + 1
    return c


def f_filled ( x , y , x1 , x1 , x2 ) :
    """
 Return the f_filled of the f_filled of the f_filled points of the f_filled points

 Parameters
 -----
 x : ndarray
 Input array
 Input array of the f_filled points of the f_filled points

 Returns
 -----
 x1 : ndarray
 Output array of the f_filled points of the f_filled points

 Returns
 ------
 x1 : ndarray
 Output array of the f_filled points of the f_filled points

 """
    return np.asarray ( x )


if __name__ == '__main__':
    param = [
    (23,98,25,),
    (87,55,94,),
    (35,90,29,),
    (25,9,41,),
    (93,22,39,),
    (52,42,96,),
    (95,88,26,),
    (91,64,51,),
    (75,1,6,),
    (96,44,76,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))