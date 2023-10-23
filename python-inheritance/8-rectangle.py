#!/usr/bin/python3
"""defines a class rectangle inherites from class base grometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import the class base geometry of module 7-base_geometry"""


class Rectangle(BaseGeometry):
    """ Represent the class"""
    def __init__(self, width, height):
        """
        Define the method int and inicialize attibute

        Args:
        width(int) of rectangle
        height(largo) of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
