#!/bin/python

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    length = len( s )

    ##  (edge case handling) string only contains 'a'
    if length == 1 and s[0] == 'a' : return n

    ##  record the number of the existence of each char
    hash_table = {}
    for char in s :
        if char not in hash_table : hash_table[char] = 1
        else : hash_table[char] += 1

    ##  accumulating by multiplying the repeatence
    repeatCounter = n / length
    for key in hash_table : hash_table[key] *= repeatCounter

    ##  process the reamining character by MOD operation
    remain = n % length
    for i in range( remain ) : hash_table[s[i]] += 1

    ##  NOTE --> need to find the existence of 'a'
    if 'a' in hash_table : return hash_table['a']
    else : return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

