#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""



import sys
import ast
from itertools import product

def min_cost_vertex_coloring_enumeration(costs):
    
    def feasible_combination(combination):
        for i in range(len(combination) - 1):
            if combination[i] == combination[i+1]:
                return False
        return True

    
    def calculate_cost_combination(combination, costs):
        total_cost = 0
        for i in range(len(combination)):
            node_number = i
            node_color = combination[i]
            total_cost = total_cost + costs[node_number][node_color]
        return total_cost

    
    #Get all possible combinations 
    number_nodes = len(costs)  
    number_colors = len(costs[0]) 
    #all_combinations = list(product(range(number_colors), range(number_colors), range(number_colors)))
    all_combinations = list(product(range(number_colors), repeat=number_nodes))
    
    
    #Enumerate list of feasible/valid combinations
    #Feasible means that all adjacent nodes have different color
    all_feasible_combinations = []
    for combination in all_combinations:
        if feasible_combination(combination):
            all_feasible_combinations.append(combination)
            
    
    #Calculate cost associated with each feasible/valid combination
    cost_all_feasible_combinations = []
    for combination in all_feasible_combinations:
        cost_all_feasible_combinations.append(calculate_cost_combination(combination, costs))
    
    
    #Get the minimum cost combination and its corresponding minimum cost
    min_cost = min(cost_all_feasible_combinations)
    index_min_cost = cost_all_feasible_combinations.index(min_cost)
    
    return min_cost, all_feasible_combinations[index_min_cost]



if __name__ == "__main__":
    if len(sys.argv) == 2:
        costs = ast.literal_eval(sys.argv[1])
        min_cost_enum , best_coloring_enum = min_cost_vertex_coloring_enumeration(costs)
        print(min_cost_enum)
        print(best_coloring_enum)
    else:
        print("Not enough arguments")
        
        
#Function call
# python HW2_5a_Vanessa_Afolabi.py "[[18,3,18], [14,14,4], [15,3,17]]"
# python HW2_5a_Vanessa_Afolabi.py "[[18,3,18], [14,14,4], [15,3,17], [16,3,17]]"