#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Checks if an object is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """A function that checks an object.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an instance or inherited instance of a class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
