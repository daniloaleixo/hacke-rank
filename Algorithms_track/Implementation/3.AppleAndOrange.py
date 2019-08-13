#!/bin/python3




# https://www.hackerrank.com/challenges/apple-and-orange/problem


import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
  relative_distance_apple = []
  relative_distance_orange = []

  for apple in apples:
    relative_distance_apple.append(a + apple)

  for orange in oranges:
    relative_distance_orange.append(b + orange)

  result_apple = 0
  result_orange = 0

  for apple in relative_distance_apple:
    if (apple >= s and apple <= t):
      result_apple = result_apple + 1
  
  for orange in relative_distance_orange:
    if (orange >= s and orange <= t):
      result_orange = result_orange + 1

  print(result_apple)
  print(result_orange)
  
  
  

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
