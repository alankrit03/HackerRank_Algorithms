#!/bin/python3

import math
import os
import random
import re
import sys

def remove_sticks(arr):
    for i in range(len(arr)):
        if arr[0]==0:
            arr.pop(0)
        else:
            return arr
    return arr
# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result=[len(arr)]
    arr.sort()
    while arr:
        arr=[arr[i]-arr[0] for i in range(len(arr))]
        arr=remove_sticks(arr)
        result.append(len(arr))
    return result[:-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
