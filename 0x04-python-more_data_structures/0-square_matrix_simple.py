#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for idx in matrix:
        new_matrix.append(list(map(lambda x: x*x, idx)))
    return new_matrix
