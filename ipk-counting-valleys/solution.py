#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    ##  edge case handling
    if steps == 1 : return 0

    counterU = 0
    flag_location = 0

    ret_value = 0

    for element in path :
        ##  record the current location
        if element == 'U' : counterU += 1
        else : counterU -= 1

        ##  walk out of the valley --> using previous location flag and current location
        if flag_location == -1 and counterU == 0 : ret_value += 1

        ##  flag the current location --> POSIVITE = on mountain; NEGATIVE = in valley; ZERO = at sea level
        if counterU > 0 : flag_location = 1
        elif counterU < 0 : flag_location = -1
        else : flag_location = 0

    return ret_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(raw_input().strip())

    path = raw_input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

