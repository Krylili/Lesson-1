#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:32:39 2019

@author: Presenter
"""

import matplotlib.pyplot as plt
import sys


# Declare sequences: easier to test when you are still
# writing the core functionality of the program
na_sequence = "CTACGGTAAATCGGCAGTCAAAGAAGCCTATATGAGTTATGGGACAAATCAAGGATTAATATCTGAAGCATAGTCCAGGC"
qs_sequence = "  GGHGFGGGGGHHHHHHGHF620BF##2E3F6HFE2EF#GF33BD31D&3#1F3%3/EBGGGFGGGGGFFFFFDEFFFE"

# Use this lines if you want the user to input sequences
# each time
#na_sequence = input("NA Sequence:")
#qs_sequence = input("QS Sequence:")

# Define a function: normalizes a Phred sequence by 
#                    replacing all characters not in
#                    the desired range by "!" (=0)
def norm_Phred_seq(sequence):
    norm_sequence = ""
    for letter in sequence:
        # in lecture this was wrong - Illumina 1.8 is 
        # from 0..41, i.e. from "!" to "J"
        if ord("!") <= ord(letter) <= ord("J"):  
            norm_sequence += letter
        else:
            norm_sequence += "!"
    return norm_sequence


# Check if input sequences are equal in length,
# if not exit the program
if len(na_sequence) != len(qs_sequence):
    print("NA sequence and QS sequence have to be the same length!")
    sys.exit()
    
# Normalize the QS sequence (replacing non-legal characters in the string)
qs_sequence = norm_Phred_seq(qs_sequence)
# Advantage: after this function we can assume that there are only legal
# characters in qs_sequence

# Calculate quality scores by getting the ordinals from
# the letters and subtracting the reference ("!" => 0) 
# from the result
scores = []
for letter in qs_sequence:
    # in lecture this was wrong - Illumina 1.8 is 
    # from 0..41, i.e. from "!" to "J"; therefore,
    # we do not need to add anything here
    Q = ord(letter) - ord("!")
    scores.append(Q)
    
# Calculate accuracies in percentage by calculating the 
# probability from the quality scores first: P = 10^(-Q/10)
accuracies = []
for Q in scores:
    P = 10.0 ** (-Q / 10.0)
    a = (1.0 - P) * 100.0  # accuracy in percentage
    accuracies.append(a)
  
# Present the results in a nice table showing some 
# of the string formatting capabilities
print("Base\tPhred QS\tAccuracy")
print("-" * 35)
for index in range(len(na_sequence)):
    print(na_sequence[index] + "\t" +
          str(scores[index]) + "\t" +
          "{0:.3f}%".format(accuracies[index])
          )

# calculate a sequence-quality measure
bases = [na_sequence[index] + str(index + 1) for index in range(len(na_sequence))]

# Let's avoid "magic numbers" and define the threshold as a variable here
threshold = 30

# Present the results to the user - figuratively
# First as Bases vs Score Bar diagram
plt.Figure()
plt.bar(bases[20:30:2], scores[20:30:2])
plt.xlabel("Bases")
plt.ylabel("Phred QS")
plt.show()

# then as a Histogram
plt.Figure()
plt.hist(scores, 10)  # 10 is the number of groups
plt.vlines(threshold, 0, max(scores))
plt.xlabel("Phred QS")
plt.show()

# Count the occurences of each possible QS (0..41) in scores
# and save the result in a list
occurences = [scores.count(QS) for QS in range(42)]
# Advantage: the index can now be used to access individual
# counts of QS - ideal for slicing!
print(sum(occurences[threshold:]))

# TODO: Calculate the fraction of above-threshold bases: if you are
#       reading this - try to implement it :)

