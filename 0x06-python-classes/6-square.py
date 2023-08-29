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
        size : the square sides; privatei
        position: the position
    Functions:
        area(self)
        __init__(self, size=0, position=(0,0))
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes the square
        Attributes:
            size : the int side
            position : the position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        getter
        Returns:
            the position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        sets the position of the square
        Arguments:
            value : the coordinates
        """
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or type(value[1]) \
           is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive \
                            integers")
        else:
            self.__position = value

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
        else:

            for p in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
