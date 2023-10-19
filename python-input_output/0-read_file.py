#!/usr/bin/python3
"""Defines read_file a function"""


def read_file(filename=""):
    """Print the contents of text file"""
    with open(filename) as f:
        txt = f.read()
        print(txt, end="")
