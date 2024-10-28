#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np
from math import *
from scipy.optimize import fmin
from math import *


def gradient_descent_algo(starting_point, epsilon=0.005, learning_rate=0.1):
    
    
    #Return gradient of the function for a given x
    def fx_grad(x):
        #compute gradient
        n = np.size(x) # we assume this a n x 1 or 1 x n vec
        grad = np.zeros(n,'d')
        grad[0] = 4*x[0] + 2*x[1] - 6
        grad[1] = 6*x[1] + 2*x[0] - 4
        grad[2] = 2*x[2]
        return grad
    
    
    k = 0
    all_x = []
    all_x.append(starting_point)
    n_iter = 0
    fx = lambda x: 2*x[0]*x[0] + 3*x[1]*x[1] + x[2]*x[2] + 2*x[0]*x[1] - 6*x[0] - 4*x[1] + 24
    while (np.linalg.norm(fx_grad(all_x[k])) >= epsilon):
        
        #Get new eta
        func_eta = lambda eta: fx([all_x[k][0] - eta * fx_grad(all_x[k])[0],
                                   all_x[k][1] - eta * fx_grad(all_x[k])[1],
                                   all_x[k][2] - eta * fx_grad(all_x[k])[2]])
        
        new_eta = np.round(fmin(func_eta, [0], disp=False)[0],3)
        
        #Compute the new minimized x
        x_new = all_x[k] - new_eta * np.array(fx_grad(all_x[k]))
        all_x.append(x_new)
        
        k = k + 1
        n_iter = n_iter + 1
    
    #Get the optimal solution and value obtained after minimizing the function
    x_sol = np.round_(all_x[k], decimals = 2)
    opt_val = round(fx(x_sol), 2)
    
    return x_sol, opt_val, n_iter



if __name__ == "__main__":
    if len(sys.argv) == 4:
        starting_point = ast.literal_eval(sys.argv[1])
        epsilon = sys.argv[2]
        learning_rate = sys.argv[3]
        x_sol, opt_val, num_iterations = gradient_descent_algo(starting_point, epsilon=0.005, learning_rate=0.1)
        print(x_sol)
        print(opt_val)
        print(num_iterations)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q4b_Afolabi_Vanessa.py "[0,0,0]" 0.005 0.1
        


