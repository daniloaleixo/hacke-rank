#!/bin/python

# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

# We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

# Your task is to find their comparison points by comparing  with ,  with , and  with .

# If , then Alice is awarded  point.
# If , then Bob is awarded  point.
# If , then neither person receives a point.
# Comparison points is the total points a person earned.

# Given  and , can you compare the two challenges and print their respective comparison points?

# Input Format

# The first line contains  space-separated integers, , , and , describing the respective values in triplet . 
# The second line contains  space-separated integers, , , and , describing the respective values in triplet .

# Constraints

# Output Format

# Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

# Sample Input

# 5 6 7
# 3 6 10
# Sample Output

# 1 1 

def compare_triplets():
	a = map(int, raw_input().strip().split(' '))
	b = map(int, raw_input().strip().split(' '))

	a_points = 0
	b_points = 0

	for i in range(0, len(a)):
		if(a[i] > b[i]): 
			a_points = a_points + 1
		elif(a[i] < b[i]):
			b_points = b_points + 1

	return str(a_points) + ' ' + str(b_points)

print compare_triplets()
