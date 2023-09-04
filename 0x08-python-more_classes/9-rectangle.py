#!/us /bin/python3
"""
Module 9-rectangle
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
    square(cls, size=0)
    ststic method:
         bigger_or_equal(rect_1, rect_2)


"""


class Rectangle:

    """
    square class definition

    Args:
        size : square side length
    """
    number_of_instances = 0
    print_symbol = "#"

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
            rect = "\n".join([str(self.print_symbol) * self.__width for rows in
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """returns rectangle with width =height= size"""
        return cls(size, size)
