#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
            print("{:d}".format(matrix[x][j]), end="")
            if j != (len(matrix[x]) - 1):
                print(" ", end="")

        print("")
