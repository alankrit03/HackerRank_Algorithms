#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    total_changes=0
    n=len(s)
    for i in range(n//2):
        if s[i]==s[-1-i]:
            pass
        elif s[i]>s[-1-i]:
            total_changes+=ord(s[i])-ord(s[-1-i])
        else:
            total_changes+=ord(s[-1-i])-ord(s[i])
    return total_changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
