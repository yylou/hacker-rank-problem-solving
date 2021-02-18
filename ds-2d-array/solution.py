#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    ret_value = float('-inf')

    ## input format
    # [ [-9  -9  -9  1  1  1],
    #   [ 0  -9   0  4  3  2],
    #   [-9  -9  -9  1  2  3],
    #   [ 0   0   8  6  6  0],
    #   [ 0   0   0 -2  0  0],
    #   [ 0   0   1  2  4  0]
    # ]

    for i in range( 4 ) :
        for j in range( 4 ) :
            tmpVal = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if tmpVal > ret_value : ret_value = tmpVal

    return ret_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

