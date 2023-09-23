#!/usr/bin/python3
"""
module square
Class square inheritingfrom Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    grandchild of base
    methods:
        def __init__(self, size, x=0, y=0, id=None)
        __str__
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializes class square"""
        super().__init__(size, size, x, y, id)

    def to_csv_row(self):
        """serializes attributes to csv"""
        return [str(self.id), str(self.size), str(self.x),
                str(self.y)]

    @classmethod
    def from_csv_row(cls, csv_row):
        """deserializes csv to instances"""
        if len(csv_row) != 4:
            raise ValueError("CSV row should contain 4 values")
        obj_id, size, x, y = map(int, csv_row)
        return cls(size, x, y, obj_id)

    @property
    def size(self):
        """gets thesquare size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the square sides"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes to square"""
        if args:
            attribute_names = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attribute_names[i], value)
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)
                    else:
                        raise AttributeError("'{}' lacks attribute '{}'".
                                             format(type(self).__name__, key))

    def to_dictionary(self):
        """returns dictionary representation of square"""
        _dict = {}
        for attr_name in ["id", "size", "x", "y"]:
            _dict[attr_name] = getattr(self, attr_name)
        return _dict

    def __str__(self):
        """overrides str method of rectangle"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))
