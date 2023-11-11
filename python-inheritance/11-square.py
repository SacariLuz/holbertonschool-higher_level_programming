#!/usr/bin/python3
"""
Defines a square class that inherits of class rectangle
"""


"""Import of the class Rectangle of modul 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsentación de la clase"""
    def __init__(self, size):
        """Define the init method and initialize atributes
        Args:
            size(int): ofSquare
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """This function calculates the area of the square
        Return:
            int: size ** 2
        """
        return self.__size ** 2

    def __str__(self):
        """method returns a text string of the class

        Return:
            string: representation ifromal
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
