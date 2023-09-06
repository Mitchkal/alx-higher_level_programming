#!/usr/bin/python3
"""
module 0-add_integer.py
method Adds two integers
"""


def add_integer(a, b=98):
    """
    returns a + b as integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
