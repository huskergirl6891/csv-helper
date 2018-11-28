# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:06:18 2018

@author: Carissa Castro
"""

import csv_helper
import os
import sys



temp = sys.argv[1]
test = os.path.abspath(temp)

# check for optional input for starting row
try:
    start_row_input = int(sys.argv[2]) - 1
except:
    start_row_input = 0
    
# check for optional input for extra value to be added to each row
try:
    value = sys.argv[3]
except:
    #value = ["a", "b"]
    # read input files to save time/date data from file name to be
    # inserted in each row
    inputs_array = csv_helper.read_csv_inputs(test)

    data_to_add = []
    for row in inputs_array:
        filename = row.split('_')
        date = filename[7]
        time = filename[8].split('.')[0]   
        data_to_add.append(date)
        
    value = data_to_add



csv_helper.batch_copy(test, test, start_row_input, value)