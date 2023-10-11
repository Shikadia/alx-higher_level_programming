#!/usr/bin/python3
# 1-write_file.py
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Return:
           The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
