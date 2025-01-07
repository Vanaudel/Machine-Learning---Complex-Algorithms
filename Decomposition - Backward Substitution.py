#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np


def BackwardSubstitution(A,b):
    
    def BS(A,b,y):
        
        n = len(A)
        y_n = b[n-1][0]/A[n-1][n-1]
        y[n-1] = y_n

        if n==1:
            return y
        else:
            #Extract the new A i.e A_1_1
            A11 = A[:n-1,:n-1]
            b1 = b[:n-1].reshape(-1) - (y_n * A[:,n-1][:n-1])
            b1 = b1.reshape(n-1,1)
            y = BS(A11,b1,y)
            return y
        
    y = np.zeros((len(A)))    
    return BS(A,b,y)  


