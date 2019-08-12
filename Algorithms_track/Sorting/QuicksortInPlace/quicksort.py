# The previous version of Quicksort was easy to understand, but it was not optimal. It required copying the numbers into other arrays, which takes up space and time. To make things faster, one can create an "in-place" version of Quicksort, where the numbers are all sorted within the array itself.

# Challenge 
# Create an in-place version of Quicksort. You need to follow Lomuto Partitioning method.

# Guideline 
# Instead of copying the array into multiple sub-arrays, use indices to keep track of the different sub-arrays. You can pass the indices to a modified partition method. The partition method should partition the sub-array and then return the index location where the pivot gets placed, so you can then call partition on each side of the pivot.

# Always select the last element in the 'sub-array' as a pivot.
# Partition the left side and then the right side of the sub-array.
# Print out the whole array at the end of every partitioning method.
# An array of length  or less will be considered sorted, and there is no need to sort or to print them.
# Since you cannot just create new sub-arrays for the elements, partition method will need to use another trick to keep track of which elements are greater and which are lower than the pivot.

# The In-place Trick

# If an element is lower than the pivot, you should swap it with a larger element on the left-side of the sub-array.
# Greater elements should remain where they are.
# At the end of the partitioning method, the pivot should be swapped with the first element of the right partition, consisting of all larger elements, of the sub-array.
# To ensure that you don't swap a small element with another small element, use an index to keep track of the small elements that have already been swapped into their "place".
# Lomuto-partitioning

# Input Format 
# There will be two lines of input:

#  - the size of the array
#  - the  numbers of the array
# Output Format 
# Print the entire array on a new line at the end of every partitioning method.

# Constraints 
 
 
# There are no duplicate numbers.

# Sample Input

# 7
# 1 3 9 8 2 7 5
# Sample Output

# 1 3 2 5 9 7 8
# 1 2 3 5 9 7 8
# 1 2 3 5 7 8 9


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

def separa(start, end):
	pivot = arr[end]
	i = start
	j = end - 1
	t = 0
	swaps = 0
	while i < j:
		if arr[i] <= pivot:
			i = i + 1
		elif arr[j] > pivot:
			j = j - 1
		else:
			t = arr[i]
			arr[i] = arr[j]
			arr[j] = t
			i = i + 1
			j = j - 1
			swaps = 1
	# print i
	if arr[i] > pivot:
		arr[end] = arr[i]
		arr[i] = pivot
		swaps = 1
	if swaps:
		for elem in arr: print elem, 
		print '\n',
	return i

def quicksort(p, r):
	# print 'quicksort ','p', p, 'r', r
	if p < r:
		i = separa(p, r)
		# print i
		quicksort(p, i)
		quicksort(i + 1, r)



quicksort(0, len(arr) - 1)



# separa(0, len(arr) - 1)
