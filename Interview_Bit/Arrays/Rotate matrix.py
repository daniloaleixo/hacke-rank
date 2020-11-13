#!/bin/ptython

# https://www.interviewbit.com/problems/rotate-matrix/

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# You need to do this in place.

# Note that if you end up using an additional array, you will only receive partial score.

# Example:

# If the array is

# [
#     [1, 2],
#     [3, 4]
# ]
# Then the rotated array becomes:

# [
#     [3, 1],
#     [4, 2]
# ]



import math

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        if len(A) % 2 == 1:
            mid = len(A)/2.0
            #print('mid', mid, range(int(math.ceil(mid))))
            for i in range(int(math.ceil(mid))):
                self.solveRing(A, int(math.floor(mid - i)), int(math.ceil(mid + i - 1)))
        else:
            mid = int(len(A)/2)
            #print('mid', mid, range(int(mid)))
            for i in range(int(mid)):
                self.solveRing(A, mid - i - 1, mid + i)
        return A
        
    def solveRing(self, A, lower, higher):
        if lower != higher:
            save_num_prev, save_num = 0, 0
            size = higher - lower + 1
            
            for i in range(int(size) - 1):
                # First rot
                save_num = A[lower+i][higher]
                A[lower+i][higher] = A[lower][lower+i]
                save_num_prev = save_num
                #print(A, save_num_prev, save_num)
                # Second rot
                save_num = A[higher][higher-i]
                A[higher][higher-i] = save_num_prev
                save_num_prev = save_num
                #print(A, save_num_prev, save_num)
                # Third rot
                save_num = A[higher-i][lower]
                A[higher-i][lower] = save_num_prev
                save_num_prev = save_num
                #print(A, save_num_prev, save_num)
                # Last rot
                A[lower][lower+i] = save_num_prev
                #print(A, save_num_prev, save_num)
