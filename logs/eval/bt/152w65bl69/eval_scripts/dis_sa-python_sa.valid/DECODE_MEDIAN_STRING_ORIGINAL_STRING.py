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
def f_gold ( s ) :
    l = len ( s )
    s1 = ""
    if ( l % 2 == 0 ) :
        isEven = True
    else :
        isEven = False
    for i in range ( 0 , l , 2 ) :
        if ( isEven ) :
            s1 = s [ i ] + s1
            s1 += s [ i + 1 ]
        else :
            if ( l - i > 1 ) :
                s1 += s [ i ]
                s1 = s [ i + 1 ] + s1
            else :
                s1 += s [ i ]
    return s1


def f_filled ( s ) :
    """ STRNEWLINE SPACETOKEN Return SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN the SPACETOKEN range SPACETOKEN of SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN range SPACETOKEN in SPACETOKEN a SPACETOKEN list SPACETOKEN of SPACETOKEN range SPACETOKEN and STRNEWLINE SPACETOKEN the SPACETOKEN range SPACETOKEN of SPACETOKEN range SPACETOKEN in SPACETOKEN the SPACETOKEN range SPACETOKEN range SPACETOKEN ( i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.SPACETOKEN i.e.

if __name__ == '__main__':
    param = [
    (' EgvQCeqYpZtv',),
    ('488540',),
    ('0000101010111',),
    ('syw',),
    ('402355',),
    ('0',),
    ('wmHMlAtq',),
    ('7962',),
    ('111111',),
    ('UbgRGDquop',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))