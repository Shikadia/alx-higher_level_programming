#!/usr/bin/python3
# 5-save_to_json_file.py
"""A function that writes an Obj to a textfile using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON representation

    Args:
        my_obj: python object
        filename: file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
