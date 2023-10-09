#!/usr/bin/python3
"""
represent Square
"""


class Square:
    """
    define a square.
    """

    def __init__(self, size=0):
        """
        This is inicialize a new square.

        Args:
            size (int): size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be a integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
