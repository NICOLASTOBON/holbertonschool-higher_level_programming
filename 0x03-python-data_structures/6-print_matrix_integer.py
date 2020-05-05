#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        column = " ".join("{:d}".format(column) for column in row)
        print(column)
