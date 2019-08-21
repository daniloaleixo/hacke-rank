#!/bin/python3


# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


import math
import os
import random
import re
import sys

# Complete the isValid function below.


def isValid(s):
    hash_s = {}
    for c in s:
        if (c in hash_s):
            hash_s[c] = hash_s[c] + 1
        else:
            hash_s[c] = 1

    print(hash_s)

    # Count the numbers
    numbers_hash = {}
    for c in hash_s:
        el = hash_s[c]
        if (el in numbers_hash):
            numbers_hash[el] = numbers_hash[el] + 1
        else:
            numbers_hash[el] = 1

    print(numbers_hash)

    if (len(numbers_hash) > 2):
        return "NO"
    elif (len(numbers_hash) <= 1):
        return "YES"
    else:
        list_numbers = []
        freq = []
        for number in numbers_hash:
            list_numbers.append(numbers_hash[number])
            freq.append(number)

        print(list_numbers)
        if ((list_numbers[0] == 1 and freq[0] <= 2) or list_numbers[1] == 1):
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
