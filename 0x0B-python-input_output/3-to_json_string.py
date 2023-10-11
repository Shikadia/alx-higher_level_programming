#!/usr/bin/python3
# 3-to_json_string.py
"""Defines an object(str)-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: python object
    Return:
        json string representation
    """
    return json.dumps(my_obj)
