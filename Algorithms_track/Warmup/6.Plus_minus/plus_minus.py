# Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Input Format

# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers describing an array of numbers .

# Output Format

# You must print the following  lines:

# A decimal representing of the fraction of positive numbers in the array.
# A decimal representing of the fraction of negative numbers in the array.
# A decimal representing of the fraction of zeroes in the array.
# Sample Input

# 6
# -4 3 -9 0 4 1         
# Sample Output

# 0.500000
# 0.333333
# 0.166667

def plus_minus():
	n = int(raw_input().strip())
	arr = map(int,raw_input().strip().split(' '))

	plus = 0
	minus = 0
	zeroes = 0

	for elem in arr:
		if(elem < 0):
			minus = minus + 1
		elif(elem > 0):
			plus = plus + 1
		else:
			zeroes = zeroes + 1

	print float(plus) / float(len(arr))
	print float(minus) / float(len(arr))
	print float(zeroes) / float(len(arr))


plus_minus()

