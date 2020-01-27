#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:30:19 2019

@author: Presenter
"""

# declare a sequence: starts with starting codon
sequence = "AUGGGCGGCGGCGGCGGCGGCXX"

# split sequence into codons

# declare empty codon string
lastcodon = ""

# declare empty list of codons
codons = []

# for each letter of sequence do the following
for letter in sequence:
# - add letter to codon
    lastcodon += letter
# - if len(codon) equals 3 do the following
    if len(lastcodon) == 3:
# - - add codon to this list
        codons.append(lastcodon)
#        codons += [lastcodon]
# - - empty codon string
        lastcodon = ""

print(codons)

#declare empty protein sequence
proteinseq = ""

# for each codon do the following
for codon in codons:
# - if codon is "GGC" do the following
    if codon == "GGC":
# - - add "Gly" to protein sequence
        proteinseq += "Gly"
    # and of course all the other codons from the table
    
    
    
    
    
    
    
    
    
    
    
