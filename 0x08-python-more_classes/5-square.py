#!/usr/bin/python3
"""
module 4-square
square class with access and
private attribute
"""


class Square:
    """
    the Square class
    Attibutes:
        size : the square sides; private
    Functions:
        area(self)
        __init__(self, size=0)
    """
    def __init__(self, size=0):
        """
        initializes the square
        Attributes:
            size : the int side
        """
        self.size = size

    @property
    def size(self):
        """
        the getter
        Returns:
            the instance
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets square property
        Arguments:
            value : the int value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        method to get area
        Return:
           the area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints the square with #
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
