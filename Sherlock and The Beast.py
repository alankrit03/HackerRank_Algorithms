#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the decentNumber function below.
def decentNumber(n):
    if n < 3 or n == 4 or n == 7:
        print(-1)
    elif n % 3 == 0:
        print('5' * n)
    else:
        if (n - 5) % 3 == 0:
            print('5' * (n - 5) + '33333')
        else:
            print('5' * (n - 10) + '3' * 10)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
