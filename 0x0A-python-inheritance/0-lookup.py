#!/usr/bin/python3
"""
module 0-lookup
returns list of attributes and
methods in an object
"""


def lookup(obj):
    """
    returns list of attributes
    """
    attributes = dir(obj)

    return (attributes)
