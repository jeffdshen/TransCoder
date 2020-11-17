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
def f_gold ( x1 , y1 , x2 , y2 ) :
    return ( float ) ( y2 - y1 ) / ( x2 - x1 )


def f_filled ( x1 , y1 , z1 , x2 , y2 ) :
    return float ( x1 - y1 ) / ( x2 - y2 )


if __name__ == '__main__':
    param = [
    (236.27324548309292,5792.493225762838,7177.837879115863,1289.5700425822731,),
    (-9201.144918204123,-2716.3347716140406,-5161.142121227645,-3205.784279961129,),
    (3480.4716834445326,3577.9608612055613,8611.515262945342,6744.864707668983,),
    (-6915.538971485092,-4113.601103381095,-748.3462104020822,-9245.271700539257,),
    (8887.97173657486,1678.4080012662428,8709.574949883017,8548.492675510739,),
    (-3785.5177159369946,-3084.67461899163,-7415.76208254121,-887.5389305564152,),
    (3037.6696554256832,4432.445827549,8387.304165588026,611.3373507518394,),
    (-7925.458496016523,-3350.27411882042,-5619.767086756504,-1185.7423219907591,),
    (1404.2919985268031,8971.636233373416,3039.112051378511,1947.6756252708972,),
    (-4748.744241168378,-675.557388148954,-5998.241086029875,-4236.658178504375,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if abs(1 - (0.0000001 + abs(f_gold(*parameters_set))) / (abs(f_filled(*parameters_set)) + 0.0000001)) < 0.001:
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))