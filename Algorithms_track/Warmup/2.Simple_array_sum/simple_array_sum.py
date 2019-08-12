# Given an array of  integers, can you find the sum of its elements?

# Input Format

# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers representing the array's elements.

# Output Format

# Print the sum of the array's elements as a single integer.

# Sample Input

# 6
# 1 2 3 4 10 11
# Sample Output

# 31


def array_sum():
	n = int(raw_input())
	array = map(int, raw_input().strip().split(' '))
	total = 0

	for num in array:
		total = total + num
	return total


print array_sum()
