#!/usr/bin/python3

"""define a class square."""


class Square:
    """represent square."""

    def __init__(self, size=0):
        """represnt square."""
        self.size = size

    def area(self):
        """returns the area of a square."""
        return (self._size * self._size)

    @property
    def size(self):
        """returns the size."""
        return self._size

    @size.setter
    def size(self, value):
        """function the value of size."""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
