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
def f_gold ( a , b , c , x1 , y1 ) :
    temp = - 2 * ( a * x1 + b * y1 + c ) / ( a * a + b * b )
    x = temp * a + x1
    y = temp * b + y1
    return ( x , y )


def f_filled ( a , b , c , x1 , y1 , y2 ) :
    temp = ( - 2 * a + b * y1 + c ) / ( a * a + b * b )
    x = temp * a + x1
    y = temp * b + y1
    return ( x , y )


if __name__ == '__main__':
    param = [
    (3732.666168699511,6717.4319776458415,8487.605110792734,3122.488414306167,7288.495313569254,),
    (-6160.28797099689,-9526.951282445563,-2727.4586614461805,-7534.755781098465,-8258.639928049572,),
    (9707.663226287044,3545.24083205238,7876.511569086982,1470.811329180811,6452.68041640754,),
    (-6911.228913076611,-2028.0397959113661,-9156.730104961494,-9225.561292876928,-1370.1493253417884,),
    (2437.324652060757,6351.663596100777,9309.29692624503,9217.775327187837,124.92622868105929,),
    (-9772.988102067504,-7037.832078976599,-1106.0784469214657,-9822.961372946284,-9850.889686793544,),
    (962.3813406727966,2636.211531080329,3803.337776332597,8968.88804348246,768.6415184062179,),
    (-5295.715793735837,-1371.1549844447245,-4574.9652965175055,-5723.073256651608,-3979.742641311409,),
    (8277.666437028653,3894.6319227476024,1927.1038244370075,8277.958654483882,4293.94644558483,),
    (-8233.422168737996,-5956.055383069726,-5624.546627814419,-4024.7562734644903,-3480.155957748129,)
        ]
    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))