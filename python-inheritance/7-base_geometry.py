#!/usr/bin/python3

"""Defines a base geometry class"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """function an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        valide a parameter as integer

        Args:
        name (str): The name of the parameter
        value (int): The parameter to validate

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
