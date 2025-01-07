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
    
    












        
