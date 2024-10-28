#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np
from scipy.optimize import fmin



def get_fmin_value(fx, starting_point):
    x_sol = np.around(fmin(fx,starting_point), 2).tolist()
    opt_val = fx(x_sol)
    
    return x_sol, opt_val



if __name__ == "__main__":
    if len(sys.argv) == 3:
        lambda_func_str = sys.argv[1]
        list_vals = lambda_func_str.split(":")
        fx = lambda x: eval(list_vals[1].strip())
        starting_point = ast.literal_eval(sys.argv[2])
        x_sol, opt_val = get_fmin_value(fx, starting_point)
        print(x_sol)
        print(opt_val)
    else:
        print("Not enough arguments")


#python DS8001_Midterm_Q4a_Afolabi_Vanessa.py "lambda x: 2*x[0]*x[0] + 3*x[1]*x[1] + x[2]*x[2] + 2*x[0]*x[1] - 6*x[0] - 4*x[1] + 24" "[0,0,0]" 
