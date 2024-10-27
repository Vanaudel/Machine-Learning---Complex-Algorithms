#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""


import pandas as pd
import sys
import numpy as np
import json
import ast

def GetNodeCover_greedy(np_adjacency):
    
    np_adjacency = np.array(np_adjacency)
    
    #Total number of edges to minimum cover with the nodes
    #total_num_edges = sum(sum(np_adjacency,[]))/2
    total_num_edges = (sum([sum(i) for i in np_adjacency]))/2

    #Selected nodes
    S = []

    #number of edges covered thus far
    count_edges = 0

    while count_edges < total_num_edges:
        
        #create a datafame using the 2D array
        np_adjacency_df = pd.DataFrame(np_adjacency)
        np_adjacency_df["Sum_Columns"] = np_adjacency_df.apply(lambda x: sum(x))

        #Find which node has the maximum number of edges
        node_with_max_edges = np_adjacency_df["Sum_Columns"].idxmax()

        #Add the node to the Minimum Set Cover
        S.append((node_with_max_edges + 1))

        #Update the number of edges covered thus far
        count_edges = count_edges + np_adjacency_df["Sum_Columns"].max()

        #Update the matrix to remove the node with max edges
        for i in range(len(np_adjacency)):  
            if np_adjacency[node_with_max_edges][i] == 1:
                np_adjacency[node_with_max_edges][i] = 0
                np_adjacency[i][node_with_max_edges] = 0

    return S


if __name__ == "__main__":
    if len(sys.argv) == 2:
        inputList = ast.literal_eval(sys.argv[1])
        list_nodes = GetNodeCover_greedy(inputList)
        print(list_nodes)
    else:
        print("Not enough arguments")

        
#Function call
# python HW2_3_Vanessa_Afolabi.py "[[0,1,0,1,0],[1,0,1,1,0],[0,1,0,1,0],[1,1,1,0,1],[0,0,0,1,0]]"

