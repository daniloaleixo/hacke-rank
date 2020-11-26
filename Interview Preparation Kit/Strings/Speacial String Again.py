#!/bin/python3

# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

# For example, given the string , we have the following special substrings: .

# Function Description

# Complete the substrCount function in the editor below. It should return an integer representing the number of special substrings that can be formed from the given string.

# substrCount has the following parameter(s):

# n: an integer, the length of string s
# s: a string
# Input Format

# The first line contains an integer, , the length of .
# The second line contains the string .

# Constraints


# Each character of the string is a lowercase alphabet, .

# Output Format

# Print a single line containing the count of total special substrings.

# Sample Input 0

# 5
# asasd
# Sample Output 0

# 7 
# Explanation 0

# The special palindromic substrings of  are 

# Sample Input 1

# 7
# abcbaba
# Sample Output 1

# 10 
# Explanation 1

# The special palindromic substrings of  are 

# Sample Input 2

# 4
# aaaa
# Sample Output 2

# 10
# Explanation 2

# The special palindromic substrings of  are 

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    
    for i in range(n - 1):
        
        # Check same chars
        j = i + 1
        while (j < n and s[i] == s[j]):
            #print('same', s[i], s[j], i, j)
            count += 1
            j += 1
            
        j = i - 1
        k = i + 1
        c = s[k] if k < n else s[j] if j >= 0 else None 
        while (c and j >= 0 and k < n and s[j] == c and s[k] == c and s[i] != c):
            #print('palin', s[j], s[k], j, k)
            count += 1
            j -= 1
            k += 1
    return count
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
