#!/usr/bin/python3
"""
module rectangele
contains class rectangle that
inherits from base
"""


from models.base import Base


class Rectangle(Base):
    """
    inherits from base
    private instance attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    constructor:
        def __init__(self, width, height, x, u, id)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes the class
        variables:
            width(int)
            height(int)
            x(int) x coordinate
            y(int) y coordinate
            id - the id of the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the y coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle with #"""
        if self.__y > 0:
            print("\n" * (self.__y - 1))

        for i in range(self.__height):
            print(' ' * self.__x + "\n".join(["#" * self.__width]))

    def __str__(self):
        """overides __str__ to retrun rectangle details"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """
        assigns argument to object attributes
        with key value pairs
        Kwargs is skipped if *args exists and is not empty
        """
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attribute_names[i], value)
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)
                    else:
                        raise AttributeError("'{}' lacks attribute '{}'".
                                             format(type(self).__name__, key))

    def to_dictionary(self):
        """
        returns dictionary representation
        of Rectangle
        """
        _dict = {}
        for attr_name in ["id", "width", "height", "x", "y"]:
            _dict[attr_name] = getattr(self, attr_name)
        return _dict
