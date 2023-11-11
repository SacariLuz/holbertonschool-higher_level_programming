#!/usr/bin/python3
"""
Definines class of the class BaseGeometry
"""


"""Import the class BaseGeometry modul 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Representation of clase"""
    def __init__(self, width, height):
        """Defines a metod init e initialize
        atributes

        Args:
        width(int) of rectangle
        height(largo) of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """the function area 

        Return:
            int: ancho * alto
        """
        return self.__height * self.__width

    def __str__(self):
        """returns the class 

        Return:
            String: Represent 
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
