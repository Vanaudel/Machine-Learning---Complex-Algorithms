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


def EnumerateOrderedDigits(n):
    return list(itertools.permutations(range(10),n))


def SolveMyEmojiPuzzle():
    
    Emojis = ['couple', 'family', 'heart', 'smiley', 'dog', 'cat']
    OrderedDigits = EnumerateOrderedDigits(6)
    
    #Assign a different digit to each emoji in the emojic-expressions without leading zeroes
    OrderedDigits = [od for od in OrderedDigits if od[0] != 0 and od[1] != 0]
    
    List_of_EmojiDigitAssignments = [dict(zip(Emojis,od)) for od in OrderedDigits]
    
    Solutions = []
    for assignment in List_of_EmojiDigitAssignments:
        summand = int(str(assignment['couple']) + str(assignment['heart']) + str(assignment['smiley']))
        addition_result = summand + summand
        correct_result = int(str(assignment['family']) + str(assignment['smiley']) + str(assignment['dog']) + str(assignment['cat']))
        if addition_result == correct_result:
            Solutions.append((summand, summand, addition_result))
        
        
    return Solutions


if __name__ == "__main__":
    if len(sys.argv) == 1:
        emoji_solutions = SolveMyEmojiPuzzle()
        print(emoji_solutions)
    else:
        print("Not enough arguments")
        
        
        
#python DS8001_Midterm_Q5a_Afolabi_Vanessa.py
        


