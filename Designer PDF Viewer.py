#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    import string
    s = string.ascii_lowercase
    # print (s)
    word_given = []
    count = 0
    for ch in word:
        word_given.append(h[s.index(ch)])
        count += 1

    return count * max(word_given)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
