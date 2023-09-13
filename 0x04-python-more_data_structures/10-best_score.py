#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if a_dictionary is None:
        return None

    big_value = None
    for i in a_dictionary:
        big_value = i if big_value is None else big_value
        if a_dictionary[i] > a_dictionary[big_value]:
            big_value = i
    return big_value
