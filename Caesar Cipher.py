#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    lst=list(s)
    n=len(s)
    database_lower=string.ascii_lowercase
    database_upper=string.ascii_uppercase
    for i in range(n):
        if lst[i].isalpha():
            print(lst[i])
            if lst[i].islower():
                lst[i]=database_lower[(database_lower.index(lst[i])+k)%26]
            else:
                lst[i]=database_upper[(database_upper.index(lst[i])+k)%26]
    return ''.join(lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
