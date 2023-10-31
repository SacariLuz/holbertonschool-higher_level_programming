#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student

        Args:
        first_name (str): the first name of the student
        last_name (str): the last name of the student
        age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get/set a dictionary representation of student
        Args:
            attrs (list):the attributes represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
