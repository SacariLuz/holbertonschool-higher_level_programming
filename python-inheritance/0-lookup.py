#!/usr/bin/python3

"""Define object attribute lookup function"""

def lookup(obj):
    """
    Return a list of an object

    Args: obj

    Return: list
    """
    return dir(obj)
