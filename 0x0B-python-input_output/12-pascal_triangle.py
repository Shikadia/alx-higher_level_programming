#!/usr/bin/python3
# 14-pascal_triangle.py
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        current_row = triangle[-1]
        tmp_list = [1]
        for i in range(len(current_row) - 1):
            tmp_list.append(current_row[i] + current_row[i + 1])
        tmp_list.append(1)
        triangle.append(tmp_list)
    return triangle
