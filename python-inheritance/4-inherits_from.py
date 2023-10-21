#!/usr/bin/python3
"""
defines function to validate the instance
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class.

    Args:
    ibj: the object a validate
    a_class: the class to match the type of obj to
    Returns:
    bool: true, false otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
