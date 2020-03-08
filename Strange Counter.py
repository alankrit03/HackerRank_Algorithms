#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the strangeCounter function below.
def strangeCounter(t):
    if t == 1:
        return 3
    elif t == 2:
        return 2
    elif t == 3:
        return 1

    time = 3
    counter = 3

    while (time < t):
        counter *= 2
        time += counter

    temp = time - t + 1

    # print('time ', time)
    # print('counter ', counter)

    return temp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
