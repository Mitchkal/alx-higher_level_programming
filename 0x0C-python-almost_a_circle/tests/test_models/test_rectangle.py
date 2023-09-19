#!/usr/bin/python3
""" test module
for python almost a circle
"""


import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO
import pep8
import os


class Test_format(unittest.TestCase):
    """Tests the pep8 style formatting"""
    def test_pep(self):
        """test Pep-8"""
        pep_style = pep8.StyleGuide(quiet=False)
        fails = 0
        inputs = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        fails += pep_style.check_files(inputs).total_errors
        self.assertEqual(fails, 0, 'Need to fix Pep8')


class TestObjects(unittest.TestCase):
    """
    A class of testcases for
    class rectangle
    """

    def test_class_attributes(self):
        """tests class attributes"""
        r = Rectangle(10, 20, 5, 5, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 1)

    def test_width_setter(self):
        """tests width setter"""
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height_setter(self):
        """tests height setter"""
        r = Rectangle(10, 20)
        r.height = 40
        self.assertEqual(r.height, 40)

    def test_x_setter(self):
        """tests x setter"""
        r = Rectangle(10, 20)
        r.x = 6
        self.assertEqual(r.x, 6)

    def test_y_setter(self):
        """tests y setter"""
        r = Rectangle(10, 20)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_width_height(self):
        """tests width and height validation"""
        r = Rectangle(10, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = 'z'
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -1
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = '2'
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -1
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0

    def test_x_y(self):
        """tests coordinate validation"""
        r = Rectangle(10, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = 'a'
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = 'b'
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -2

    def test_correct_class(self):
        """verifies the correct class"""
        self.assertEqual(type(Rectangle(3, 4)), Rectangle)

    def test_area(self):
        """tests correct area"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_access(self):
        """ensures unaccessibility of private attributes"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__y)
            print(Rectangle.__x)
            print(Rectangle.__width)
            print(Rectangle.__height)

    def test_insufficient_args(self):
        """tests for coorect argument nos"""
        with self.assertRaises(TypeError):
            r2 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)
            r2 = Rectangle(None)

    def test_display(self):
        """tests display"""
        r = Rectangle(4, 6)

        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(output, expected_output)

    def test_display_coordinates(self):
        """tests display with coordinates"""
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)

    def test_string(self):
        """tests string equivalent"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        output = str(r1)
        self.assertEqual(output, expected_output)

    def test_update_args(self):
        """tests argument update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        expected_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r1), expected_output)
        r1.update(89, 2)
        expected_output2 = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r1), expected_output2)
        r1.update(89, 2, 3)
        expected_output3 = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r1), expected_output3)
        r1.update(89, 2, 3, 4)
        expected_output4 = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r1), expected_output4)
        r1.update(89, 2, 3, 4, 5)
        expected_output5 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r1), expected_output5)

    def test_update_args(self):
        """"tests args and kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        expected_outputs = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(str(r1), expected_outputs)
        r1.update(height=1)
        expected_output = "[Rectangle] (10) 10/10 - 10/1"
        self.assertEqual(str(r1), expected_output)
        r1.update(width=1, x=2)
        expected_output2 = "[Rectangle] (10) 2/10 - 1/1"
        self.assertEqual(str(r1), expected_output2)
        r1.update(y=1, width=2, x=3, id=89)
        expected_output3 = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r1), expected_output3)
        r1.update(x=1, height=2, y=3, width=4)
        expected_output4 = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(r1), expected_output4)

    def test_dictionary(self):
        """tests to dictionary method"""
        dic = Rectangle(4, 6, 2, 1, 12).to_dictionary()
        self.assertEqual(type(dic), dict)
        r1 = Rectangle(8, 3, 0, 0)
        r1.update(**dic)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')


if __name__ == '__main__':
    unittest.main()
