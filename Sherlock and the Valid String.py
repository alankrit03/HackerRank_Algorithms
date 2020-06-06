#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    n = len(s)
    print(n)
    c = Counter(s)
    num_of_letters = len(c)
    counter_of_values = Counter(c.values())
    print(counter_of_values)

    print(num_of_letters * counter_of_values.most_common(1)[0][0])
    if len(counter_of_values) > 2:
        return 'NO'
    elif len(counter_of_values) == 1:
        return 'YES'

    else:
        temp = counter_of_values.most_common(2)
        if (temp[0][1] == 1 or temp[1][1] == 1) and abs(temp[0][0] - temp[1][0]) == 1:
            return 'YES'
        elif (temp[0][1] == 1 and temp[0][0] == 1) or (temp[1][1] == 1 and temp[1][0] == 1):
            return 'YES'

        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
