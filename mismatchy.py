#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:06:52 2019

@author: Presenter
"""

#declare sequence and maybe-complementary sequence
sequence = "AAAGCCTTUUU"
maybe_compl = "TTTCGCAAACA"

# create an ideal complementary sequence of sequence
# declare an empty complementary sequence
com_sequence = ""

com_bases = {"A": "T", "T": "A", "G": "C", "C": "G", "U": "A"}

for letter in sequence:
    if letter in com_bases:
        com_sequence += com_bases[letter]
    else:
        print("Unknown base", letter)
        com_sequence += "-"

print(sequence)
print(com_sequence)  
print(maybe_compl)     

# compare ideal complementary sequence to 
# maybe-complementary sequence

# define index and set it to zero
index = 0
# for each base in sequence do the following
for base in sequence:
# - if maybe_compl[index] not equals com_sequence[index] do the following
    if maybe_compl[index] != com_sequence[index]:
        print("Mismatch found at position", index + 1, base, 
              maybe_compl[index], "should be", com_sequence[index])
# - - print to user: position (index + 1) and the mismatch
# - increase index by one
    index += 1


