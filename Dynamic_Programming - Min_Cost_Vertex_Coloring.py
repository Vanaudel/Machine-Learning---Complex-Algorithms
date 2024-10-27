#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""


import sys
import ast

def min_cost_vertex_coloring_DP(costs):
    
    number_nodes = len(costs)  
    number_colors = len(costs[0]) 
    
    #Create an empty array to store all the Opt(k,i) values computed.
    all_opt_ki = [[0 for i in range(number_colors)] for k in range(number_nodes)]
  
    def Opt(k,i):
        all_costs_k_minus_1_j = []
        for j in range(number_colors): 
            if j != i:
                all_costs_k_minus_1_j.append(all_opt_ki[k-1][j])
        return costs[k][i] + min(all_costs_k_minus_1_j)

    
    #If there are no nodes to paint then there is no cost    
    if number_nodes == 0:
        min_cost_dp = 0
    
    #The first node(0) colors are already known and come from costs
    for i in range(number_colors):
        all_opt_ki[0][i] = costs[0][i]
        
    #Find the optimal color for all remaining nodes    
    for k in range(1, number_nodes):
        for i in range(number_colors):
            all_opt_ki[k][i] = Opt(k,i)
    
    #Find the minimum cost of coloring each node
    #The minimum cost of coloring the last node is the cumulative minimum of coloring all previous nodes
    min_cost_dp = min(all_opt_ki[number_nodes-1])
    
    #What is the cheapest enum of colors
    best_coloring_dp = []
    min_cost_dp_k = min(all_opt_ki[number_nodes-1])
    for k in reversed(range(number_nodes)):
        list_vals = all_opt_ki[k]
        min_index = list_vals.index(min_cost_dp_k)
        best_coloring_dp.append(min_index)
        min_cost_dp_k = min_cost_dp_k - costs[k][min_index]        
    #reverse the list
    new_best_coloring_dp = best_coloring_dp[::-1]
        
    return min_cost_dp, new_best_coloring_dp, all_opt_ki



if __name__ == "__main__":
    if len(sys.argv) == 2:
        costs = ast.literal_eval(sys.argv[1])
        min_cost_dp, best_coloring_dp, dp_table = min_cost_vertex_coloring_DP(costs)
        print(min_cost_dp)
        print(best_coloring_dp)
        print(dp_table)
    else:
        print("Not enough arguments")
        
        
#Call function
# python HW2_5b_Vanessa_Afolabi.py "[[18,3,18], [14,14,4], [15,3,17]]"
# python HW2_5b_Vanessa_Afolabi.py "[[18,3,18], [14,14,4], [15,3,17], [16,3,17]]"
