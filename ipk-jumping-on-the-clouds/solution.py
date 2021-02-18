#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    i, ret_value, length = 0, 0, len(c)

    while i < length :
        ##  (edge case handling) the end of list
        if i == length-1 : break

        ##  (edge case handling) the one before the end of list --> cannot jump, only can walk
        if i+1 == length-1 :
            ret_value += 1
            break

        ##  CAN JUMP
        if c[i+2] == 0 :
            ret_value += 1
            i += 2

        ##  CANNOT JUMP
        else :
            ret_value += 1
            i += 1

    return ret_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

