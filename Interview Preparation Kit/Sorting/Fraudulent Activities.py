#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    arr_sorted = counting_sort([expenditure[i] for i in range(d)], 201)
    
    for i in range(d, len(expenditure)):
        #print('>>> ', i + 1)
        start_index = i - d
        end_index = i - 1
        
        
        # Update sorted array
        if i > d:
            arr_sorted = remove(arr_sorted, expenditure[start_index - 1])
            #print('Removed', arr_sorted, expenditure[start_index - 1])
            arr_sorted = add(arr_sorted, expenditure[end_index])
            #print('Added', arr_sorted, expenditure[end_index])
        
        median = 0
        if d % 2 == 1:
            median = arr_sorted[int(d/2)]
        else:
            median = (arr_sorted[int(d/2)] + arr_sorted[math.ceil(d/2)]) / 2.0
        #print(start_index, end_index, median, arr_sorted, count)
        
        
        if expenditure[i] >= median * 2:
            count += 1
            
    return count

    
def add(array, k):
    index_to_add1, index_to_add2 = binary_search(array, 0, len(array) - 1, k)
    return array[:index_to_add1 + 1] + [k] + array[index_to_add2 + 1:]
    
def remove(array, k):
    index_to_remove, _ = binary_search(array, 0, len(array) - 1, k)
    return array[:index_to_remove] + array[index_to_remove + 1:]

def binary_search(arr, low, high, x): 
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid, mid
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return high, low
    
def counting_sort(arr, max_val):
    k = max_val + 1
    C = [0] * k
    B = [0] * len(arr)
    # Occurence couting
    for i in range(0, len(arr)): C[arr[i]] += 1
    #print(C)
    # Sum occurrence
    for i in range(0, k): C[i] = C[i] + C[i - 1]
    #print(C)
    
    # Array
    i = len(arr) - 1
    while(i >= 0):
        B[C[arr[i]] - 1] = arr[i]
        #print(B, C, arr[i], i)
        C[arr[i]] -= 1
        i -= 1
    return B
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
