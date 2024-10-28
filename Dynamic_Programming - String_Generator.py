#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np
from random import choice
import difflib
import time


# a helper function to get the overlap between s1 and s2
def get_overlap(s1, s2):
        
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))
    s_overlap = s1[pos_a:pos_a+size]    
    
    # check if the overlap is VALID: begin of one, end of other one is only valid setting
    # e.g., s1="III" and s2 = "EIE" does not have valid overlap due to "I"
    if (s_overlap == s1[:size] and s_overlap == s2[-size:]) or (s_overlap == s1[-size:] and s_overlap == s2[:size]):
        return s_overlap
    else:
        return ""

    
    
def merge_strings(s1,s2):
    
    #Get the overlap
    overlap_s1s2 = get_overlap(s1, s2)
    
    #Add prefix and suffix of both strings to the overlap
    merge_option_1 = s1.replace(overlap_s1s2, '') + overlap_s1s2 + s2.replace(overlap_s1s2, '')
    merge_option_2 = s2.replace(overlap_s1s2, '') + overlap_s1s2 + s1.replace(overlap_s1s2, '')
    
    #find the option that contains both s1 and s2 as substrings
    merged_strings_s1_s2 = ''
    if s1 in merge_option_1 and s2 in merge_option_1:
        merged_strings_s1_s2 = merge_option_1
    elif s1 in merge_option_2 and s2 in merge_option_2:
        merged_strings_s1_s2 = merge_option_1
    
    return merged_strings_s1_s2



def StringGenerator_efficient(S):
    
    def helper_StringGenerator_efficient(S):    
        n = len(S)
        overlap_pairs_2d = [[0]*n for i in range(n)]

        #Merge strings for the first row
        for i in range(n):
            overlap_pairs_2d[0][i] = get_overlap(S[0],S[i])

        #Get all remaining merged strings
        for i in range(1, len(S)):
            for j in range(len(S)):
                option_1 = get_overlap(S[i],S[j])
                option_2 = get_overlap(S[i],overlap_pairs_2d[i-1][j])
                if len(option_1) > len(option_2):
                    overlap_pairs_2d[i][j] = option_1
                else:
                    overlap_pairs_2d[i][j] = option_2

        #traceback to get the biggest overlap in each row then merge
        all_traceback = []
        for row in overlap_pairs_2d:
            #get longest string in the list
            longest = max(row, key=len)
            all_traceback.append(longest)

        #combined efficient string
        combined_efficient_str = ''
        for i in range(len(all_traceback)):
            combined_efficient_str = merge_strings(combined_efficient_str,all_traceback[i])

        return combined_efficient_str
    
    #Compute the efficient run time
    start_time = time.time()
    combined_efficient_str = helper_StringGenerator_efficient(S)
    end_time = time.time()
    efficient_run_time = start_time - end_time
    
    return combined_efficient_str, efficient_run_time



if __name__ == "__main__":
    if len(sys.argv) == 2:
        S = ast.literal_eval(sys.argv[1])
        combined_efficient_str, efficient_run_time = StringGenerator_efficient(S)
        print(combined_efficient_str)
        print(efficient_run_time)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q2b_Afolabi_Vanessa.py "['III', 'IIE', 'IEE', 'EEE', 'EEI']" 
        


