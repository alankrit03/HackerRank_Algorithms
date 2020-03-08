#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def first_root(a,b):
    while a<=b:
        root=a**0.5
        if root==int(root):
            return a,int(root)
        else: a+=1
    return 0,0

def squares(a, b):
    square,root=first_root(a,b)
    print(square,root)
    if root:
        count=0
    else:return 0
    while square<=b:
        count+=1
        square+=(2*root)+1
        root+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
