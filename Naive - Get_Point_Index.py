#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""


import time
import sys
import ast
from datetime import timedelta


def GetPointIndex_naive(A):
    start_time = time.monotonic()
    found = False

    for i in range(len(A)):
        if A[i] == i:
            found = True
            break
        
    end_time = time.monotonic()
    run_time = timedelta(seconds=end_time - start_time)
    
    return found, run_time



if __name__ == "__main__":
    if len(sys.argv) == 2:
        A = ast.literal_eval(sys.argv[1])
        bool_val, run_time = GetPointIndex_naive(A)
        print(bool_val)
        print(run_time)
    else:
        print("Not enough arguments")
        
        
#Function call
# python HW2_1a_Vanessa_Afolabi.py "[-3,0,5,4,5,5,7]"
# python HW2_1a_Vanessa_Afolabi.py "[-3,0,5,4,5,6,7]"
