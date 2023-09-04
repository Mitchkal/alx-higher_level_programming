#!/usr/bin/python3
"""
module 3-square
square class with public instance
method area
"""


class Square:
    """
    defines the square
    Attributes:
        size : the square side
    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initializes the square sides
        Arguments:
            size: the side int initialized
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the square area
        Returns:
            the area
        """
        return (self.__size)**2
