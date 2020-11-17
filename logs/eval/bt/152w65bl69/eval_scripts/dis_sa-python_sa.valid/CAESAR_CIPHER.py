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
def f_gold ( text , s ) :
    result = ""
    for i in range ( len ( text ) ) :
        char = text [ i ]
        if ( char.isupper ( ) ) :
            result += chr ( ( ord ( char ) + s - 65 ) % 26 + 65 )
        else :
            result += chr ( ( ord ( char ) + s - 97 ) % 26 + 97 )
    return result


def f_filled ( text ) :
    """
 Return the text of the text to the text byte string.

 Args:
 text: the text to parse text to parse text.
 text: the text to parse text to parse text.
 text: the text to parse text to parse text.
 text: the text to parse text to parse text.
 """
    text = text.strip ( )
    if text is None :
        text = text.strip ( )
    return text


if __name__ == '__main__':
    param = [
    ('LsvbpcviVPwq',15,),
    ('35225904',2,),
    ('010010',36,),
    ('QnYd',44,),
    ('2571694',11,),
    ('101101011010',94,),
    ('jb',22,),
    ('928874',83,),
    ('11',93,),
    ('FbvbkMb',37,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))