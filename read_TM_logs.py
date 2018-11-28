# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:06:18 2018

@author: Carissa Castro
"""

import csv_helper
import os
import sys

temp = sys.argv[1]
start_row_input = int(sys.argv[2])
print(start_row_input)
test = os.path.abspath(temp)
csv_helper.batch_copy(test, test, start_row_input)