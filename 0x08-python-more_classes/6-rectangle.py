#!/us /bin/python3
"""
Module 6-rectangle
defines rectangle class wih private
instance attribute width and height
arg:
    width: int
    height: int
    number_of_instnaces:int

Methods:
    area(self) gets area
    perimeter(self) gets perimeter
    width(self, value)
    width(self)
    height(self)
    height(self, value)
    __str__(self)
    __repr__(self)
    __del__(self)


"""


class Rectangle:

    """
    square class definition

    Args:
        size : square side length
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        rectangle initialization

        Attributes:
            size : the rectangel side
            width: the width
        """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        args:
            value: an int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        args:
            value: the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ finds and returns rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """finds and returns rectanle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """prints string equivalent of rectangle with #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = "\n".join(["#" * self.__width for rows in
                              range(self.__height)])
            return rect

    def __repr__(self):
        """
        return a string representation of the rectangle to be able to
        recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """detects rectangle instance deletion"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
