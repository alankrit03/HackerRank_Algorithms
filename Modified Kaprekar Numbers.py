#!/bin/python3

import math
import os
import random
import re
import sys

def isKaprekar(num):
    square=str(int(num**2))
    d=len(str(num))
    if num==(int(square[-d:])+int(square[:-d])):
        return True
    else:
        return False


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    count=0
    for i in range(p,q+1):
        if i==1:
            print('1',end=' ')
        if i<4:
            continue
        if isKaprekar(i):
            print(i,end=' ')
            count+=1
    if count==0:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
