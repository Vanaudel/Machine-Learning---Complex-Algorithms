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
sys.setrecursionlimit(10000)


def Cholesky(A):
    n = len(A)
    a11 = A[0][0] 
    l11 = np.sqrt(a11)
    if n == 1:
        return l11
    else:
        A21 = A[1:,0]
        L21 = (1/l11)*A21

        myL = np.zeros((n,n))
        myL[0][0] = l11
        myL[1:,0] = L21
        A_prim = A[1:,1:] - np.outer(L21,L21.transpose()) 
        myL[1:,1:] = Cholesky(A_prim)
        return np.around(myL,1)
    
    
def mean_matrix_non_zero(A):
    
    all_non_zero_vals = []
    num_rows = A.shape[0]
    num_cols = A.shape[1]
    
    for row in range(num_rows):
        for col in range(num_cols):
            all_non_zero_vals.append(A[row][col])
            
    return round(np.mean(all_non_zero_vals),1)       


def run_Cholesky_all(dic_instances):
    
    size = list(dic_instances.keys())
    cholesky_CPU = []
    cholesky_mean_L = []
    np_CPU = []
    np_mean_L = []

    for matrixSize in dic_instances.keys():
        
        # Get the SPD matrix
        AA = np.around(np.random.rand(matrixSize, matrixSize)*10, 1)
        BB = np.dot(AA, AA.transpose()) #SPD matrix

        # Method A - Cholesky decomposition
        start_time = time.time()
        cholesky_L = Cholesky(BB)
        end_time = time.time()
        elapsed_time = end_time - start_time
        cholesky_CPU.append(round(elapsed_time, 1))
        cholesky_mean_L.append(mean_matrix_non_zero(cholesky_L))

        # Method A - np decomposition
        start_time = time.time()
        np_L = np.around(np.linalg.cholesky(BB), 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        np_CPU.append(round(elapsed_time, 1))
        np_mean_L.append(mean_matrix_non_zero(np_L))

    df_ress_cholesky = pd.DataFrame({'size': size,
                                     'cholesky_mean_L':cholesky_mean_L,
                                     'cholesky_CPU':cholesky_CPU,
                                     'np_mean_L':np_mean_L,
                                     'np_CPU':np_CPU})
    return df_ress_cholesky
        

    
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dic_instances = ast.literal_eval(sys.argv[1])
        df_ress_cholesky = run_Cholesky_all(dic_instances)
        print(df_ress_cholesky)
    else:
        print("Not enough arguments")


#python HW3_3_Vanessa_Afolabi.py "{100:1, 500:1, 1000:1}"

































        
