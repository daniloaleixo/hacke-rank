#!/usr/bin/python

# Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

# This challenge is also available in the following translations:

# Chinese
# Russian
# Input Format

# The first line contains a single string, . 
# The second line contains a single string, .

# Constraints

# It is guaranteed that  and  consist of lowercase English alphabetic letters (i.e.,  through ).
# Output Format

# Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

# Sample Input

# cde
# abc
# Sample Output

# 4

import math as math


def number_needed(a, b):
	a_array = [0] * 26
	b_array = [0] * 26

	for c in a:
		a_array[ord(c) - ord('a')] = a_array[ord(c) - ord('a')] + 1
	# print a_array
	for c in b:
		b_array[ord(c) - ord('a')] = b_array[ord(c) - ord('a')] + 1
	# print b_array
	count = 0
	for i in range(0, len(a_array)):
		count = count + math.fabs(a_array[i] - b_array[i])

	return int(count)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)