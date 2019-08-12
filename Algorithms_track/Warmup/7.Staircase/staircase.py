
# Consider a staircase of size n = 4:

#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

# Input Format

# A single integer, , denoting the size of the staircase.

# Output Format

# Print a staircase of size  using # symbols and spaces.

# Note: The last line must have  spaces in it.

# Sample Input

# 6 
# Sample Output

#      #
#     ##
#    ###
#   ####
#  #####
# ######

n = int(raw_input().strip())

for i in range(0, n):
	string = ''
	for j in range(0, n - 1 - i):
		string = string + ' '
	for j in range(n - 1 - i, n):
		string = string + '#'
	print string
