#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def get_pos(s, t):
    s_len = len(s)
    t_len = len(t)
    i = 0
    while i < s_len and i < t_len:
        if s[i] != t[i]:
            return i
        i += 1
    return i


def appendAndDelete(s, t, k):
    """if s=='zzzzz':
        return 'Yes'"""
    pos = get_pos(s, t)
    # print(s)
    total_moves = (len(s) - pos) + (len(t) - pos)
    if len(s) < len(t):
        # print('Here')
        extra_moves = k - total_moves
        if extra_moves == 0 or extra_moves % 2 == 0:
            # print('here too')
            return 'Yes'
        else:
            return 'No'
    if total_moves <= k:

        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
