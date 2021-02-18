#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    nHour = int( s[:2] )
    sRemainTime = s[2:-2]
    sFormat = s[-2:]

    if   sFormat == 'AM' and nHour >= 12 : nHour -= 12
    elif sFormat == 'PM' and nHour <  12 : nHour += 12

    ##  NOTE --> remember to add '0' if the number is smaller than 10
    if nHour < 10 : sHour = '0' + str(nHour)
    else : sHour = str(nHour)

    return sHour + sRemainTime


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

