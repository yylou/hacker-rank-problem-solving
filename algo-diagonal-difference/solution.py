i#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ret_value = 0

    ##  example:
    #   00 01 02 03 04
    #   10 11 12 13 14
    #   20 21 22 23 24
    #   30 31 32 33 34
    #   40 41 42 43 44
    #
    #   row 0 : take element at '0' (00) and '-1 = -1*0 - 1' (04)
    #   row 1 : take element at '1' (11) and '-2 = -1*1 - 1' (13)
    #   row 2 : take element at '2' (22) and '-3 = -1*2 - 1' (22)
    #   row 3 : take element at '3' (33) and '-4 = -1*3 - 1' (31)
    #   row 4 : take element at '4' (44) and '-5 = -1*4 - 1' (40)

    for i in range( len(arr) ) :
        ret_value += arr[i][i]
        ret_value -= arr[i][-1*i - 1]

    return abs( ret_value )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

