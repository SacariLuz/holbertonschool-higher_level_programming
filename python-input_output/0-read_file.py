#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """print the contents of text file"""
    with open (filename) as f:
        txt = f.read()
        print(txt, end="")
