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



def StringGenerator_greedy(S):
    
    if len(S) == 1:
        return S
    
    #Compute overlap for every pair of distinct elements in S
    overlap_pairs_dict = {}
    for i in range(len(S) - 1):
        key = S[i] + '-' + S[i+1]
        overlap_pairs_dict[key] = get_overlap(S[i], S[i+1])
        
        
    #Choose two distinct elements of S with the maximum overlap
    overlap_lengths_dict = {}
    for key, value in overlap_pairs_dict.items():
        overlap_lengths_dict[key] = len(value)
    overlap_lengths_dict = dict(sorted(overlap_lengths_dict.items(), key=lambda item: item[1]))
    max_elements = list(overlap_lengths_dict)[-1]
    max_1 = max_elements.split('-')[0]
    max_2 = max_elements.split('-')[1]
        
        
    #Merge the selected elements and add the obtained string to S
    merged_strings = merge_strings(max_1, max_2)
    S.append(merged_strings)
    
    #Remove the selected two elements from S
    S.remove(max_1)
    S.remove(max_2)
    
    return StringGenerator_greedy(S)



def StringGenerator_recursive_greedy(S):
    start_time = time.time()
    combined_recursive_str = StringGenerator_greedy(S)
    end_time = time.time()
    recursive_run_time = start_time - end_time
    return combined_recursive_str, recursive_run_time



if __name__ == "__main__":
    if len(sys.argv) == 2:
        S = ast.literal_eval(sys.argv[1])
        combined_recursive_str, recursive_run_time = StringGenerator_recursive_greedy(S)
        print(combined_recursive_str)
        print(recursive_run_time)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q2a_Afolabi_Vanessa.py "['III', 'IIE', 'IEE', 'EEE', 'EEI']" 
        


