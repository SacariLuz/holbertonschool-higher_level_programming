#!/usr/bin/python3
"""function checks the object is an instance"""


def is_same_class(obj, a_class):
    """
    define function that takes 2 argument
    data type is concret.

    Args: obj is object checks
    Return: return true if obj belong the data type a class
    otherwise false
    """
    return type(obj) == a_class
