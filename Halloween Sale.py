#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total_games=0
    while p>m and s>0:
        print(s>0)
        s=s-p
        total_games+=1
        p=p-d
    total_games+=s//m
    print('p={} s={} total_games={}'.format(p,s,total_games))
    if total_games<0:
        return 0
    return total_games

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
