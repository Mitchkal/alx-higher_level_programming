#!/usr/bin/python3
"""module 101-add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    """checks if possible to add attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr_name] = attr_value
