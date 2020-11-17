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
def f_gold ( array , m , n ) :
    counter = 0
    for i in range ( 0 , m ) :
        for j in range ( 0 , n ) :
            if ( array [ i ] [ j ] == 0 ) :
                counter = counter + 1
    return ( counter > ( ( m * n ) // 2 ) )


def f_filled ( 0x70x70x70eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

if __name__ == '__main__':
    param = [
    ([[79, 48, 59, 39, 33, 8, 8, 47, 45, 54, 35, 40, 70, 98, 70, 81, 48, 52, 74, 83, 67, 46, 14, 60, 47, 12], [95, 48, 3, 19, 14, 81, 2, 3, 72, 55, 5, 88, 98, 97, 75, 61, 42, 46, 49, 14, 20, 16, 9, 66, 21, 66], [98, 83, 30, 38, 55, 85, 23, 83, 32, 84, 5, 6, 76, 59, 12, 22, 33, 28, 36, 9, 2, 9, 18, 24, 65, 73], [58, 62, 97, 33, 65, 60, 11, 68, 52, 60, 54, 47, 82, 66, 16, 20, 75, 55, 38, 20, 24, 46, 11, 22, 1, 75], [3, 83, 28, 4, 72, 68, 64, 23, 94, 1, 3, 97, 46, 21, 47, 41, 23, 63, 1, 15, 24, 36, 71, 40, 87, 56], [87, 70, 71, 85, 10, 80, 33, 46, 87, 36, 16, 25, 15, 97, 13, 87, 87, 74, 37, 21, 37, 4, 99, 23, 31, 53], [37, 67, 88, 27, 27, 86, 32, 90, 65, 26, 93, 49, 91, 15, 13, 9, 96, 69, 56, 80, 87, 41, 91, 59, 46, 85], [65, 76, 25, 87, 63, 66, 39, 69, 8, 43, 67, 97, 94, 91, 99, 34, 71, 70, 95, 74, 88, 21, 42, 80, 16, 68], [48, 96, 30, 38, 71, 98, 72, 14, 43, 37, 38, 71, 37, 89, 51, 85, 27, 7, 20, 36, 96, 75, 76, 58, 50, 36], [77, 5, 4, 57, 52, 38, 62, 82, 49, 46, 36, 97, 70, 53, 83, 74, 74, 42, 72, 11, 88, 75, 11, 92, 40, 10], [72, 83, 15, 66, 57, 13, 85, 41, 9, 30, 67, 28, 1, 72, 92, 51, 76, 44, 52, 6, 74, 33, 31, 10, 71, 50], [42, 98, 1, 67, 51, 2, 18, 44, 14, 56, 4, 74, 34, 39, 50, 27, 48, 33, 67, 18, 12, 86, 32, 5, 90, 75], [90, 43, 82, 96, 38, 98, 79, 41, 78, 36, 3, 73, 74, 65, 74, 34, 85, 45, 77, 37, 89, 9, 86, 54, 10, 64], [53, 62, 86, 98, 61, 70, 18, 81, 57, 96, 65, 59, 12, 21, 96, 31, 16, 66, 13, 61, 31, 70, 43, 64, 84, 46], [53, 28, 98, 9, 34, 67, 46, 53, 57, 37, 85, 4, 29, 96, 59, 32, 45, 22, 52, 27, 66, 20, 57, 18, 97, 99], [32, 80, 33, 40, 8, 25, 13, 66, 26, 33, 30, 16, 37, 16, 93, 50, 58, 89, 87, 3, 26, 42, 56, 60, 81, 15], [46, 79, 18, 27, 8, 63, 81, 54, 19, 21, 3, 40, 86, 31, 18, 50, 11, 22, 80, 68, 60, 3, 82, 52, 30, 11], [48, 21, 33, 73, 88, 88, 15, 97, 46, 7, 33, 59, 91, 17, 80, 76, 58, 84, 10, 78, 93, 47, 3, 2, 17, 17], [67, 93, 87, 24, 28, 29, 20, 48, 26, 25, 25, 79, 47, 31, 10, 55, 48, 18, 59, 57, 89, 20, 14, 44, 34, 52], [87, 26, 22, 3, 40, 62, 64, 72, 52, 71, 11, 8, 79, 37, 28, 81, 21, 63, 90, 22, 74, 85, 26, 92, 57, 89], [80, 51, 54, 52, 35, 3, 13, 49, 36, 3, 12, 41, 91, 28, 29, 30, 40, 58, 73, 60, 95, 61, 52, 75, 91, 94], [90, 99, 20, 51, 37, 85, 46, 21, 62, 17, 16, 48, 61, 89, 79, 55, 5, 51, 88, 68, 38, 62, 42, 38, 16, 52], [95, 40, 54, 18, 67, 64, 52, 21, 52, 98, 84, 96, 48, 21, 34, 84, 18, 2, 47, 24, 78, 15, 10, 87, 88, 77], [89, 24, 15, 93, 26, 70, 3, 93, 64, 62, 85, 67, 6, 88, 66, 14, 19, 22, 33, 89, 91, 7, 1, 39, 37, 50], [40, 20, 50, 29, 3, 11, 66, 40, 11, 65, 13, 97, 87, 70, 1, 37, 25, 99, 81, 99, 95, 66, 88, 47, 54, 91], [36, 44, 14, 79, 81, 56, 56, 12, 7, 31, 74, 3, 18, 83, 27, 18, 75, 6, 46, 70, 69, 1, 95, 92, 12, 52]],25,16,),
    ([[67, 41, 95, 96, 46, 82, 5, 44, 41, 3, 55, 19, 1, 18, 59, 62, 56, 37, 60, 49, 5, 79, 68], [85, 12, 82, 41, 38, 52, 33, 75, 11, 46, 3, 21, 13, 93, 20, 42, 52, 95, 74, 69, 93, 1, 81], [95, 24, 13, 91, 41, 41, 85, 4, 98, 89, 97, 25, 13, 33, 18, 51, 54, 58, 24, 7, 33, 7, 65], [60, 17, 53, 18, 95, 76, 49, 84, 61, 35, 53, 48, 45, 88, 73, 51, 51, 8, 61, 97, 76, 15, 38], [30, 58, 80, 23, 72, 21, 10, 98, 40, 36, 54, 67, 79, 97, 94, 59, 86, 77, 93, 36, 77, 84, 5], [89, 42, 17, 26, 96, 26, 88, 89, 86, 21, 97, 39, 96, 57, 83, 24, 6, 85, 68, 12, 15, 92, 16], [45, 85, 17, 37, 50, 90, 60, 57, 3, 31, 32, 44, 66, 61, 32, 47, 2, 49, 38, 99, 21, 43, 95], [46, 50, 98, 39, 76, 81, 51, 16, 48, 63, 37, 54, 73, 30, 3, 41, 74, 61, 13, 4, 66, 92, 49], [25, 60, 8, 35, 12, 70, 77, 66, 35, 88, 40, 57, 38, 97, 31, 44, 6, 13, 3, 68, 28, 58, 72], [68, 78, 45, 66, 58, 8, 25, 90, 77, 1, 55, 60, 98, 54, 71, 60, 18, 86, 29, 48, 78, 75, 4], [56, 95, 41, 62, 43, 81, 32, 55, 95, 35, 61, 11, 34, 70, 27, 99, 59, 90, 27, 33, 71, 16, 35], [68, 16, 57, 90, 76, 38, 11, 75, 31, 81, 12, 62, 9, 3, 58, 51, 88, 25, 80, 72, 44, 14, 15], [99, 24, 44, 97, 54, 95, 80, 78, 12, 1, 86, 77, 27, 55, 54, 40, 65, 87, 6, 16, 14, 36, 87], [53, 8, 42, 68, 29, 57, 22, 34, 4, 87, 69, 56, 6, 81, 15, 83, 81, 31, 61, 7, 18, 2, 81], [26, 43, 12, 57, 23, 79, 80, 26, 70, 36, 33, 28, 27, 72, 97, 52, 13, 90, 45, 1, 44, 81, 38], [43, 82, 40, 76, 62, 67, 88, 72, 93, 2, 18, 87, 14, 1, 15, 88, 32, 39, 68, 31, 44, 54, 16], [99, 50, 21, 42, 96, 76, 40, 78, 48, 32, 66, 65, 10, 62, 39, 16, 41, 78, 59, 50, 50, 5, 83], [92, 92, 66, 22, 29, 40, 40, 16, 41, 61, 64, 13, 63, 76, 63, 10, 91, 12, 20, 88, 79, 54, 47], [61, 68, 76, 59, 98, 25, 18, 44, 3, 95, 61, 77, 12, 39, 79, 83, 92, 13, 75, 39, 6, 5, 65], [49, 12, 1, 19, 6, 19, 8, 86, 44, 61, 23, 88, 6, 52, 85, 67, 13, 74, 64, 46, 54, 96, 86], [2, 39, 65, 66, 43, 54, 6, 96, 27, 88, 90, 65, 26, 65, 23, 89, 26, 78, 76, 94, 37, 83, 3], [46, 32, 63, 18, 68, 16, 40, 27, 77, 56, 92, 52, 14, 6, 15, 3, 22, 48, 40, 51, 13, 95, 21], [28, 13, 95, 35, 18, 71, 3, 37, 46, 77, 61, 89, 52, 94, 46, 90, 59, 3, 19, 49, 79, 14, 49]],22,12,),
    ([[54, 80, 87, 13, 57, 54, 87, 86, 35, 80, 99, 77, 74, 67, 40, 17, 2, 58, 15, 68, 51, 81, 39, 80, 19, 51, 2, 90], [91, 30, 51, 84, 38, 71, 75, 65, 72, 14, 2, 93, 22, 1, 32, 18, 39, 41, 69, 18, 94, 21, 5, 12, 50, 10, 89, 85], [47, 9, 38, 92, 12, 34, 4, 35, 7, 80, 82, 20, 97, 74, 6, 41, 22, 60, 39, 84, 81, 73, 79, 73, 73, 36, 17, 6], [7, 58, 59, 11, 60, 12, 79, 26, 93, 56, 6, 87, 74, 91, 87, 6, 5, 35, 80, 73, 16, 81, 40, 92, 98, 30, 73, 39], [60, 35, 37, 72, 3, 55, 13, 47, 47, 87, 50, 33, 52, 15, 76, 10, 24, 24, 77, 62, 57, 66, 61, 28, 33, 40, 45, 65], [71, 80, 22, 56, 73, 49, 79, 4, 8, 73, 27, 16, 27, 35, 47, 36, 73, 19, 86, 37, 95, 73, 46, 57, 29, 19, 44, 9], [62, 34, 21, 35, 50, 13, 75, 34, 74, 12, 95, 30, 75, 30, 10, 48, 49, 8, 75, 31, 15, 95, 65, 86, 69, 4, 59, 46], [55, 27, 65, 56, 88, 34, 92, 9, 71, 38, 35, 64, 72, 19, 25, 82, 80, 77, 46, 33, 51, 55, 35, 74, 24, 76, 16, 14], [7, 7, 61, 69, 10, 36, 34, 91, 47, 37, 52, 23, 46, 16, 65, 85, 1, 85, 58, 61, 61, 15, 36, 62, 39, 88, 85, 35], [62, 81, 60, 3, 16, 7, 82, 42, 49, 99, 49, 10, 67, 87, 10, 33, 63, 71, 1, 33, 93, 98, 48, 58, 21, 26, 82, 47], [3, 5, 47, 13, 28, 79, 22, 51, 58, 41, 74, 52, 88, 43, 84, 70, 40, 24, 29, 83, 59, 23, 63, 58, 2, 32, 32, 81], [86, 20, 78, 78, 53, 93, 60, 99, 51, 87, 70, 30, 99, 16, 52, 14, 99, 21, 96, 48, 5, 86, 89, 48, 15, 79, 55, 57], [92, 16, 18, 8, 89, 97, 99, 62, 26, 58, 19, 25, 3, 87, 56, 45, 94, 76, 80, 23, 93, 56, 61, 63, 33, 5, 83, 91], [54, 92, 96, 19, 75, 7, 54, 70, 29, 40, 35, 11, 21, 41, 72, 65, 41, 60, 58, 58, 81, 11, 44, 32, 50, 71, 48, 58], [36, 34, 49, 92, 54, 31, 67, 69, 91, 4, 23, 34, 43, 5, 47, 66, 93, 20, 40, 19, 80, 57, 77, 24, 31, 21, 7, 20], [64, 55, 68, 71, 33, 93, 9, 44, 10, 50, 92, 24, 66, 88, 72, 92, 11, 55, 67, 33, 61, 29, 88, 76, 58, 14, 42, 34], [17, 23, 25, 42, 98, 72, 96, 14, 43, 38, 14, 96, 30, 93, 14, 86, 43, 17, 16, 57, 52, 22, 47, 63, 11, 76, 3, 39], [45, 3, 94, 41, 65, 72, 49, 18, 42, 81, 49, 8, 19, 8, 5, 47, 47, 71, 23, 13, 20, 62, 43, 44, 49, 61, 83, 97], [15, 97, 29, 80, 77, 46, 44, 71, 86, 75, 45, 76, 70, 44, 41, 68, 78, 76, 60, 13, 75, 37, 49, 34, 2, 94, 43, 86], [23, 12, 73, 12, 86, 62, 39, 61, 9, 26, 31, 73, 97, 48, 74, 10, 31, 55, 6, 39, 3, 80, 38, 48, 99, 35, 47, 93], [84, 75, 94, 3, 7, 20, 17, 77, 30, 36, 45, 68, 98, 73, 17, 29, 87, 69, 19, 38, 71, 86, 84, 36, 55, 51, 85, 44], [60, 12, 36, 49, 28, 96, 10, 20, 61, 87, 4, 68, 46, 19, 94, 49, 96, 96, 16, 69, 19, 51, 92, 59, 78, 2, 34, 40], [13, 54, 9, 18, 58, 3, 33, 77, 52, 93, 97, 12, 8, 71, 6, 69, 11, 71, 54, 6, 80, 64, 28, 82, 19, 98, 28, 46], [54, 68, 45, 43, 98, 63, 32, 70, 81, 32, 31, 39, 23, 32, 84, 87, 99, 91, 43, 97, 96, 42, 65, 98, 74, 5, 94, 88], [17, 29, 96, 93, 95, 20, 40, 37, 56, 74, 98, 15, 22, 83, 18, 75, 81, 99, 6, 27, 38, 29, 72, 57, 40, 26, 94, 49], [79, 96, 80, 43, 95, 44, 13, 62, 30, 10, 98, 65, 59, 46, 90, 56, 93, 38, 68, 40, 76, 19, 30, 20, 19, 80, 56, 5], [75, 90, 50, 89, 77, 6, 72, 68, 73, 94, 5, 21, 80, 36, 36, 88, 7, 49, 69, 16, 44, 78, 86, 59, 86, 49, 26, 33], [94, 79, 16, 65, 95, 4, 84, 59, 56, 78, 36, 5, 47, 40, 4, 17, 21, 17, 57, 27, 26, 35, 26, 1, 32, 13, 88, 72]],27,20,),
    ([[39, 82, 13, 38, 88, 30, 51, 34, 53, 58, 54, 87, 30, 72, 77, 48, 55, 34, 87], [70, 86, 28, 68, 52, 48, 78, 42, 68, 21, 27, 35, 41, 53, 76, 18, 39, 24, 61], [16, 38, 21, 46, 59, 52, 95, 97, 88, 90, 43, 83, 11, 25, 40, 18, 37, 47, 3], [53, 9, 6, 43, 54, 79, 86, 88, 68, 7, 79, 21, 70, 88, 77, 63, 90, 45, 64], [99, 16, 85, 5, 92, 38, 81, 26, 48, 18, 1, 43, 8, 59, 28, 47, 51, 31, 90], [4, 87, 14, 14, 97, 51, 81, 65, 25, 1, 22, 32, 46, 85, 90, 21, 85, 42, 44], [8, 96, 27, 63, 63, 65, 73, 66, 9, 54, 89, 93, 26, 72, 58, 71, 25, 67, 22], [76, 76, 64, 6, 24, 23, 29, 82, 7, 76, 93, 28, 54, 79, 47, 45, 53, 93, 24], [13, 30, 78, 6, 4, 21, 75, 30, 78, 42, 11, 19, 36, 4, 40, 35, 64, 19, 56], [61, 15, 99, 3, 59, 34, 15, 16, 3, 74, 70, 81, 11, 56, 24, 79, 31, 95, 30], [86, 49, 28, 58, 35, 14, 20, 83, 59, 88, 68, 16, 29, 74, 54, 64, 39, 89, 34], [79, 40, 23, 60, 79, 43, 88, 1, 21, 5, 51, 30, 20, 72, 63, 28, 56, 80, 2], [46, 70, 71, 17, 9, 12, 98, 70, 89, 72, 99, 25, 10, 9, 58, 67, 91, 97, 55], [84, 89, 11, 89, 91, 37, 34, 88, 35, 68, 92, 53, 90, 40, 12, 56, 16, 51, 32], [18, 89, 27, 59, 9, 86, 56, 35, 70, 5, 30, 5, 53, 42, 75, 63, 28, 14, 20], [21, 83, 86, 48, 24, 16, 5, 97, 65, 79, 51, 42, 2, 36, 2, 70, 64, 31, 19], [94, 81, 22, 39, 33, 76, 10, 41, 94, 25, 33, 15, 78, 17, 42, 53, 46, 69, 50], [45, 90, 30, 89, 62, 86, 37, 35, 8, 38, 64, 17, 6, 20, 92, 83, 84, 28, 41], [51, 97, 5, 17, 16, 93, 15, 74, 74, 98, 24, 25, 66, 71, 95, 44, 47, 39, 41]],11,9,),
    ([[45, 34, 40, 86, 92, 30, 11, 67, 66, 18, 30, 47, 69, 10, 98, 55, 85, 39, 46, 78], [49, 6, 79, 57, 39, 75, 91, 82, 91, 18, 86, 11, 46, 94, 96, 93, 31, 73, 98, 60], [40, 27, 52, 15, 85, 14, 9, 6, 47, 67, 46, 13, 29, 75, 53, 71, 80, 56, 88, 30], [36, 24, 45, 38, 71, 83, 10, 64, 26, 16, 31, 30, 33, 89, 69, 93, 59, 14, 19, 91], [23, 84, 17, 24, 58, 16, 79, 4, 84, 37, 91, 9, 15, 34, 52, 9, 24, 1, 81, 30], [34, 83, 45, 69, 25, 64, 16, 98, 87, 41, 68, 1, 17, 10, 81, 9, 87, 16, 48, 1], [26, 8, 59, 97, 5, 70, 41, 34, 95, 34, 92, 34, 76, 27, 83, 84, 90, 83, 39, 81], [58, 55, 22, 85, 45, 11, 27, 6, 71, 61, 97, 72, 78, 81, 93, 9, 21, 60, 96, 37], [2, 25, 36, 41, 31, 74, 4, 1, 70, 34, 45, 6, 19, 23, 5, 72, 48, 3, 66, 90], [37, 17, 39, 34, 86, 86, 49, 64, 89, 98, 23, 48, 76, 47, 34, 81, 77, 11, 67, 20], [6, 4, 27, 99, 14, 45, 92, 84, 63, 36, 50, 24, 98, 16, 81, 89, 94, 33, 13, 4], [51, 11, 25, 40, 65, 38, 4, 73, 67, 76, 81, 43, 87, 55, 28, 26, 49, 51, 97, 41], [10, 68, 99, 15, 59, 15, 1, 35, 8, 40, 58, 29, 36, 63, 51, 54, 41, 83, 92, 8], [26, 35, 58, 32, 90, 53, 11, 57, 43, 67, 9, 95, 98, 74, 29, 24, 8, 40, 83, 34], [46, 96, 63, 39, 20, 39, 69, 98, 23, 30, 29, 13, 24, 95, 72, 27, 18, 31, 78, 68], [15, 75, 63, 63, 95, 80, 19, 52, 10, 53, 88, 55, 94, 73, 85, 47, 85, 6, 80, 99], [67, 79, 6, 51, 9, 27, 54, 1, 69, 13, 39, 14, 64, 7, 85, 72, 90, 66, 87, 55], [55, 88, 18, 52, 43, 74, 81, 63, 6, 8, 62, 71, 28, 93, 4, 49, 75, 79, 66, 7], [34, 21, 47, 36, 76, 83, 10, 31, 91, 83, 12, 14, 43, 91, 51, 23, 45, 27, 66, 63], [96, 65, 87, 13, 87, 14, 33, 15, 79, 29, 14, 84, 77, 95, 47, 48, 44, 17, 78, 82]],14,14,),
    ([[42, 12, 11, 27, 59, 79, 58, 6, 82, 98, 65, 11, 95, 88, 36, 77, 61, 28, 50, 28, 70, 14, 95, 80, 20, 65, 34, 20, 88, 46, 82], [1, 96, 71, 86, 2, 9, 74, 20, 86, 87, 24, 96, 26, 21, 1, 69, 81, 31, 10, 37, 36, 39, 1, 27, 75, 69, 30, 36, 72, 28, 98], [18, 65, 21, 19, 89, 33, 81, 88, 43, 82, 73, 24, 95, 93, 47, 28, 17, 84, 14, 83, 26, 60, 11, 59, 10, 88, 15, 56, 70, 87, 6], [66, 16, 52, 35, 8, 58, 36, 40, 75, 53, 58, 99, 56, 22, 72, 14, 68, 44, 41, 64, 8, 50, 37, 36, 15, 19, 45, 15, 43, 53, 88], [73, 21, 71, 14, 86, 73, 13, 23, 69, 2, 31, 46, 92, 48, 21, 1, 90, 16, 38, 69, 86, 43, 49, 64, 6, 67, 78, 26, 55, 14, 57], [82, 84, 40, 95, 26, 69, 81, 37, 37, 83, 31, 49, 24, 25, 55, 95, 60, 16, 31, 51, 68, 54, 21, 67, 88, 72, 67, 88, 60, 43, 52], [44, 44, 36, 89, 17, 72, 6, 53, 12, 96, 46, 89, 63, 84, 33, 17, 61, 24, 53, 7, 51, 32, 98, 74, 86, 38, 31, 72, 95, 97, 81], [85, 45, 94, 87, 79, 71, 68, 12, 22, 58, 22, 85, 14, 7, 37, 88, 36, 92, 47, 34, 5, 72, 97, 54, 65, 46, 12, 66, 25, 46, 8], [58, 48, 97, 83, 67, 99, 28, 41, 80, 28, 94, 82, 76, 16, 59, 78, 65, 11, 28, 7, 95, 29, 58, 68, 14, 38, 47, 12, 69, 66, 18], [53, 14, 30, 70, 31, 44, 10, 1, 79, 76, 33, 79, 65, 54, 25, 96, 51, 80, 53, 66, 10, 42, 46, 57, 41, 39, 51, 13, 4, 28, 44], [54, 45, 31, 12, 11, 54, 5, 58, 36, 27, 84, 18, 78, 61, 49, 31, 31, 88, 10, 13, 19, 43, 28, 9, 34, 51, 17, 83, 15, 49, 62], [71, 83, 64, 18, 74, 48, 19, 52, 99, 50, 98, 49, 8, 73, 43, 85, 52, 19, 77, 83, 81, 43, 73, 63, 80, 45, 43, 80, 63, 6, 52], [47, 20, 16, 17, 59, 58, 56, 14, 39, 1, 66, 15, 76, 22, 23, 53, 97, 17, 76, 24, 66, 62, 46, 63, 87, 9, 31, 72, 14, 68, 50], [64, 94, 13, 2, 45, 48, 57, 13, 11, 31, 34, 7, 24, 90, 24, 66, 26, 61, 9, 15, 8, 28, 86, 76, 37, 4, 92, 35, 72, 93, 93], [58, 80, 95, 77, 7, 36, 55, 28, 37, 2, 85, 62, 43, 9, 46, 14, 29, 63, 16, 14, 40, 80, 94, 86, 32, 1, 45, 48, 43, 44, 47], [94, 14, 6, 63, 92, 78, 80, 77, 40, 19, 74, 67, 13, 14, 25, 74, 76, 76, 62, 25, 55, 23, 61, 98, 32, 39, 61, 86, 4, 47, 69], [20, 46, 96, 16, 79, 16, 86, 10, 30, 20, 25, 69, 74, 88, 15, 91, 74, 97, 2, 5, 13, 37, 92, 8, 99, 14, 46, 19, 19, 74, 67], [26, 34, 34, 85, 1, 51, 34, 55, 91, 6, 24, 45, 7, 94, 21, 77, 88, 14, 36, 59, 10, 26, 6, 33, 18, 40, 9, 13, 53, 42, 24], [46, 40, 59, 19, 6, 86, 68, 5, 55, 32, 75, 24, 8, 90, 1, 58, 83, 20, 23, 33, 5, 76, 13, 52, 87, 6, 35, 28, 2, 1, 94], [42, 82, 23, 86, 81, 20, 39, 5, 51, 50, 92, 87, 74, 50, 40, 87, 39, 9, 82, 71, 15, 81, 8, 99, 36, 16, 40, 8, 10, 74, 96], [5, 36, 89, 45, 15, 98, 24, 17, 30, 40, 27, 73, 31, 71, 56, 30, 92, 84, 18, 29, 22, 32, 41, 22, 54, 94, 87, 93, 78, 87, 75], [59, 94, 45, 80, 53, 46, 25, 43, 26, 66, 24, 35, 93, 77, 76, 88, 48, 63, 86, 59, 84, 12, 50, 91, 30, 51, 33, 95, 56, 91, 73], [90, 74, 86, 27, 96, 47, 7, 33, 42, 67, 94, 71, 10, 49, 19, 46, 49, 12, 91, 86, 43, 34, 87, 35, 71, 24, 10, 89, 6, 19, 48], [50, 66, 60, 59, 81, 36, 45, 77, 60, 2, 24, 89, 58, 34, 38, 90, 92, 63, 80, 85, 47, 1, 1, 35, 21, 11, 78, 39, 42, 65, 74], [1, 87, 40, 86, 74, 21, 38, 82, 16, 26, 8, 16, 44, 92, 83, 64, 79, 2, 75, 95, 40, 35, 57, 56, 55, 12, 59, 94, 94, 35, 94], [35, 64, 13, 52, 28, 88, 14, 55, 63, 81, 51, 1, 98, 97, 42, 13, 24, 33, 40, 85, 88, 4, 86, 63, 34, 82, 70, 42, 76, 57, 36], [82, 10, 12, 74, 92, 50, 4, 74, 42, 91, 76, 86, 97, 6, 92, 64, 83, 2, 64, 15, 59, 43, 24, 48, 95, 16, 36, 69, 21, 11, 88], [23, 19, 93, 9, 85, 70, 28, 44, 28, 79, 48, 78, 38, 24, 77, 41, 46, 73, 97, 50, 81, 7, 44, 66, 98, 7, 17, 99, 27, 98, 16], [98, 24, 28, 57, 76, 91, 95, 14, 27, 87, 68, 78, 75, 5, 61, 43, 86, 36, 1, 48, 11, 36, 92, 5, 4, 44, 32, 72, 18, 61, 82], [74, 52, 92, 80, 86, 94, 3, 63, 40, 42, 69, 93, 95, 57, 55, 88, 47, 23, 92, 24, 92, 16, 35, 73, 40, 76, 98, 25, 29, 18, 99], [54, 18, 49, 72, 31, 41, 51, 75, 72, 54, 76, 74, 42, 72, 63, 89, 4, 3, 19, 34, 63, 25, 93, 77, 45, 46, 5, 85, 30, 93, 18]],22,20,),
    ([[31, 83, 88, 14, 5, 89, 29, 61, 90, 20, 15, 11, 57, 68, 68, 11, 8, 72, 4, 96, 69, 42, 26, 96, 55, 42, 48, 89], [40, 32, 27, 51, 96, 95, 49, 46, 65, 66, 48, 71, 86, 96, 95, 51, 1, 50, 9, 65, 17, 35, 5, 63, 50, 53, 79, 46], [93, 89, 15, 91, 97, 99, 42, 74, 43, 90, 50, 41, 42, 41, 72, 51, 64, 28, 69, 81, 53, 64, 66, 44, 55, 72, 48, 79], [62, 71, 53, 27, 36, 9, 97, 5, 58, 99, 91, 90, 45, 50, 27, 67, 76, 83, 80, 58, 81, 46, 94, 56, 32, 46, 81, 10], [74, 60, 54, 4, 68, 71, 98, 4, 2, 96, 21, 48, 68, 21, 32, 82, 61, 63, 74, 27, 29, 15, 14, 38, 35, 87, 2, 62], [41, 71, 71, 83, 67, 39, 88, 38, 84, 65, 84, 84, 19, 11, 19, 75, 36, 98, 81, 19, 67, 3, 75, 41, 17, 29, 39, 86], [48, 58, 48, 48, 26, 84, 42, 94, 22, 89, 29, 59, 71, 53, 21, 30, 2, 17, 68, 42, 66, 97, 95, 64, 89, 52, 1, 62], [65, 64, 7, 14, 73, 61, 98, 8, 26, 55, 98, 72, 19, 22, 47, 61, 90, 86, 99, 82, 91, 18, 12, 45, 88, 77, 40, 53], [22, 19, 71, 37, 53, 90, 29, 28, 20, 14, 8, 98, 52, 59, 97, 22, 90, 83, 99, 94, 60, 75, 16, 83, 43, 53, 49, 88], [83, 71, 91, 80, 33, 91, 19, 23, 42, 21, 77, 80, 64, 67, 39, 12, 38, 87, 5, 1, 98, 52, 12, 73, 14, 48, 85, 68], [32, 34, 50, 56, 19, 81, 20, 17, 23, 32, 83, 56, 96, 87, 94, 88, 91, 21, 27, 10, 53, 57, 3, 80, 90, 72, 13, 25], [83, 78, 50, 75, 10, 50, 44, 86, 45, 27, 82, 63, 17, 99, 37, 99, 51, 27, 6, 20, 25, 15, 83, 53, 95, 14, 27, 36], [37, 59, 5, 5, 54, 95, 23, 26, 55, 77, 58, 63, 23, 88, 20, 83, 89, 11, 39, 80, 40, 75, 48, 26, 70, 93, 6, 6], [64, 69, 75, 19, 11, 23, 73, 83, 23, 53, 45, 10, 34, 6, 95, 52, 87, 20, 27, 90, 23, 83, 65, 21, 64, 48, 12, 38], [79, 9, 79, 55, 45, 30, 21, 52, 55, 31, 83, 17, 42, 68, 86, 55, 63, 49, 57, 16, 18, 5, 10, 96, 12, 52, 44, 51], [39, 29, 63, 29, 91, 23, 16, 41, 88, 1, 22, 43, 14, 43, 74, 84, 40, 53, 78, 85, 25, 88, 95, 18, 4, 69, 71, 69], [98, 52, 2, 83, 27, 24, 72, 22, 50, 24, 42, 39, 57, 89, 94, 90, 20, 63, 59, 71, 92, 64, 64, 9, 71, 95, 12, 42], [81, 10, 77, 3, 50, 2, 50, 52, 87, 83, 32, 80, 18, 15, 63, 16, 59, 44, 23, 14, 89, 14, 20, 93, 66, 22, 97, 36], [85, 87, 81, 24, 2, 41, 66, 56, 86, 31, 41, 79, 10, 49, 68, 18, 90, 50, 37, 18, 77, 48, 30, 77, 10, 41, 38, 90], [27, 4, 40, 48, 20, 70, 90, 81, 98, 41, 56, 2, 46, 57, 28, 21, 60, 60, 42, 89, 87, 90, 16, 58, 56, 76, 89, 36], [33, 9, 29, 18, 59, 89, 83, 54, 22, 11, 44, 9, 26, 91, 76, 36, 93, 73, 91, 89, 89, 1, 95, 61, 19, 65, 82, 57], [30, 78, 79, 87, 39, 53, 77, 49, 34, 1, 22, 74, 71, 77, 39, 25, 40, 91, 21, 69, 56, 40, 98, 65, 19, 60, 95, 43], [66, 4, 31, 83, 70, 97, 24, 72, 60, 73, 21, 47, 47, 19, 21, 6, 85, 61, 15, 93, 83, 45, 8, 29, 22, 34, 8, 51], [51, 96, 68, 8, 55, 48, 54, 62, 71, 29, 83, 95, 84, 5, 39, 96, 61, 87, 55, 47, 69, 93, 79, 1, 49, 75, 11, 34], [19, 60, 96, 25, 29, 36, 41, 92, 13, 28, 5, 58, 97, 76, 71, 89, 36, 89, 21, 32, 60, 31, 92, 53, 92, 1, 69, 22], [21, 47, 54, 12, 93, 11, 86, 4, 54, 25, 52, 84, 14, 86, 54, 19, 31, 38, 52, 24, 88, 16, 87, 45, 14, 97, 25, 81], [15, 92, 56, 70, 82, 14, 58, 46, 62, 61, 25, 16, 10, 35, 23, 18, 19, 8, 25, 80, 10, 18, 30, 63, 74, 56, 98, 20], [60, 17, 40, 74, 8, 64, 22, 37, 82, 10, 36, 27, 21, 30, 6, 78, 17, 60, 87, 42, 87, 9, 19, 33, 19, 20, 94, 18]],24,19,),
    ([[86, 39, 88, 64, 64, 37, 73, 80, 25, 79, 52, 51, 19, 48, 70, 73, 48, 63, 88, 16, 65, 48, 18, 28, 86, 68, 39, 5, 55, 72, 32, 80, 36, 99, 34], [48, 65, 65, 73, 63, 75, 55, 30, 69, 9, 72, 86, 91, 97, 40, 82, 5, 27, 81, 60, 14, 1, 26, 40, 66, 25, 90, 67, 99, 91, 72, 58, 90, 15, 32], [23, 80, 72, 57, 90, 2, 90, 95, 85, 57, 31, 8, 50, 43, 82, 6, 52, 75, 80, 62, 45, 2, 12, 63, 85, 70, 26, 16, 70, 81, 7, 32, 37, 94, 98], [15, 21, 54, 26, 33, 81, 87, 40, 92, 3, 85, 11, 78, 60, 22, 41, 52, 56, 59, 35, 32, 46, 52, 94, 7, 87, 37, 97, 93, 62, 28, 5, 49, 82, 22], [76, 57, 20, 20, 21, 61, 42, 5, 77, 98, 55, 66, 19, 93, 10, 63, 95, 65, 56, 79, 97, 53, 34, 6, 10, 40, 40, 31, 85, 64, 41, 69, 13, 87, 53], [6, 47, 51, 40, 50, 99, 74, 22, 81, 41, 4, 80, 4, 43, 91, 22, 21, 15, 63, 17, 34, 66, 39, 55, 36, 66, 97, 38, 55, 87, 18, 97, 31, 89, 65], [75, 45, 99, 54, 56, 42, 4, 40, 26, 96, 88, 36, 81, 33, 95, 53, 81, 39, 28, 25, 75, 8, 69, 40, 16, 30, 37, 78, 71, 31, 87, 42, 22, 36, 17], [40, 19, 21, 62, 43, 32, 10, 82, 99, 29, 95, 44, 95, 94, 16, 14, 1, 50, 32, 96, 88, 83, 15, 1, 84, 6, 45, 63, 14, 11, 83, 74, 76, 96, 53], [78, 42, 30, 64, 97, 13, 16, 42, 44, 61, 2, 67, 81, 11, 51, 80, 99, 2, 42, 54, 51, 51, 96, 3, 16, 49, 5, 44, 75, 56, 74, 48, 72, 43, 7], [30, 13, 90, 78, 1, 17, 42, 50, 87, 19, 86, 72, 78, 4, 86, 39, 8, 43, 49, 48, 19, 60, 27, 24, 74, 73, 13, 59, 32, 34, 55, 93, 24, 84, 56], [71, 81, 10, 4, 78, 71, 76, 75, 47, 17, 8, 27, 67, 21, 59, 79, 47, 26, 30, 40, 80, 44, 54, 37, 11, 9, 94, 73, 42, 82, 49, 19, 47, 75, 59], [59, 76, 5, 83, 49, 4, 17, 80, 90, 96, 52, 83, 24, 8, 81, 92, 32, 77, 76, 70, 34, 47, 63, 68, 15, 66, 20, 92, 55, 81, 77, 17, 8, 81, 73], [42, 41, 17, 73, 48, 41, 60, 14, 37, 36, 68, 95, 62, 2, 48, 41, 85, 76, 85, 91, 11, 4, 18, 24, 71, 25, 27, 57, 81, 80, 62, 4, 18, 72, 8], [38, 10, 4, 2, 15, 22, 30, 4, 70, 25, 43, 60, 74, 55, 1, 50, 1, 20, 99, 52, 27, 42, 12, 51, 10, 3, 91, 27, 69, 82, 98, 21, 70, 1, 36], [11, 38, 88, 76, 14, 36, 99, 12, 60, 88, 12, 30, 57, 95, 77, 4, 74, 43, 20, 3, 15, 30, 26, 91, 88, 21, 96, 31, 22, 65, 79, 32, 38, 97, 20], [91, 68, 2, 42, 32, 36, 69, 28, 59, 46, 34, 14, 94, 2, 13, 60, 38, 54, 14, 30, 2, 83, 99, 20, 65, 77, 61, 1, 27, 14, 15, 26, 38, 65, 4], [94, 68, 94, 65, 13, 26, 89, 89, 27, 10, 22, 34, 32, 84, 91, 6, 97, 95, 53, 88, 53, 77, 54, 35, 61, 52, 29, 25, 88, 35, 73, 83, 95, 13, 11], [12, 14, 83, 83, 42, 39, 88, 9, 99, 11, 13, 11, 78, 75, 96, 30, 3, 76, 68, 78, 15, 98, 46, 92, 71, 64, 45, 22, 71, 80, 4, 91, 60, 66, 22], [10, 29, 19, 7, 13, 42, 4, 98, 67, 72, 47, 42, 54, 72, 3, 6, 58, 55, 12, 96, 62, 46, 83, 78, 22, 16, 98, 36, 25, 92, 67, 32, 11, 15, 2], [39, 67, 9, 76, 60, 65, 51, 86, 92, 15, 34, 71, 79, 34, 76, 71, 69, 38, 88, 26, 17, 85, 91, 85, 6, 18, 96, 7, 6, 71, 95, 49, 98, 78, 5], [89, 10, 38, 46, 2, 86, 85, 95, 58, 25, 7, 14, 61, 61, 82, 75, 78, 32, 28, 84, 74, 64, 1, 2, 99, 54, 29, 8, 67, 29, 96, 95, 76, 83, 94], [16, 74, 25, 21, 88, 17, 42, 20, 7, 10, 85, 58, 88, 82, 14, 47, 87, 59, 23, 53, 34, 50, 51, 84, 32, 98, 50, 40, 25, 31, 74, 35, 58, 43, 89], [5, 35, 15, 66, 10, 31, 80, 97, 78, 68, 70, 1, 30, 19, 73, 2, 61, 77, 37, 72, 59, 3, 97, 99, 16, 68, 24, 35, 33, 60, 28, 17, 11, 27, 92], [39, 7, 84, 66, 13, 77, 85, 75, 47, 93, 22, 38, 11, 24, 13, 88, 42, 29, 14, 23, 68, 95, 41, 30, 43, 73, 91, 16, 37, 18, 14, 51, 46, 22, 39], [23, 80, 42, 44, 50, 99, 71, 76, 57, 68, 10, 39, 4, 25, 24, 53, 15, 31, 64, 84, 50, 87, 61, 3, 34, 82, 81, 4, 59, 35, 7, 46, 32, 20, 56], [81, 91, 69, 77, 25, 97, 84, 86, 33, 18, 24, 71, 98, 70, 66, 41, 36, 92, 65, 4, 12, 25, 19, 19, 49, 30, 20, 90, 30, 67, 11, 12, 5, 27, 54], [36, 75, 39, 62, 33, 96, 58, 29, 40, 24, 58, 25, 78, 3, 30, 99, 26, 82, 62, 77, 62, 81, 14, 34, 26, 29, 13, 34, 65, 21, 99, 61, 33, 24, 12], [23, 36, 37, 10, 68, 81, 51, 93, 63, 32, 8, 2, 58, 68, 39, 59, 54, 45, 31, 52, 95, 18, 61, 50, 4, 42, 2, 48, 84, 51, 62, 36, 1, 75, 16], [51, 30, 65, 41, 21, 92, 69, 37, 82, 90, 94, 83, 58, 69, 15, 70, 76, 53, 26, 33, 68, 21, 7, 29, 57, 75, 23, 49, 54, 14, 85, 93, 45, 3, 66], [11, 77, 15, 97, 25, 31, 51, 21, 51, 45, 28, 85, 69, 24, 81, 54, 14, 30, 37, 83, 59, 40, 15, 29, 49, 61, 90, 47, 81, 46, 86, 36, 50, 69, 87], [37, 31, 92, 34, 89, 71, 27, 44, 82, 49, 16, 10, 66, 50, 66, 83, 61, 7, 16, 13, 56, 84, 87, 71, 84, 25, 92, 2, 24, 53, 44, 14, 30, 58, 51], [44, 46, 26, 61, 98, 73, 52, 50, 29, 62, 67, 4, 16, 14, 96, 64, 58, 51, 62, 45, 90, 59, 59, 76, 17, 94, 65, 69, 7, 98, 36, 79, 6, 88, 79], [31, 74, 85, 47, 10, 66, 82, 98, 24, 16, 63, 86, 6, 15, 96, 33, 45, 6, 39, 8, 23, 83, 46, 11, 35, 26, 1, 41, 10, 11, 45, 65, 49, 49, 14], [38, 49, 34, 11, 77, 96, 90, 2, 3, 18, 14, 32, 14, 86, 13, 55, 66, 86, 28, 47, 88, 40, 8, 51, 28, 76, 95, 22, 9, 70, 99, 98, 71, 78, 25], [59, 83, 92, 82, 62, 79, 88, 91, 65, 45, 82, 96, 99, 72, 63, 35, 89, 96, 93, 83, 11, 89, 33, 3, 54, 62, 71, 65, 67, 71, 69, 30, 79, 6, 16]],20,22,),
    ([[93, 31, 15, 23, 44, 84, 3, 83, 86, 47, 93], [79, 70, 36, 92, 40, 24, 18, 39, 41, 97, 9], [11, 36, 96, 6, 22, 15, 34, 56, 34, 68, 34], [52, 69, 93, 9, 63, 72, 7, 78, 84, 87, 16], [53, 5, 78, 45, 85, 29, 33, 32, 34, 93, 78], [41, 43, 9, 62, 60, 66, 82, 69, 35, 97, 64], [34, 33, 87, 61, 11, 92, 47, 56, 60, 85, 3], [32, 44, 45, 55, 46, 6, 67, 16, 12, 34, 11], [24, 47, 38, 60, 54, 10, 71, 86, 75, 86, 4], [80, 33, 53, 67, 42, 69, 3, 87, 73, 15, 96], [22, 38, 56, 60, 17, 44, 73, 96, 75, 3, 27]],10,8,),
    ([[65]],0,0,)
        ]

    for i, p_set in enumerate(param):
        param[i] = list(param[i])
        if i % 2 == 0:
            param[i][0] = [[0 if e % 2 == 0 or e % 3 == 0 else e for e in l] for l in p_set[0]]

    n_success = 0
    for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))