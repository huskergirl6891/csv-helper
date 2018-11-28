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
            if filename != "output.csv":
                full_file_path = inputs + "\\" + filename
                list_of_files.append(full_file_path)
            continue
        else:
            continue
    return list_of_files
    

# function to copy all rows from a csv file into an array
def copy_rows(file_path, start_row, insert_value):
    # Empty array to hold data from each row of a csv file
    csv_data = []
    # Opens each csv file and reads each line.  Optional user
    # input for start_row is passed into this function. To 
    # include everything, either enter no arg or enter 1 
    # (i.e. to start at the first row). To ignore the first row 
    # and start at the second row, enter 2. The helper function 
    # subtracts one to account for Python starting loop 
    # iteration at 0.
    full_path = os.path.abspath(file_path)    
    with open(full_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        idx = 0
        for idx, row in enumerate(reader):
            if idx >= start_row:
                if insert_value != "":
                    row.append(insert_value)
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
def batch_copy(array_of_inputs, output, start_row=0, insert_value_array=""):
    inputs_array = read_csv_inputs(array_of_inputs)
    print(insert_value_array)
    total_data = []   
    for num, csv_file in enumerate(inputs_array):
        # check if no input was given to be added to each row
        if insert_value_array == "":
            insert_value = ""
        else:
            # use the value from each item in the input array
            # to insert into each file
            try:
                insert_value = insert_value_array[num]
            except:
                insert_value = ""
        data = copy_rows(csv_file, start_row, insert_value)
        for row in data:
            total_data.append(row)
    combine_csv_data(total_data, output)
