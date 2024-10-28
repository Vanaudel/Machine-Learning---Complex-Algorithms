#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np



def knapsack_extension_DP_solutions(dp_table, capacity, weights):
    
    item_num = len(weights)-1
    C = int(capacity)
    chosen_values = []
    
    while C > -1:

        #Start traversing the dp table from the bottom left
        if dp_table[item_num][C] == dp_table[item_num-1][C]:

            #From the bottom, move one row up
            item_num = item_num - 1
        else:
            chosen_values.append(item_num)

            #From the bottom, move one row up
            item_num = item_num - 1

            #Compute the new capacity by subtracting the
            C = C-weights[item_num]
        
    #Aggregate the selected items
    selected_items = {}
    for val in chosen_values:
        if val in selected_items:
            selected_items[val] = selected_items[val] + 1
        else:
            selected_items[val] = 1
            
    #Sort dictionary based on keys
    selected_items = dict(sorted(selected_items.items()))

    return selected_items



if __name__ == "__main__":
    if len(sys.argv) == 4:
        dp_table = ast.literal_eval(sys.argv[1])
        capacity =sys.argv[2]
        weights = ast.literal_eval(sys.argv[3])
        dp_solution = knapsack_extension_DP_solutions(dp_table, capacity, weights)
        print(dp_solution)
    else:
        print("Not enough arguments")

#python DS8001_Midterm_Q3c_Afolabi_Vanessa.py "[[0,10,20,30,40,50], [0,10,20,30,40,50], [0,10,20,40,50,60], [0,10,20,40,50,60]]" 5 "[1,2,3,5]"
