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



#Simulated Annealing - Binary Knapsack
def simulated_annealing(w, v, W, num_iter):
    
    
    # sort the items based on their value; keep putting the items into the knapsack until reaching the capacity
    def GetInitialSolution(w, W):

        # sort the items based on their value
        sorted_v_indices = sorted(((v, i) for i, v in enumerate(v)), reverse=True)
        v_sorted = [tup[0] for tup in sorted_v_indices]
        original_indices = [tup[1] for tup in sorted_v_indices]

        #keep putting the items into the knapsack until reaching the capacity
        x = [0] * len(v)
        capacity = 0
        for i in range(len(v)):
            index = original_indices[i]
            if capacity + w[index] <= W:
                capacity = capacity + w[index]
                x[index] = 1
            i = i + 1

        return x
    
    
    #generates a neighbor solution for x_best
    def CreateNeighbor(x_best):

        #systematically change components of x_best at the random indices
        def generate_random_neighbor(x_best):

            x_new = x_best.copy()

            #pick 2 random indices
            random_indices = list(np.random.randint(0, len(x_best), size = 2))

            #Change 0 to 1 and change 1 to 0
            for index in random_indices:
                if x_best[index] == 1:
                    x_new[index] = 0
                elif x_best[index] == 0:
                    x_new[index] = 1

            return x_new

        x_new =  generate_random_neighbor(x_best)       
        #check if the generated neighbor is feasible; keep trying to find a feasible solution
        while sum(x_new * w) > W:
            x_new =  generate_random_neighbor(x_best)        

        return x_new
    
    
    #Decrease the temperature over iterations
    def ReduceTemperature(T, k):
        return (T/k) + 0.1
    
    
    #initial temperature
    T0 = 1000
    T = T0
    x_best = GetInitialSolution(w, W)
    
    for k in range(num_iter):
        x_new = CreateNeighbor(x_best)
        if sum(x_new * v) >= sum(x_best * v):
            x_best = x_new
        else:
            #random number between 0 and 1
            r = random.uniform(0, 1)
            exponent_value = (-1 * abs(sum(x_new * v) - sum(x_best * v)))/T
            if r < math.exp(exponent_value):
                x_best = x_new
                
        T = ReduceTemperature(T, k+1)
    
    return x_best    
    
    

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




def run_Knapsack_SA_all(dic_instances):
    
    n_items = list(dic_instances.keys())
    SA_list = []
    DP_list = []
    gap_list = []
    for n in n_items:
        v_value = np.random.randint(1,20, size = n)
        v_weight = np.random.randint(1,10, size = n)
        v_sampleSoln = np.random.binomial(1, 0.25, size=n)
        d_TotalWeight = sum(v_sampleSoln * v_weight) #25% of the items selected to get W
        num_iter = 100
        
        #Simulated Annealing - Binary Knapsack
        SA = simulated_annealing(v_weight, v_value, d_TotalWeight, num_iter)
        SA_value = sum(SA * v_value)
        SA_list.append(SA_value)
        
        #Dynamic Programming - Binary Knapsack
        gdfItems = pd.DataFrame({'weight': v_weight,
                                 'value': v_value})
        dtotalVal_DP, vlistItems_DP = DP_knapsack(gdfItems, d_TotalWeight)
        DP_list.append(dtotalVal_DP)
        
        #Calculate gap between DP optimal value and simulated annealing value
        gap = (SA_value - dtotalVal_DP)/(dtotalVal_DP)
        gap_list.append(gap)
        
        
    df_ress_SA = pd.DataFrame({'n_items':n_items,
                               'SA': SA_list,
                               'Opt':DP_list,
                               'Gap': gap_list})
    
    return df_ress_SA




if __name__ == "__main__":
    if len(sys.argv) == 2:
        dic_instances = ast.literal_eval(sys.argv[1])
        df_ress_SA = run_Knapsack_SA_all(dic_instances)
        print(df_ress_SA)
    else:
        print("Not enough arguments")


#python HW3_4_Vanessa_Afolabi.py "{100:1, 500:1, 1000:1}"  

































        
