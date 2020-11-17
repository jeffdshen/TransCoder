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
def f_gold ( num ) :
    series = [ 1 , 3 , 2 , - 1 , - 3 , - 2 ] ;
    series_index = 0 ;
    result = 0 ;
    for i in range ( ( len ( num ) - 1 ) , - 1 , - 1 ) :
        digit = ord ( num [ i ] ) - 48 ;
        result += digit * series [ series_index ] ;
        series_index = ( series_index + 1 ) % 6 ;
        result %= 7 ;
    if ( result < 0 ) :
        result = ( result + 7 ) % 7 ;
    return result ;


def f_filled ( num , series , series = None ) :
    """ STRNEWLINE SPACETOKEN Returns SPACETOKEN the SPACETOKEN series SPACETOKEN of SPACETOKEN a SPACETOKEN series SPACETOKEN series SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN in SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Returns SPACETOKEN the SPACETOKEN series SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN for SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Returns SPACETOKEN a SPACETOKEN series SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN for SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Returns SPACETOKEN a SPACETOKEN series SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN for SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Returns SPACETOKEN a SPACETOKEN series SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN for SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Returns STRNEWLINE SPACETOKEN - - - - - STRNEWLINE SPACETOKEN a SPACETOKEN series SPACETOKEN ` ` series _ series ` ` SPACETOKEN for SPACETOKEN ` ` series _ series ` `.STRNEWLINE STRNEWLINE SPACETOKEN Examples STRNEWLINE SPACETOKEN - - - - - STRNEWLINE SPACETOKEN >> > SPACETOKEN from SPACETOKEN numpy.polynomial.hermite _ e SPACETOKEN import SPACETOKEN series STRNEWLINE SPACETOKEN >> > SPACETOKEN series SPACETOKEN = SPACETOKEN series.hermite _ e SPACETOKEN import SPACETOKEN series STRNEWLINE SPACETOKEN >> > SPACETOKEN series.hermite _ e SPACETOKEN = SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series STRNEWLINE SPACETOKEN >> > SPACETOKEN series.hermite _ e SPACETOKEN = SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series STRNEWLINE SPACETOKEN >> > SPACETOKEN series.hermite _ e SPACETOKEN = SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _ e SPACETOKEN + SPACETOKEN series.hermite _

if __name__ == '__main__':
    param = [
    ('K',),
    ('850076',),
    ('00111',),
    ('X',),
    ('1',),
    ('10010001100',),
    (' pgPeLz',),
    ('53212456821275',),
    ('101',),
    ('V',)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))