#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingSort function below.
def countingSort(arr):
    temp = [0] * 100
    result = []

    for x in arr:
        temp[x] += 1

    for i in range(100):
        if temp[i]:
            result.extend([i] * temp[i])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    temp = countingSort(arr)

    fptr.write(' '.join(map(str, temp)))
    fptr.write('\n')

    fptr.close()
