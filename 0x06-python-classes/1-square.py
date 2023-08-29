#!/usr/bin/python3
"""
Module 1-square
defines Square class wih private
instance attribute size
"""


class Square:

    """
    square class definition

    Args:
        size : square side length
    """
    def __init__(self, size):
        """
        square initialization

        Attributes:
            size : the square side
        """
        self.__size = size
