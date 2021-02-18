#!/bin/python

import math
import os
import random
import re
import sys

def reverseArray(a):
    ##  two pointers solution --> one from the start; the other one from the end
    left, right = 0, len(a)-1

    while right > left :
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1

    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

