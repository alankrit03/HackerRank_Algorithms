#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    alice_rank = 1
    alice_iter = len(alice) - 1
    score_iter = 0
    current_max = scores[score_iter]
    score_len = len(scores)
    while score_iter < score_len:
        if alice_iter == -1:
            return alice

        if alice[alice_iter] >= scores[score_iter]:
            alice[alice_iter] = alice_rank
            alice_iter -= 1



        else:
            score_iter += 1
            if score_iter != score_len and scores[score_iter] < current_max:
                alice_rank += 1
                current_max = scores[score_iter]

    for i in range(alice_iter, -1, -1):
        alice[i] = alice_rank + 1
    # print('alice_iter',alice_iter)
    return alice


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
