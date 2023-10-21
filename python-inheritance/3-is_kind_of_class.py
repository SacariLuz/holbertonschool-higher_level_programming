#!/usr/bin/python3
"""
defines a class and inherited class checking function
"""


def is_kind_of_class(obj, a_class):
    """
    function checks an object is an instance or inherited instance of class

    Args:
    obj: the object to check
    Returns:
    if obj is an instance, false otherwise
    """
    return isinstance(obj, a_class)
