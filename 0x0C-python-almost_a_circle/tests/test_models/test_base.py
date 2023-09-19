#!/usr/bin/python3
"""module test_base
tests the base_class
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import pep8


class Test_format(unittest.TestCase):
    """
    Tests the pep8 style formatting
    """
    def test_pep(self):
        """test Pep-8"""
        pep_style = pep8.StyleGuide(quiet=False)
        fails = 0
        inputs = ["models/base.py", "tests/test_models/test_base.py"]
        fails += pep_style.check_files(inputs).total_errors
        self.assertEqual(fails, 0, 'Need to fix Pep8')


class Testbase(unittest.TestCase):
    """the test class"""
    def test_id(self):
        """test given and increment id"""
        self.assertTrue(Base(10), self.id == 10)
        self.assertTrue(Base(-1), self.id == -1)
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_access(self):
        """tests for private access"""
        with self.assertRaises(AttributeError):
            print(Base.nb_objects)
            print(Base.nb__objects)

    def test_invalids(self):
        """tests for invalid args"""
        with self.assertRaises(TypeError):
            Base(20, 20)

    def test_class(self):
        """teststhe class"""
        self.assertTrue(Base(10), self.__class__ == Base)

    def _json_string(self):
        """
        Test non, empty dict,
        given dict
        """
        d0 = None
        strd1 = Base.to_json_string([d0])
        self.assertTrue(type(strd1) == str)
        self.assertTrue(strd1, "[]")

        d1 = dict()
        strd2 = Base.to_json_string([d1])
        self.assertTrue(len(d1) == 0)
        self.assertTrue(type(strd2) == str)
        self.assertTrue(strd2, "[]")

        d2 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d3 = {"id": 2, "width": 4, "height": 6, "x": 8, "y": 10}
        strd3 = Base.to_json_string([d2, d3])
        self.assertTrue(type(d2) == dict)
        self.assertTrue(type(strd3) == str)
        self.assertTrue(strd3,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 2, "width": 4, "height": 6, "x": 8, "y": 10}])

    def test_create(self):
        """
        Validates creation of object
        from dictionary attrs
        """
        r1 = Rectangle(6, 10, 1, 2, 95)
        rdic = r1.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r1), '[Rectangle] (95) 1/2 - 6/10')
        self.assertEqual(str(r2), '[Rectangle] (95) 1/2 - 6/10')
        self.assertIsNot(r1, r2)

    def test_from_json_string(self):
        """
        validates  JSON string convesion
        to dictionary
        """
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}])
        self.assertTrue(strs0[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_save_to_file(self):
        """
        validate saving to json file for
        empty list, None, list
        """
        r1 = Rectangle(9, 5, 2, 8, 97)
        r2 = Rectangle(3, 6, 2, 2, 95)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                f.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_load_from_file(self):
        """
        Validates attribute loading
        load from file, none file, and empty file
        """
        r1 = Rectangle(9, 5, 2, 8, 97)
        r2 = Rectangle(3, 6, 2, 2, 95)
        Rectangle.save_to_file([r1, r2])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 2)

        for key, value in enumerate(rects):
            if key == 0:
                self.assertEqual(str(value), '[Rectangle] (97) 2/8 - 9/5')
            if key == 1:
                self.assertEqual(str(value), '[Rectangle] (95) 2/2 - 3/6')

        rects = Rectangle.load_from_file()
        self.assertEqual(type(rects), list)
        self.assertEqual(len(rects), 2)

        Rectangle.save_to_file([])
        rects = Rectangle.load_from_file()
        self.assertEqual(type(rects), list)
        self.assertEqual(len(rects), 0)
