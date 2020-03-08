#!/bin/python3

import math
import os
import random
import re
import sys

def count_a(s):
    count=0
    for i in range(len(s)):
        if s[i]=='a':
            count+=1
    return count
# Complete the repeatedString function below.
def repeatedString(s, n):
    a_in_s=count_a(s)
    n_left=n%len(s)
    return a_in_s*(n//len(s))+count_a(s[:n_left])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
