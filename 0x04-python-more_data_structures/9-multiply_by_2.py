#!/usr/bin/python3
# 9-multiple_by_2.py


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    multiply_dict = {}
    for key, value in a_dictionary.items():
        multiply_dict[key] = value * 2
    return multiply_dict
