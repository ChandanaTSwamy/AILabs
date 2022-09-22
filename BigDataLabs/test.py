

matrix = []


with open('C:/Users/R00225087/PycharmProjects/BigDataLabs/input_files/input_1.txt') as farr:
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
