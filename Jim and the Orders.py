#!/bin/python3

import math
import os
import random
import re
import sys
def add(x):
    return x[0]+x[1]

def cook(x):
    return x[1]
# Complete the jimOrders function below.
def jimOrders(orders):
    orders=list(map(add,orders))
    orders=(list(enumerate(orders,1)))
    orders.sort(key=cook)
    result=[x[0] for x in orders]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
