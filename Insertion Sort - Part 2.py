#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(2,n+1):
        insertionSort1(i,arr)



def insertionSort1(n, arr):
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        #print(i)
        if arr[i]>temp:
            arr[i+1]=arr[i]
        else:
            arr[i+1]=temp
            print(*arr,sep=' ')
            break
        #print(*arr,sep=' ')
    else:
        arr[0]=temp
        print(*arr,sep=' ')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
