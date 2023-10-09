#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt that inherits from the int class."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Invert == opeartor to !="""
        return self.real != value

    def __ne__(self, value):
        """Invert != operator to =="""
        return self.real == value
