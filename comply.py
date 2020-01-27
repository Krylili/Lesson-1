#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:35:38 2019

@author: Presenter
"""

# declare a sequence
sequence = "AAAAAAGGGGCCXXCTTTUUU"
print(sequence)

# declare an empty complementary sequence
com_sequence = ""

com_bases = {"A": "T", "T": "A", "G": "C", "C": "G", "U": "A"}

for letter in sequence:
    if letter in com_bases:
        com_sequence += com_bases[letter]
    else:
        print("Unknown base", letter)
        com_sequence += "-"

## for each letter in sequence do the following
#for letter in sequence:
## - if letter is "A" do the following
#    if letter == "A":
## - - add "T" to complementary sequence
#        com_sequence += "T"   
#
## - else if letter is "G" do the following
#    elif letter == "G":
## - - add "C" to complementary sequence
#        com_sequence += "C"
#        
## - else if letter is "C" do the following
#    elif letter == "C":
## - - add "G" to complementary sequence
#        com_sequence += "G"
#
## - else if letter is "T" do the following
#    elif letter == "T" or letter == "U":
## - - add "A" to complementary sequence
#        com_sequence += "A"
#        
#    else:
#        print("Unknown base:", letter)

# present to the user
print(com_sequence)
