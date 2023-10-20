#!/usr/bin/python3
"""Defines write_file a function"""


def write_file(filename="", text=""):
    """Return the contents of text file"""
    with open(filename, "w") as f:
        f.write(text)
        return f.tell()
