#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hackerrankInString function below.
def hackerrankInString(s):
    pat = 'hackerrank'
    pos = 0
    for x in s.lower():

        if x == pat[pos]:
            pos += 1
        if pos == 10:
            return 'YES'

    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
