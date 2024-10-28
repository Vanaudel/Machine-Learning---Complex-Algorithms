#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np



def get_k_nearest_DC(A, target, k):
    
    
    #Use a slightly altered Binary Search to find the earliest index where Ai > target
    #Accomplish this using Divide and Conquer
    #This is from the course's/prof's code
    def binary_search_val_DC(A, target):
        size = len(A)
        idx0 = 0
        idxn = size-1

        # find the middle most value
        while idx0 <= idxn:
            midval = (idx0 + idxn)//2

            #Target found in the middle of list
            if A[midval] == target:
                return midval

            # compare the value to middle most value
            if target > A[midval]:
                idx0 = midval+1
            elif target < A[midval]:
                idxn = midval-1
            else:
                return midval
        return idx0

    target = int(target)
    k = int(k)

    #Find the earliest index where Ai > target using DC
    target_vicinity_index = binary_search_val_DC(A, target)
    n = len(A)
    all_KNNs = [0] * n

    
    remaining_k = k    
    #The first value added is the value at the vicinity index
    all_KNNs[target_vicinity_index] = A[target_vicinity_index]
    remaining_k = remaining_k - 1
    
    
    #Find the remaining k-1 KNNs by checking both left and right values further away from the vicinity index
    left_index = target_vicinity_index - 1
    right_index = target_vicinity_index + 1
    while remaining_k != 0:
        
        if left_index >= 0 and right_index > n:
            all_KNNs[left_index] = A[left_index]
            left_index = left_index - 1
        elif left_index < 0 and right_index <= n:
            all_KNNs[right_index] = A[right_index]
            right_index = right_index + 1
        else:
            if (target - A[left_index]) <= (A[right_index] - target):
                all_KNNs[left_index] = A[left_index]
                left_index = left_index - 1
            else:
                all_KNNs[right_index] = A[right_index]
                right_index = right_index + 1
                     
        remaining_k = remaining_k - 1
        
    #Return only the values that are not zero/indices not populated
    #This will maintain the ordering
    all_KNNs = [val for val in all_KNNs if val != 0]
        
    return all_KNNs    


if __name__ == "__main__":
    if len(sys.argv) == 4:
        A = ast.literal_eval(sys.argv[1])
        target = sys.argv[2]
        k = sys.argv[3]
        kNearest_DC = get_k_nearest_DC(A, target, k)
        print(kNearest_DC)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q1b_Afolabi_Vanessa.py "[10,15,17,18,20,21]" 14 4
        


