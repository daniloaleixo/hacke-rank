# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Input Format

# A single line of five space-separated integers.

# Constraints

# Each integer is in the inclusive range .
# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14



def minimax():

	array_str = raw_input().strip().split(' ')
	array = map(long, array_str)

	minimum = min(array)
	maximum = max(array)

	index_max_cut_off = array.index(minimum)
	index_min_cut_off = array.index(maximum)

	sum_mim, sum_max = 0, 0

	for i in range(0, len(array)):
		if(i != index_min_cut_off):
			sum_mim = sum_mim + array[i]
		if(i != index_max_cut_off):
			sum_max = sum_max + array[i]


	print sum_mim, sum_max

minimax()