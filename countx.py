#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:10:35 2019

@author: Presenter
"""

# declare a sequence
sequence = "AGCTXXRRRGGCTRXXX"

#nobases = len(sequence)
#
#nocommonbases = sequence.count("A") + sequence.count("T") + \
#              + sequence.count("G") + sequence.count("C") + \
#              + sequence.count("U")
#
#nouncommonbases = nobases - nocommonbases

# define common bases
commonbases = ["A", "G", "C", "T", "U"]

# define a counter, set it to zero
nouncommonbases = 0

# for each letter of the sequence do the following
for letter in sequence:
# - if letter is not in list do the following
    if letter not in commonbases:
# - - increase counter by one
        nouncommonbases += 1

# Present counter to user
print("Number of non-common bases in sequence:", nouncommonbases)

