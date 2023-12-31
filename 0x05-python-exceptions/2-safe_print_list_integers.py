#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Parameters:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Return: The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            pass
    print()
    return (ret)
