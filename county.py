#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Counts bases in a nucleic acid sequence

# Declare a NA sequence
sequence = "AGCCATTAGCTTAAUUU"

sequence_spaced = ""
counter = 0

# For each letter in sequence do the following
for letter in sequence:
# - Copy this letter to sequence_based
    sequence_spaced = sequence_spaced + letter
# - Increase counter by 1
    counter = counter + 1
# - If counter equals 4 do the following
    if counter == 4:
# - - add a space to sequence_based
        sequence_spaced = sequence_spaced + " "
# - - set counter = 0
        counter = 0

# Present sequence to user
print("Our sequence is", sequence_spaced)

# Count all bases in this sequence
nobases = len(sequence)

# Present count to user
print("It contains", nobases, "bases in total.")

bases = ["adenine", "guanine", "thymine", "cytosine", "uracil"]

# For each base in bases do the following
for basename in bases:
# - get first letter capitalized
    letter = basename[0].upper()
# - count occurences of this letter in sequence
    occurence = sequence.count(letter)
# - present this occurence to the user
    print("It contains", occurence, basename + "s")


# Count individual bases
#noadenines = sequence.count("A")
#noguanines = sequence.count("G")
#nothymines = sequence.count("T")
#nocytosines = sequence.count("C")

# Present numbers to user
#print("It contains", noadenines, "adenines.")
#print("It contains", noguanines, "guanines.")
#print("It contains", nothymines, "thymines.")
#print("It contains", nocytosines, "cytosines.")



