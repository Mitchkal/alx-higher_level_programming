#!/usr/bin/python3
"""module 4-inherits_from"""


def inherits_from(obj, a_class):
    """returns true or false in chechking
    for inheritance
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
