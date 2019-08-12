# Watson gives two integers ( and ) to Sherlock and asks if he can count the number of square integers between  and  (both inclusive).

# Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.

# Input Format

# The first line contains , the number of test cases.  test cases follow, each in a new line. 
# Each test case contains two space-separated integers denoting  and .

# Constraints

 

# Output Format

# For each test case, print the required answer in a new line.

# Sample Input

# 2
# 3 9
# 17 24
# Sample Output

# 2
# 0

import math

numbers = [i for i in range(0, 100000)]

t = int(raw_input().strip())

array_input = []

for i in range(0, t):
	array_input.append(map(int, raw_input().strip().split(' ')))



for i in range(0, t):
	result = 0

	sqrt_left = math.sqrt(array_input[i][0])
	sqrt_right = math.sqrt(array_input[i][1])

	left_boundary = int(sqrt_left) if sqrt_left == int(sqrt_left) else int(sqrt_left) + 1
	right_boundary = int(sqrt_right) + 1

	# print left_boundary, right_boundary
	# print 'numbers'
	# for i in range(left_boundary, right_boundary):
	# 	print numbers[i],  

	result = right_boundary - left_boundary
		
	print result




