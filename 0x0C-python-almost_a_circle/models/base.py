#!/usr/bin/python3
"""
module base
contains class BaSE
"""

import json
import os
import turtle
import csv


class Base:
    """
    private class attribute __nb_objects = 0
    constructor: def__init__(self, id = None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returnsJSON string rep of list_dictionaries
        first checks if list_dictionaries is none/empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes Json string of list_objs to file"""
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"

        with open(file_name, 'w') as f:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_list)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            json_list = []
            return json_list
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """createand eturn instance with attributes from dict"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loadinstances from json file and return
        list of instances
        """
        file_name = cls.__name__ + ".json"

        if not os.path.isfile(file_name):
            return []

        with open(file_name, 'r') as f:
            json_string = f.read()

        json_list = cls.from_json_string(json_string)
        instances = [cls.create(**dict_data) for dict_data in json_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes objects to CSV"""
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".csv"

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                data = obj.to_csv_row()
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize objects from csv file"""
        file_name = cls.__name__ + ".csv"
        instances = []

        try:
            with open(file_name, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    obj_data = cls.from_csv_row(row)
                    instances.append(obj_data)

        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the list of recs and squares"""
        screen = turtle.Screen()
        screen.title("drawing the rectangles and squares")

        c = turtle.Turtle()

        def draw_rectangle(rectangle):
            """draws the rectangle"""
            c.penup()
            c.goto(rectangle.x, rectangle.y)
            c.pendown()
            c.forward(rectangle.width)
            c.left(90)
            c.forward(rectangle.height)
            c.left(90)
            c.forward(rectangle.width)
            c.left(90)
            c.forward(rectangle.height)
            c.left(90)
            c.penup()

        def draw_square(square):
            """draws the square"""
            c.penup()
            c.goto(square.x, square.y)
            c.pendown()
            for i in range(4):
                c.forward(square.size)
                c.left(90)
            c.penup()

        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        for square in list_squares:
            draw_square(square)

        screen.exitonclick()
