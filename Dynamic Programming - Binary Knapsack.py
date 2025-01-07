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
import math
import random
sys.setrecursionlimit(10000)



    

#Dynamic Programming - Binary Knapsack    
def DP_knapsack(gdfItems, gW):
    '''
    For a given a dataframe that holds the information on the items, 
    return total value of the the items and the id's of the 
    items (as a list) using a DP algo
    '''
    
    t_dpTable = np.zeros((gdfItems.shape[0]+1, gW+1))
    t_dpTable_items = np.zeros((gdfItems.shape[0]+1, gW+1))

    # print(t_dpTable)
    # print('\n')

    for i in list(gdfItems.index):
        for w in range(gW+1):
            if (gdfItems.loc[i].weight <= w) and (gdfItems.loc[i].value + t_dpTable[i-1][w - gdfItems.loc[i].weight] > t_dpTable[i-1][w]):
                t_dpTable[i][w] = gdfItems.loc[i].value + t_dpTable[i-1][w - gdfItems.loc[i].weight]
                t_dpTable_items[i][w] = 1
            else:
                t_dpTable[i][w] = t_dpTable[i-1][w]
    
    # print(t_dpTable)
    # print('\n')

    # print(t_dpTable_items)
    # print('\n')

    tmp_vpicks = []
    t_dRemaining_cap = gW

    # traverse the DP table to identify which items were picked
    for i in range(gdfItems.shape[0],0,-1):
        if t_dpTable_items[i][t_dRemaining_cap] == 1:
            tmp_vpicks.append(i)
            t_dRemaining_cap -= gdfItems.loc[i].weight
    tmp_vpicks.sort()
    # print("tmp_vpicks: %s" %tmp_vpicks)

    return t_dpTable[list(gdfItems.index)[-1]][gW], tmp_vpicks    






        
