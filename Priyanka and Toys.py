#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    container=1
    min_weight=w[0]
    for x in w:
        if x>min_weight+4:
            min_weight=x
            container+=1
    return container


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
