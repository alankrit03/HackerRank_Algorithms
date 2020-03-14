#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    #special_characters = r""
    count=0
    if not re.search(r'\d',password):
        print('her digit')
        count+=1
    if not re.search(r'[!@#$%^&*()\-+]',password):
        print('her secia;')
        count+=1
    if not re.search(r'[a-z]',password):
        count+=1
        print('her lower')
    if not re.search(r'[A-Z]',password):
        count+=1
        print('her capit')
    s=n+count
    if s<6:
        return 6-s+count
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
