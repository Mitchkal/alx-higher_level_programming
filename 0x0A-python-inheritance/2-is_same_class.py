#!/usr/bin/python3
"""
module 2-is_same_class
functions:
    is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """checks if object is exact class instance"""
    if type(obj) == a_class:
        return True
    return False
