#!/usr/bin/python3
"""Defines class rectangle"""


class Rectangle:
    """Represent a rectagle."""
    def __init__(self, width=0, height=0):
        """
        Inicializes new rectagle
        Args:
        width (int):the new rectangle
        height (int):of the new rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """return heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """return width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
