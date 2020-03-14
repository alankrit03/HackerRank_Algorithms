#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    result=[arr[0],arr[1]]
    diff=abs(arr[0]-arr[1])
    for i in range(1,len(arr)-1):
        if diff==abs(arr[i]-arr[i+1]):
            result.extend([arr[i],arr[i+1]])
        elif diff>abs(arr[i]-arr[i+1]):
            result=[arr[i],arr[i+1]]
            diff=abs(arr[i]-arr[i+1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
