#!/usr/bin/python3
# 7-base_geometry.py
"""Defines a class BaseGeometry based on 6-base_geometry.py."""


class BaseGeometry:
    """Represent the base geometry."""

    def area(self):
        """Raise exception for area not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
