#!/usr/bin/python3
"""
Defines MyList
hereda de la clase list
"""


class MyList(list):
    """
    class toma funcionalidad heredando de list
    """
    def print_sorted(self):
        """
        The metod created sorted
        """
        print(sorted(self))

    def __repr__(self):
        """
        the method return with string

        Return:
            list (list): return representation the list
        """
        return f"{list(self)}"
