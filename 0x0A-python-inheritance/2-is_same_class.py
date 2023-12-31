#!/usr/bin/python3

"""
Module: 2-is_same_class

Contains a function that checks if an object is exactly an
instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class;
        False otherwise.
    """
    return type(obj) is a_class
