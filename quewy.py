#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:40:03 2019

@author: Presenter
"""

# Import our "happy" module that includes the FASTQ-functions
import happy

# Ask the user for a filename; for convenience at the testing and 
# development stage, we predefine a string with our testfile so
# that we do not have to type in the name of the file each time
# we run the program
#filename = input("Please provide a FASTQ-file (incl. extension) to process:")
filename = "tenthousandseq.fastq"

# Try to open and process this FASTQ file; if something goes wrong
# then errors will be caught by the "except:"-blocks at the bottom
try:
    # Open the file for reading ("r")
    fastqfile = open(filename, "r")
    
    # Start with an empty set of lines and a dataset ID counter at 1
    dataset_id = 1
    fastq_lines = []
    
    # TODO: Print a header line
    
    # For each line in the file do the following:
    for line in fastqfile:
        # Append the line to the above list
        fastq_lines.append(line)
        
        # If there are 4 lines (i.e. a complete FASTQ-set) in the list
        # do the following
        if len(fastq_lines) == 4:
            # Process these lines by our function in "happy" that turns
            # these lines into a handy dataset dictionary
            dataset, errno = happy.convert_FASTQ_into_dictionary(fastq_lines)
            
            # If the function showed no error, do the following:
            if errno == happy.FASTQ_NOERROR:
                # Print a tabular line with several columns (separated by
                # tabulator, i.e. \t) containing
                # - dataset ID
                # - Sequence ID
                # - NA Sequence
                # - Quality score
                # - Quality sequence
                print("{0:d}\t{1:s}\t{2:d}\t{3:s}\t{4:.1f}%\t{5:s}".
                      format(dataset_id, dataset["Sequence ID"], 
                             len(dataset["Sequence"]), dataset["Sequence"],
                             happy.Phredy_quality_fraction(dataset["Quality sequence"]) * 100.0,
                             dataset["Quality sequence"]))
    
                # Empty the list of collected lines for the next set
                fastq_lines = []
                
                # Increase the dataset ID by one
                dataset_id += 1
    
    # Close the file
    fastqfile.close()
    
# Catching File-not-found errors as exception; we print an error message
# to the console as well as append ("a" in open) a string to an error.txt
except FileNotFoundError as exc:    
    errorfile = open("error.txt", "a")
    errorfile.write("Filenotfound error\n")
    errorfile.close()
    
    print("Error:", exc)
    
# Catching other errors that might happen; again, we print an error message
# to the console as well as append ("a" in open) a string to an error.txt
except:
    errorfile = open("error.txt", "a")
    errorfile.write("Unknown error\n")
    errorfile.close()
    
    print("Unknown error")
    




