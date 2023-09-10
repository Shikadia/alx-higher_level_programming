#!/usr/bin/python3


def no_c(my_string):
    _str = f""
    for i in my_string:
        if i != 'c' and i != 'C':
            _str += f"{i}"
    return _str
