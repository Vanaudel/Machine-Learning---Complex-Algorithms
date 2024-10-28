#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np



def knapsack_extension_greedy(values, weights, capacity):
    
    def get_next_greedy_index(values, weights, capacity):
        #compute the weight per value ratio and sort in decreasing order
        ratio = []
        for i in range(len(values)):
            ratio.append(values[i]/weights[i])
            
        #Find the index of the best ratio whose weight is <= remaining_capacity
        for val in sorted(ratio, reverse=True):
            index = ratio.index(val)
            if int(weights[index]) <= int(capacity):
                return index

            
    # Put the maximum number of items with the best ratio into the knapsack, and move to
    # the next items according to the ratio until the knapsack is filled
    remaining_capacity = capacity
    all_indices = []
    while remaining_capacity != 0:
        next_index = get_next_greedy_index(values, weights, remaining_capacity)
        all_indices.append(next_index)
        remaining_capacity = int(remaining_capacity) - int(weights[next_index])
        
    
    #Compute total value
    total_value = 0
    for val in all_indices:
        total_value = total_value + values[val]
        
        
    #Aggregate the selected items
    selected_items = {}
    for val in all_indices:
        if val in selected_items:
            selected_items[val] = selected_items[val] + 1
        else:
            selected_items[val] = 1
            
    #Sort dictionary based on keys
    selected_items = dict(sorted(selected_items.items()))
        
    return total_value, selected_items


if __name__ == "__main__":
    if len(sys.argv) == 4:
        values = ast.literal_eval(sys.argv[1])
        weights = ast.literal_eval(sys.argv[2])
        capacity = sys.argv[3]
        total_value, selected_items = knapsack_extension_greedy(values, weights, capacity)
        print(total_value)
        print(selected_items)
    else:
        print("Not enough arguments")


#python DS8001_Midterm_Q3a_Afolabi_Vanessa.py "[10,15,40,55]" "[1,2,3,5]" 5
#python DS8001_Midterm_Q3a_Afolabi_Vanessa.py "[1,4,5,7]" "[1,2,5,6,7]" 11
