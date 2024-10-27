#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""


import sys

def GetLongSpecialSubstring_DC(word):
    word = str(word)
    
    #Any string that contains less than 2 characters cannot be a Special String
    if len(word) < 2:
        return ""
        
    #Begin looking for both an uppercase and lowercase instance for each character in word
    for i in range(len(word)):
        if ((word[i].upper() not in word) | (word[i].lower() not in word)):
            left_half_word = GetLongSpecialSubstring_DC(word[:i])
            right_half_word = GetLongSpecialSubstring_DC(word[i+1:])
            return left_half_word if len(left_half_word) > len(right_half_word) else right_half_word
        
    return word  


if __name__ == "__main__":
    if len(sys.argv) == 2:
        ss = GetLongSpecialSubstring_DC(sys.argv[1])
        print(ss)
    else:
        print("Not enough arguments")
        
        
        
#Function call
# python HW2_2_Vanessa_Afolabi.py FdedDdfgGgGHHhpiIbBJJjKkK
