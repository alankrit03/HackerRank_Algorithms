#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n=len(c)
    i=(0+k)%n
    if c[i]==1:
        e=97
    else:e=99
    while i:
        print('current_position',i)
        i=(i+k)%n
        if c[i]==1:
            e-=3
        else:e-=1
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
