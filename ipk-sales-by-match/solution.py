#!/bin/python

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    ##  edge case handling
    if n == 0 or n == 1 : return 0

    hash_table = {}

    ##  record the number of the existence of each COLOR
    for element in ar :
        if element not in hash_table : hash_table[element] = 1
        else : hash_table[element] += 1

    ret_value = 0

    ##  accumulating by dividing the counter by 2
    for key, value in hash_table.items() : ret_value += value / 2

    return ret_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

