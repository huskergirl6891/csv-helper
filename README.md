# csv-helper

# Overview
Use this CSV helper script to easily manipulate CSV files.  The main script is csv-helper.py and it can be used as a library with other customized scripts.  An example custom script with a use case is included (read_TM_logs.py) as well.  See below for details on the use case.

# Main functions
The main function in the csv-helper is batch_copy which takes an array of input csv files and combines the contents of each csv file into a single csv file called "output.csv".  The batch_copy file has several arguments:
* array_of_inputs : this should be the path name of a folder that contains all of the csv files to be copied/combined
* output : this should be the path name of the desired destination of the combined output file
* start_row : optional argument for desired starting row to copy. To include everything, either enter no arg or enter 1 (i.e. to start at the first row). To ignore the first row and start at the second row, enter 2. The helper function subtracts one to account for Python starting loop iteration at 0.
* insert_value_array : optional argument; pass in an array of data to be added to each row. The first item in the array is added to each row in the first file, the second item in the array is added to each row in the second file, etc.

# Example Use
An example script (read_TM_logs.py) is included to demonstrate how the csv-helper library can be used.  This script can be called from the command line like this:

`python C:/directory_path/read_TM_logs.py C:/path_to_csv_folder 2`

The third argument is the full path to the folder where the CSV files are located to be combined.  In this example, the same folder is used for the output as well.  The last argument is the starting row to be copied in each CSV, and is optional.

