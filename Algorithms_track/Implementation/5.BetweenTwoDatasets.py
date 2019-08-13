#!/bin/python3

# https://www.hackerrank.com/challenges/between-two-sets/problem

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
  min_of_multiples = min(b)
  look_for_all_those = []
  for el in a:
    for i in range(el, min_of_multiples + 1, el):
      look_for_all_those.append(i)

  look_for_all_those = list(dict.fromkeys(look_for_all_those))

  count = 0

  for el in look_for_all_those:
    # print(el)
    jump = False

    if (not jump):
      for ai in a:
        if (el % ai != 0 or el < ai):
          jump = True
          break

    if (not jump):
      for bi in b:
        if (bi % el != 0 or el > bi):
          jump = True
          break
    if (not jump):
      count = count + 1
      # print("Entra", el)
      
  return count


  


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    # fptr.write(str(total) + '\n')

    # fptr.close()
