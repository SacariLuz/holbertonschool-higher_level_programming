#!/usr/bin/python3


"""define class square"""


class Square:
    """ represent a square."""

    def __init__(self, size=0):
        """inizialite a new square."""
        if type(size) == int:
            if size >= 0:
                self._size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """return the current area of the square."""
        return (self._size * self._size)
