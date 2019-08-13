#!/bin/python3

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.


def breakingRecords(scores):
    minimum = 999999999
    maximum = -1
    count_min_breaks = -1
    count_max_breaks = -1

    for sc in scores:
        if(sc < minimum):
            minimum = sc
            count_min_breaks = count_min_breaks + 1
        if(sc > maximum):
            maximum = sc
            count_max_breaks = count_max_breaks + 1

    if (count_min_breaks < 0):
        count_min_breaks = 0
    if (count_max_breaks < 0):
        count_max_breaks = 0
    return [count_max_breaks, count_min_breaks]


if __name__ == '__main__':
        # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
