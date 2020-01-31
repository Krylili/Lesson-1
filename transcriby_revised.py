#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:30:19 2019

@author: Presenter
"""

import sys

import librarydef

# declare a sequence: starts with starting codon
sequence = "GGTTAACAUGGGCATCGCTATATAAXXGCGTCXX"
#sequence = "AUGUUUUUAUCACUUCCACGCGGUGCCACCAUCUAAUCUUCCGUUGUGGACGGAUACCUCGUCAGAAGUUGUUGCUGGUUCUUGCUACUGAAAAAUCCCCCUCCGUCGAUAUAGGGGACUACACAACAUUAUCACAUUGCAGCGGCUGUAGGCAGGAGCCGGCGUACGCGAGAGGAUGAAAAGAACUGA"


# find AUG and split string there

ret = sequence.find("AUG")

if ret == -1:
    print("AUG not found in sequence")
    sys.exit()

cropped_seq = sequence[ret:]

print(ret,cropped_seq)

no_codons = int(len(cropped_seq) / 3)   # each codon has 3 letter
print(no_codons)
codons = [cropped_seq[c*3:c*3+3] for c in range(no_codons)]

print(codons)

 
protein_seq = ""
for c in codons:
    if c == "TAA":
        break
    
    if c in librarydef.aminoacids:
        protein_seq += librarydef.aminoacids[c] + "-"
    else:
        protein_seq += c + "-"
        
    
    
print(protein_seq[:-1])
    
    
    
    
    
    
    
    
