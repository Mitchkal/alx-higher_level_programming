#!/usr/bin/python3
""" test module
for python almost a circle
"""


import unittest
from models.square import Square
import sys
from io import StringIO
import pep8
import os


class Test_format(unittest.TestCase):
    """Tests the pep8 style formatting"""
    def test_pep(self):
        """totest Pep-8"""
        pep_style = pep8.StyleGuide(quiet=False)
        fails = 0
        inputs = ["models/square.py", "tests/test_models/test_square.py"]
        fails += pep_style.check_files(inputs).total_errors
        self.assertEqual(fails, 0, 'Need to fix Pep8')


class TestObjects(unittest.TestCase):
    """
    A class of testcases for
    class square
    """

    def test_class_attributes(self):
        """tests class attributes"""
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_width_setter(self):
        """tests width setter"""
        r = Square(10)
        r.width = 30
        self.assertEqual(r.width, 30)
        self.assertEqual(r.size, 30)

    def test_height_setter(self):
        """tests height setter"""
        r = Square(10)
        r.height = 40
        self.assertEqual(r.height, 40)
        self.assertEqual(r.size, 10)

    def test_x_setter(self):
        """tests x setter"""
        r = Square(10)
        r.x = 6
        self.assertEqual(r.x, 6)

    def test_y_setter(self):
        """tests y setter"""
        r = Square(10)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_width(self):
        """tests width validation"""
        r = Square(10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = 'z'
            Square("1")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -1
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0
            Square(0)
            Square(-1)

    def test_x_y(self):
        """tests coordinate validation"""
        r = Square(10, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = 'a'
            Square(1, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -1
            Square(1, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -2
            Square(1, 2, -3)

    def test_correct_class(self):
        """verifies the correct class"""
        self.assertEqual(type(Square(4)), Square)

    def test_area(self):
        """tests correct area"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(8, 0, 0).area(), 64)

    def test_access(self):
        """ensures unaccessibility of private attributes"""
        with self.assertRaises(AttributeError):
            print(Square.__y)
            print(Square.__x)
            print(Square.__width)

    def test_insufficient_args(self):
        """tests for coorect argument nos"""
        with self.assertRaises(TypeError):
            r2 = Square()
        with self.assertRaises(TypeError):
            r2 = Square(None)

    def test_display(self):
        """tests display"""
        r = Square(4)

        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = "####\n####\n####\n####\n"
        self.assertEqual(output, expected_output)

    def test_display_coordinates(self):
        """tests display with coordinates"""
        r1 = Square(2, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = "\n\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)

    def test_str(self):
        """tests __str__  equivalent"""
        r1 = Square(1, 2, 3, 44)
        r1.size = 16
        expected_output = "[Square] (44) 2/3 - 16"
        output = str(r1)
        self.assertEqual(output, expected_output)

    def test_update_args(self):
        """tests argument update"""
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        expected_output = "[Square] (89) 10/10 - 10"
        self.assertEqual(str(r1), expected_output)
        r1.update(89, 2)
        expected_output2 = "[Square] (89) 10/10 - 2"
        self.assertEqual(str(r1), expected_output2)
        r1.update(89, 2, 3)
        expected_output3 = "[Square] (89) 3/10 - 2"
        self.assertEqual(str(r1), expected_output3)
        r1.update(89, 2, 3, 4)
        expected_output4 = "[Square] (89) 3/4 - 2"
        self.assertEqual(str(r1), expected_output4)

    def test_update_args(self):
        """"tests args and kwargs"""
        r1 = Square(10, 10, 10, 10)
        expected_outputs = "[Square] (10) 10/10 - 10"
        self.assertEqual(str(r1), expected_outputs)
        r1.update(height=1)
        expected_output = "[Square] (10) 10/10 - 10"
        self.assertEqual(str(r1), expected_output)
        r1.update(width=1, x=2)
        expected_output2 = "[Square] (10) 2/10 - 1"
        self.assertEqual(str(r1), expected_output2)
        r1.update(y=1, width=2, x=3, id=89)
        expected_output3 = "[Square] (89) 3/1 - 2"
        self.assertEqual(str(r1), expected_output3)
        r1.update(x=1, height=2, y=3, width=4)
        expected_output4 = "[Square] (89) 1/3 - 4"
        self.assertEqual(str(r1), expected_output4)

    def test_to_dictionary(self):
        """tests to_dictionary method"""
        dic = Square(2, 4, 6, 8).to_dictionary()
        self.assertEqual(type(dic), dict)
        s1 = Square(10, 10)
        s1.update(**dic)
        self.assertEqual(str(s1), '[Square] (8) 4/6 - 2')


if __name__ == '__main__':
    unittest.main()
