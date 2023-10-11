#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-to-object(Python data structure) function"""
import json


def from_json_string(my_str):
    """Returns python data structure from JSON string

    Args:
        my_str: json string representation
    Return:
        python object
    """
    return json.loads(my_str)
