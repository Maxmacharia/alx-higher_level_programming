#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in matrix:
        squared.append([j ** 2 for j in i])
    return squared
