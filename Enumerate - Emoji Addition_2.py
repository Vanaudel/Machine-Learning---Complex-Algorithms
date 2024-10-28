#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast
import numpy as np
import itertools


import random

def get_List_of_EmojiDigitAssignments():
    
    List_of_EmojiDigitAssignments = {}
    extra_digits = {}

    #Find smiley
    smiley = random.randint(0, 9)
    List_of_EmojiDigitAssignments['smiley'] = smiley


    #Find cat
    sum_smiley = smiley + smiley
    if len(str(sum_smiley)) == 2:
        cat = int(str(sum_smiley)[-1])
        cat_carry_over = int(str(sum_smiley)[0])
    elif len(str(sum_smiley)) == 1:
        cat = int(str(sum_smiley))
        cat_carry_over = 0
    List_of_EmojiDigitAssignments['cat'] = cat


    #Find heart
    heart = random.randint(0, 9)
    List_of_EmojiDigitAssignments['heart'] = heart


    #Find dog
    sum_heart = heart + heart + cat_carry_over
    if len(str(sum_heart)) == 2:
        dog = int(str(sum_heart)[-1])
        dog_carry_over = int(str(sum_heart)[0])
    elif len(str(sum_heart)) == 1:
        dog = int(str(sum_heart))
        dog_carry_over = 0
    List_of_EmojiDigitAssignments['dog'] = dog


    #Find couple
    couple = random.randint(0, 9)
    List_of_EmojiDigitAssignments['couple'] = couple


    #Find family
    sum_couple = couple + couple + dog_carry_over
    if (len(str(sum_couple)) == 2):
        first_digit = int(str(sum_couple)[0])
        family = first_digit
        second_digit = int(str(sum_couple)[-1])
        List_of_EmojiDigitAssignments['family'] = family
        extra_digits["first_digit"] = first_digit
        extra_digits["second_digit"] = second_digit
    
    return List_of_EmojiDigitAssignments, extra_digits




def SolveMyEmojiPuzzle_enhanced():
        
    #Check the validity of the emoji assignments
    valid_dict = {}
    while len(valid_dict) == 0:
        
        #Get all 6 emoji digit assignments
        List_of_EmojiDigitAssignments, extra_digits = get_List_of_EmojiDigitAssignments()
        while len(List_of_EmojiDigitAssignments) != 6:
            List_of_EmojiDigitAssignments = get_List_of_EmojiDigitAssignments()
        
        if ((len(List_of_EmojiDigitAssignments.values()) == len(set(List_of_EmojiDigitAssignments.values()))) and 
            (List_of_EmojiDigitAssignments["couple"] != 0) and 
            (List_of_EmojiDigitAssignments["family"] != 0) and
           (List_of_EmojiDigitAssignments["smiley"] == extra_digits['second_digit'])):
            valid_dict = List_of_EmojiDigitAssignments
        else:
            valid_dict = {}
        
    summand = int(str(assignment['couple']) + str(assignment['heart']) + str(assignment['smiley']))
    addition_result = summand + summand
    
    return (summand, addition_result)



if __name__ == "__main__":
    if len(sys.argv) == 1:
        emoji_solutions_enhanced = SolveMyEmojiPuzzle_enhanced()
        print(emoji_solutions_enhanced)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q5b_Afolabi_Vanessa.py
        


