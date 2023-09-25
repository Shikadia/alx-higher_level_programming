#!/usr/bin/python3
# 101-safe_function.py

from sys import stderr


def safe_function(fct, *args):
    """Executes a function safely.

    Parameters:
        fct: The function to execute.
        args: Arguments of fct function.

    Return:
        If an error occurs - None.
        Otherwise - the result of the function.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return (None)
