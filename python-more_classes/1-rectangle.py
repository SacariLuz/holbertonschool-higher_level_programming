#!/usr/bin/python3
"""Este módulo define la clase Rectangle."""


class Rectangle:
    """Esta clase expone un Rectangle."""

    def __init__(self, width=0, height=0):
        """Inicialize new rectangle, 2 optional parameters.

        Args:
            width (int): width of Rectangle.
            height (int): height of Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return height of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
