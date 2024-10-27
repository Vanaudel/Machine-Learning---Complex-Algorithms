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


def GetPointIndex_DC(B, indices=None):
    start_time = time.monotonic()
    def helper(B, indices=None):
        found = False

        if indices == None:
            indices = list(range(len(B)))

        mid = int(len(B)/2)
        if len(B) == 0:
            return False
        elif len(B) == 1:
            return B[0] == indices[0]
        else:
            found = (helper(B[:mid], indices[:mid]) or helper(B[mid:], indices[mid:]))

        return found 
    
    point_index = helper(B)
    end_time = time.monotonic()
    run_time = timedelta(seconds=end_time - start_time)
    
    return point_index, run_time


if __name__ == "__main__":
    if len(sys.argv) == 2:
        A = ast.literal_eval(sys.argv[1])
        bool_val, run_time = GetPointIndex_DC(A)
        print(bool_val)
        print(run_time)
    else:
        print("Not enough arguments")


#Function call
# python HW2_1b_Vanessa_Afolabi.py "[-3,0,5,4,5,6,7]"
# python HW2_1b_Vanessa_Afolabi.py "[-3,0,2,4,5,6,7]"
