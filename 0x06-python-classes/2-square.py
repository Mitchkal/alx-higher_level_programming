#!/usr/bin/python3
"""
module 2-square
defines square class
"""


class Square:
    """
    square class
    Attributes:
        size  : square side
    """
    def __init__(self, size=0):
        """
        initializes the square class
        Arguments:
            size : the sde
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self .__size = size
