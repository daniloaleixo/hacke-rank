# Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

# Input Format

# The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

# Output Format

# Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output

# 15
# Explanation

# The primary diagonal is: 
# 11
#       5
#             -12

# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:
#             4
#       5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19 
# Difference: |4 - 19| = 15

import math

def diagonal_diff():

	n = int(raw_input().strip())
	a = []
	for a_i in xrange(n):
	    a_temp = map(int,raw_input().strip().split(' '))
	    a.append(a_temp)

	diagonals = [0,0]

	# first diagonal
	for i in range(0, n):
		diagonals[0] = diagonals[0] + a[i][i]
		diagonals[1] = diagonals[1] + a[n-1-i][i]

	return int(math.fabs(diagonals[0] - diagonals[1]))


print diagonal_diff()