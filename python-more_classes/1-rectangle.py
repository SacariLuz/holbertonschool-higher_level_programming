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
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """get height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
