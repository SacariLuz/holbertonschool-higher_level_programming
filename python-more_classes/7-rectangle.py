#!/usr/bin/python3
"""Defines a Rectangle a class"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Inicialize a new rectangle

        Args:
            width(int)is width of the new rectangle
            height(int)is height of the new rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Set the width of rectangle

        Return:
            int:return the height
        """
        return self.__width

    @width.setter
    def width(self, value):
        """define call of wdth
        Args:
            value(int): value set width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of rectangle

        Return:
            int: return the hight
        """
        return self.__height

    @height.setter
    def height(self, value):
        """defines call of height

        Args:
            value(int): value set height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle

        Return:
            int:height * wight
        """
        return self.__height * self.__width

    def perimeter(self):
        """return the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        represent string the rectangle.
        Return:
            str: return the rectangle#
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            a = self.__height + 1
            b = self.__width
            str_repr = ''.join(
                [f"{str(self.print_symbol) * b}\n" for i in range(a) if i])
            return str_repr[:len(str_repr) - 1]

    def __repr__(self):
        """
        return the string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        print a message for delete of rectangle
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
