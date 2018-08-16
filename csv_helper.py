# -*- coding: utf-8 -*-
"""
CSV-Helper

Created on Thu Aug  2 22:51:46 2018

@author: Carissa Castro
"""

import csv
import os

# function to read all data from multiple csv files
def read_csv_inputs(inputs):
    list_of_files = []
    directory = os.fsencode(inputs)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            full_file_path = inputs + "\\" + filename
            list_of_files.append(full_file_path)
            continue
        else:
            continue
    return list_of_files
    

# function to copy all rows from a csv file into an array
def copy_all_rows(file_path):
    # Empty array to hold data from each row of a csv file
    csv_data = []
    
    # Open csv and read each row  
    full_path = os.path.abspath(file_path)    
    with open(full_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            csv_data.append(row)
    return csv_data

# helper function to write to a csv
def csv_writer(data, path):
    ###
    #
    # Write data to a CSV file path
    #
    ###
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

# function to copy data from list of input csv files into new single csv
def combine_csv_data(input_data, output_path):
    output = os.path.abspath(output_path)
    output = output + "\\output.csv"
    csv_writer(input_data, output)

# main function to call helper functions to combine csv data into "output.csv"        
def batch_copy(array_of_inputs, output):
    inputs_array = read_csv_inputs(array_of_inputs)
    total_data = []   
    for csv_file in inputs_array:
        data = copy_all_rows(csv_file)
        for row in data:
            total_data.append(row)
    combine_csv_data(total_data, output)
