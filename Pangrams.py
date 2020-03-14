#!/bin/python3

import math
import os
import random
import re
import sys
import string


# Complete the pangrams function below.
def pangrams(s):
    check = string.ascii_lowercase
    for x in check:
        if x not in s.lower():
            # print(x)
            return 'not pangram'
    else:
        return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
