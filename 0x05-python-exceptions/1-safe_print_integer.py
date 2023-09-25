#!/usr/bin/python3
# 1-safe_print_integer.py


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Parameter:
        value (int): The integer to print.
    Return:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
