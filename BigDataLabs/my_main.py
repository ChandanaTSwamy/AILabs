# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

import sys


# import codecs

# ------------------------------------------
# 1. FUNCTION parse_in
# ------------------------------------------
def parse_in(input_file_name):
    matrix = []

    with open(input_file_name) as farr:
        rows_cols = farr.readline()

        num_rows = int(rows_cols.split()[0])
        num_cols = int(rows_cols.split()[1])
        print('No.of rows: ', num_rows)
        print('No.of rows: ', num_cols)

        for i in range(num_rows):
            larr = farr.readline()
            # print(larr.split())
            # splittxt = larr.split()
            matrix.append(larr.split())

        print('Printing matrix: \n', matrix)


    return (num_rows, num_cols, matrix)


# ------------------------------------------
# 2. FUNCTION parse_out
# ------------------------------------------
def parse_out(output_file_name, num_rows, num_columns, sol_matrix):
    pass


# ------------------------------------------
# 3. FUNCTION solve
# ------------------------------------------
def solve(num_rows, num_columns, matrix):
    pass


# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------

def my_main(input_file_name, output_file_name):
    # 1. We do the parseIn from the input file
    (num_rows, num_columns, matrix) = parse_in(input_file_name)

    print('Inside main: printing rows', num_rows, '; cols: ', num_columns)

    x = 2

    # 2. We do the strategy to solve the problem
    # sol_matrix = solve(num_rows, num_columns, matrix)

    # 3. We do the parse out to the output file
    # parse_out(output_file_name, num_rows, num_columns, sol_matrix)


# --------------------------------------------------------
#
# PYTHON PROGRAM EXECUTION
#
# Once our computer has finished processing the PYTHON PROGRAM DEFINITION section its knowledge is set.
# Now its time to apply this knowledge.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer finally processes this PYTHON PROGRAM EXECUTION section, which:
# (i) Specifies the function F to be executed.
# (ii) Define any input parameter such this function F has to be called with.
#
# --------------------------------------------------------
if __name__ == '__main__':
    # 1. We use as many input arguments as needed
    input_file_name = "C:/Users/R00225087/PycharmProjects/BigDataLabs/input_files/input_1.txt"
    output_file_name = "C:/Users/R00225087/PycharmProjects/BigDataLabs/results/output.txt"

    if (len(sys.argv) > 1):
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]

    # 2. We solve the problem
    my_main(input_file_name, output_file_name)
