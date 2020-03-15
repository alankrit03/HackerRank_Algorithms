#!/bin/python3

import math
import os
import random
import re
import sys

def important(x):
    return x[1],x[0]
# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=important,reverse=True)
    print(contests)
    luck=0
    for x in contests:
        if not x[1]:
            luck+=x[0]
        else:
            if k:
                luck+=x[0]
                k-=1
            else:
                luck-=x[0]
    return luck

    return 8
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
