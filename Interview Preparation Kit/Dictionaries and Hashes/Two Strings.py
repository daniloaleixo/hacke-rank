#!/bin/python3

# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

# twoStrings has the following parameter(s):

# s1, s2: two strings to analyze .
# Input Format

# The first line contains a single integer , the number of test cases.

# The following  pairs of lines are as follows:

# The first line contains string .
# The second line contains string .
# Constraints

#  and  consist of characters in the range ascii[a-z].
# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO
# Explanation

# We have  pairs to check:

# , . The substrings  and  are common to both strings.
# , .  and  share no common substrings.

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    keys_s1 = {}
    keys_s2 = {}
    
    i, j = 0, 0
    while(i < len(s1) and j < len(s2)):
        if i < len(s1):
            keys_s1[s1[i]] = True
            if s1[i] in keys_s2: return "YES"
            i += 1
            
        if j < len(s2):
            keys_s2[s2[j]] = True
            if s2[j] in keys_s1: return "YES"
            j += 1
    return "NO"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
