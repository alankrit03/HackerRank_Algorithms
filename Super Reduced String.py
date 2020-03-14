#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    change = 1
    new_s = s
    while (change == 1):
        new_s, change = reduce_string(new_s)
        # print(change)
        """while(i<len(s)):
        if s[i]==s[i+1]:
            i=i+2
        else:
            new_str+=s[i]
            change=1
        print(new_s)"""

    if (new_s == ''):
        return 'Empty String'
    else:
        return new_s


def reduce_string(s):
    change = 0
    new_str = ''
    # print(s)
    i = 0
    while (i < len(s) - 1):
        if s[i] == s[i + 1]:
            i = i + 2
            change = 1
        else:
            new_str += s[i]
            i = i + 1
    if (i == len(s) - 1):
        new_str += s[i]
    if (change == 1):
        return new_str, 1
    else:
        return s, 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
