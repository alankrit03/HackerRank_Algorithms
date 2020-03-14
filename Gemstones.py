#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gemstones function below.
def gemstones(arr):
    gem_stone_set = set(arr[0])
    for x in arr:
        # print(gem_stone_set,'\n',x)
        gem_stone_set.intersection_update(set(x))

    return len(gem_stone_set)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
