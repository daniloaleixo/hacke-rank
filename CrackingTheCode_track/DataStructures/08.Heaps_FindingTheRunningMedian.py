#!/usr/bin/python3

import sys

# 
# I have to use binary search to return the correct index in O(lg n)
def binary_search(array, target):
    lower = 0
    upper = len(array)
    x = 0
    while lower < upper:   # use < instead of <=
      x = lower + (upper - lower) // 2
      val = array[x]
      if target == val:
          return x
      elif target > val:
          if lower == x:   # this two are the actual lines
              break        # you're looking for
          lower = x
      elif target < val:
          upper = x
    return x

# I decided to make my own insert because I do not have to run the entire array 
# and I reduce the time to O(lg n) to this task
# which otherwise cost O(n lg n)  due to sorting
def insertItem(num, arr):
	if len(arr) == 0:
		arr.append(num)

	else:
		# Make a binary search
		i = binary_search(arr, num)

		# If its in the beginning
		if i == 0:
			if arr[0] <= num:
				aux = arr[0]
				arr[0] = num
				arr.insert(0, aux)
			else:
				arr.insert(0, num)
		else:
			arr.insert(i + 1, num)
	
	return arr

def getMedian(arr):
	if(len(arr)) == 0:
		return 0;
	elif(len(arr) % 2 == 0):
		return (arr[int(len(arr)/2)] + arr[int(len(arr)/2 - 1)]) / 2
	else:
		return arr[int(len(arr) / 2)]


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   insertItem(a_t, a)
   print("{0:0.1f}".format(getMedian(a)))
