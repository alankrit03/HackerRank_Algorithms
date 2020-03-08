#!/bin/python3

import math
import os
import random
import re
import sys


def get_config(n):
    root = (n ** 0.5)
    lower = int(root)
    if lower == root:
        return lower, lower
    elif lower * (lower + 1) >= n:
        return lower, lower + 1
    else:
        return lower + 1, lower + 1


def chunks(s, row):
    for i in range(0, len(s), row):
        yield s[i:i + row]


# Complete the encryption function below.
def encryption(s):
    s = re.sub(r' ', '', s)
    n = len(s)
    row, col = get_config(n)
    # print(row,col) used to check the config returned from the func
    result = []

    for chunk in chunks(s, col):
        result.append(chunk)

    final = []
    for i in range(col):
        temp = ''
        for x in result:
            if len(x) > i:
                temp += x[i]
        final.append(temp)

    return ' '.join(final)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
