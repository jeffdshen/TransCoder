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
def f_gold ( no ) :
    return 0 if no == 0 else int ( no % 10 ) + f_gold ( int ( no / 10 ) )


def f_filled ( no ) :
    if no.f_filled :
        return f_filled.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no.f_filled ( no

if __name__ == '__main__':
    param = [
    (73,),
    (91,),
    (27,),
    (79,),
    (31,),
    (84,),
    (68,),
    (9,),
    (85,),
    (35,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))