#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    t=list(reversed(s))
    s_diff=[]
    t_diff=[]
    n=len(s)
    for i in range(n-1):
        s_diff.append(abs(ord(s[i])-ord(s[i+1])))
        t_diff.append(abs(ord(t[i])-ord(t[i+1])))
    if s_diff==t_diff:
        return 'Funny'
    else:return 'Not Funny'




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
