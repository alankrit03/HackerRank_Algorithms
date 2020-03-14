#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    if len(arr)==1:
        return 'YES'
    all_sum=sum(arr)
    upto_sum=0
    for x in arr:
        if 2*upto_sum == all_sum-x:
            return 'YES'
        else:
            upto_sum+=x
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
