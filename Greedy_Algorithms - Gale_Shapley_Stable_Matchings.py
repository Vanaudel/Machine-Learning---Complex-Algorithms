#!/usr/bin/env python
# coding: utf-8

# In[5]:

"""
Vanessa Afolabi
"""

import sys
import ast


def Orders(Array, Start, End):
    if not Start:
        Array.append(End)
    else:
        n = len(Start)
        for i in range(n):
            NextEnd = End + Start[i:i+1]  #Add the item at index i to End
            NextStart = Start[:i] + Start[i+1:]  #Remove item at index i from Start
            Orders(Array, NextStart, NextEnd)

            
def FindAllStableMatchings(MenPref, WomenPref):
    
    def Match_Is_Stable(matching, MenPref, WomenPref):
    
        for match in matching:
            
            w = match[1]
            current_male_partner_w = match[0]

            # 1: Find all the preferences for w
            all_pref_w = WomenPref[w]

            # 2: Where does the current partner rank in all of w's preferences
            current_partner_rank = all_pref_w.index(current_male_partner_w)

            # 3:Find men w would prefer over current_partner
            all_men_w_prefers_over_current_partner = all_pref_w[:current_partner_rank]
            
            #Determine if at least one of w's preferences actual prefer her over their current match
            if len(all_men_w_prefers_over_current_partner) != 0: # if len = 0 w prefers no men over her current match
                for man in all_men_w_prefers_over_current_partner:
                    
                    #Find the current partner(w) of this man in the matching
                    current_partner_man = [match[1] for match in matching if match[0] == man][0]

                    #If man prefers w to his current_partner return FALSE because NOT a stable matching
                    all_pref_man = MenPref[man]
                    if all_pref_man.index(w) < all_pref_man.index(current_partner_man):
                        return False
                    
        #At this point all the matches were found to be stable
        return True

    
    #Find the number of men and women
    n = len(MenPref)
    
    #Find all the unique men and women
    men = [i for i in range(n)]
    women = [i for i in range(n)]
    
    #Find all the women orderings
    all_orderings_women = []
    Start = women
    End = []
    Orders(all_orderings_women, Start, End)
    
    #Find/enumerate all possible matchings between men and women
    all_matchings = []
    for woman_order in all_orderings_women:
        one_match = [] 
        for i in range(n):
            one_match.append((men[i], woman_order[i]))
        all_matchings.append(one_match)

        
    #Find all the stable matching and return the count
    num_stable_matchings = 0 
    for match in all_matchings:
        if Match_Is_Stable(match, MenPref, WomenPref) == True:
            num_stable_matchings = num_stable_matchings + 1

    #return n, men, women, all_orderings_women, all_matchings
    return num_stable_matchings


if __name__ == "__main__":
    if len(sys.argv) == 3:
        MenPref = ast.literal_eval(sys.argv[1])
        WomenPref = ast.literal_eval(sys.argv[2])
        n_stable = FindAllStableMatchings(MenPref, WomenPref)
        print(n_stable)
    else:
        print("Not enough arguments")
        
        
#Function call
#python HW2_4b_Vanessa_Afolabi.py "[[5,6,4,2,0,3,1],[0,5,1,2,4,3,6],[3,6,1,2,5,0,4],[1,2,5,0,6,4,3], [6,0,2,4,3,1,5],[2,1,4,0,3,6,5],[5,6,4,2,0,1,3]]" "[[0,4,3,1,5,2,6],[5,1,4,6,3,2,0],[1,5,4,2,6,3,0],[0,1,4,5,3,2,6],[5,2,4,1,0,6,3],[5,6,3,2,0,1,4],[2,6,5,3,4,0,1]]"
