#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np




def knapsack_extension_DP(values, weights, capacity):
    all_opt_iw = np.empty((len(values)+1, int(capacity) + 1))
    all_opt_iw.fill(0)

    #no subset of items being used initially; set all OPT(0,w) to 0
    for w in range(int(capacity) + 1):
        all_opt_iw[0][w] = 0

    #Compute the max profit subset of items 1,...,i with weight limit w    
    for i in range(1,len(values) + 1): #pick the subset of items 1..i e,g {},{1},{1,2},{1,2,3},{1,2,3,4}
        for w in range(int(capacity) + 1): #Get max profit for each incremental capacity from 0 to capacity inclusive e.g 0,1,3,4,5
            if (weights[i-1] > w): #in python indices start at 0; if wi > w
                all_opt_iw[i][w] = all_opt_iw[i-1][w]
            else:
                delta_weight = w - weights[i-1]
                all_opt_iw[i][w] = max(all_opt_iw[i-1][w], (values[i-1] + all_opt_iw[i][delta_weight]))
                
    #Get the total max value
    total_value_dp = all_opt_iw[len(all_opt_iw)-1][len(all_opt_iw[0])-1]
    
    return total_value_dp, all_opt_iw[1:]



if __name__ == "__main__":
    if len(sys.argv) == 4:
        values = ast.literal_eval(sys.argv[1])
        weights = ast.literal_eval(sys.argv[2])
        capacity = sys.argv[3]
        total_value_dp, dp_table = knapsack_extension_DP(values, weights, capacity)
        print(total_value_dp)
        print(dp_table)
    else:
        print("Not enough arguments")

        
        
#python DS8001_Midterm_Q3b_Afolabi_Vanessa.py "[10,15,40,55]" "[1,2,3,5]" 5
#python DS8001_Midterm_Q3b_Afolabi_Vanessa.py "[1,4,5,7]" "[1,2,5,6,7]" 11
#python DS8001_Midterm_Q3b_Afolabi_Vanessa.py "[1,6,18,22,28]" "[1,2,5,6,7]" 11

