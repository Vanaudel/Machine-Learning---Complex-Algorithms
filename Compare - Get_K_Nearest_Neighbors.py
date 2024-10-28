#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""



import sys
import ast
import numpy as np
import time
import pandas as pd
import random





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





def compare_k_nearest_algorithms(num_trials, k, array_size = 10000, array_max = 100000):
    
    num_trials = int(num_trials)
    k = int(k)
    array_size = int(array_size)
    array_max = int(array_max)
    
    
    trial = []
    all_targets = []
    all_naive_solution = []
    all_dc_solution = []
    all_naive_runtime = []
    all_dc_runtime = []
    
    
    for i in range(num_trials):
        
        trial.append(i)
        
        
        #generate a sorted array with given size (array_size) and max value 
        #(i.e., values in the array must range between [0, array_max])
        sorted_arr = sorted([random.randint(0, array_max) for val in [0]*array_size])
        
        
        #randomly generate target
        target = random.randint(0, array_max)
        all_targets.append(target)
        
        
        #Record run time of naive solution
        start_time = time.time()
        naive_solution = get_k_nearest_naive(sorted_arr, target, k)
        end_time = time.time()
        all_naive_runtime.append(end_time-start_time)
        all_naive_solution.append(naive_solution)
        
        
        #Record run time of DC solution
        start_time = time.time()
        dc_solution = get_k_nearest_DC(sorted_arr, target, k)
        end_time = time.time()
        all_dc_runtime.append(end_time-start_time)
        all_dc_solution.append(dc_solution)
        
        
    data = {'trial': trial,
            'target': all_targets,
            'naive_solution': all_naive_solution,
            'dc_solution': all_dc_solution,
            'naive_runtime': all_naive_runtime,
            'dc_runtime': all_dc_runtime}

    return pd.DataFrame(data)





if __name__ == "__main__":
    if len(sys.argv) == 5:
        num_trials = sys.argv[1]
        k = sys.argv[2]
        array_size = sys.argv[3]
        array_max = sys.argv[4]
        df_kneighbors = compare_k_nearest_algorithms(num_trials, k, array_size, array_max)
        print(df_kneighbors)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q1c_Afolabi_Vanessa.py 3 4 10000 100000
        


