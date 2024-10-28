#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np



def get_k_nearest_naive(A, target, k):
    
    n = len(A)
    all_KNNs = [0] * n
    target = int(target)
    k = int(k)
    
    #traverse the values in the array until A[i] > target
    #If all the values in the list are less than target then the last value is closest to target
    target_vicinity_index = n
    for i in range(n):
        if A[i] >= target:
            target_vicinity_index = i
            break;
     
    
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
        kNearest_naive = get_k_nearest_naive(A, target, k)
        print(kNearest_naive)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q1a_Afolabi_Vanessa.py "[10,15,17,18,20,21]" 14 4
        


