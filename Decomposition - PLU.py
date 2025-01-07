#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""



import sys
import ast
import numpy as np
from scipy.linalg import lu
import math
import timeit



def determinant_calculation_comparison(A):
    
    
    #Compute the determinant by using the numpy library
    start = timeit.default_timer()
    det_np = round(np.linalg.det(A),2)
    stop = timeit.default_timer()
    np_time = stop - start
    
    #Compute the determinant using the PLU decomposition
    # A PLU decomposition of A
    # P = Permutation matrix
    # Lower = Lower triangular matrix
    # Upper = Upper triangular matrix
    P, L, U = lu(A)

    
    #The determinant of P can be computed by counting how many row swaps (k) it takes to transform an identity matrix to P
    #det(P) = (-1)^k
    #Find the number of displaced ones(not on a diagonal) and minus 1
    start = timeit.default_timer()
    num_displaced_ones = 0
    for i in range(len(P)):
        for j in range(len(P)):
            if (i==j) and (P[i][j]!=1):
                num_displaced_ones = num_displaced_ones + 1
    k = num_displaced_ones - 1
    det_P = pow(-1,k)

    
    #The determinant of a triangular matrix is the product of its diagonal elements
    all_diagonal_elements_L = []
    for i in range(len(L)):
        for j in range(len(L)):
            if i==j:
                all_diagonal_elements_L.append(L[i][j])
    det_L = np.prod(all_diagonal_elements_L)
    
    
    #The determinant of a triangular matrix is the product of its diagonal elements
    all_diagonal_elements_U = []
    for i in range(len(U)):
        for j in range(len(U)):
            if i==j:
                all_diagonal_elements_U.append(U[i][j])
    det_U = np.prod(all_diagonal_elements_U)
    
    det_plu = round((det_P * det_L * det_U),2)
    stop = timeit.default_timer()
    plu_time = stop - start
    
    return det_np, np_time, det_plu, plu_time



if __name__ == "__main__":
    if len(sys.argv) == 2:
        A = ast.literal_eval(sys.argv[1])
        det_np, np_time, det_plu, plu_time = determinant_calculation_comparison(A)
        print(det_np)
        print(np_time)
        print(det_plu)
        print(plu_time)
    else:
        print("Not enough arguments")

#Call function
# python HW3_2a_Vanessa_Afolabi.py "[[2,5,8,7],[5,2,2,8],[7,5,6,6],[5,4,4,8]]" 


