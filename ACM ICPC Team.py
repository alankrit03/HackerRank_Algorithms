#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the acmTeam function below.
def count_topic(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == '1' or s2[i] == '1':
            count += 1
    return count


def acmTeam(topic):
    max_topics = 0
    count = 0
    for i in range(len(topic)):
        for j in range(i + 1, len(topic)):
            topic_known = count_topic(topic[i], topic[j])
            # print(topic[i],topic[j],topic_known)
            if topic_known == max_topics:
                count += 1
            elif topic_known > max_topics:
                count = 1
                max_topics = topic_known

    return [max_topics, count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
