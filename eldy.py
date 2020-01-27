#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import happy
import cProfile

source = "AATAA"
targets = [source, "AAGAA", "AAATA", "TTATT", "TTGTT"]

for t in targets:
    ld = happy.levenshtein_distance(source, t)
    print(source + "\t" + t + "\t" + str(ld))
    

print(cProfile.run("happy.levenshtein_distance('AATAA', 'TTGTT')"))

# old recursive version: 8455 function calls, 36ms
# new iterative version: 42 function calls, 1ms