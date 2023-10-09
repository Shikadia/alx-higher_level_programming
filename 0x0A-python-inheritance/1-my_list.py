#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyList that inherits from list (a built-in class)."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
