#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
from collections import Counter
def migratoryBirds(arr):
    arr.sort()
    c=Counter(arr)
    d=c.most_common(1)
    return d[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
