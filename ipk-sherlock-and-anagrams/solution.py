#!/bin/python3

import math
import os
import random
import re
import sys

def findGroupAnagram(s):
    lenS = len(s)

    retHashTable = {}

    ##  (1) loop through each substring --> time complexity: O(n^2)
    for i in range( lenS ) :
        for j in range( i+1, lenS+1 ) :
            subString = s[i:j]

            ##  (2) find all groups of anagrams by sorting --> time complexity: O(nlog2n)
            sortedString = ''.join( sorted(subString) )

            if sortedString not in retHashTable : retHashTable[sortedString] = [subString]
            else : retHashTable[sortedString].append( subString )

    return retHashTable


def sherlockAndAnagrams(s):
    ##  (1) find groups of anagrams
    groupAnagram = findGroupAnagram(s)

    ##  (2) loop through each group and accumulate the number of occurrences
    ##  NOTE. if substring appears for n times, the total possible anagrams of that substring is 1+2+...+(n-1)
    retVal = 0
    for key, value in groupAnagram.items() :
        if len(value) > 1:
            print( value )
            retVal += sum( range( len(value) ) )

    print( retVal )
    return retVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

