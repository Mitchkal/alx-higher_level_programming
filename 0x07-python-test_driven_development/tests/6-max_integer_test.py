#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """tests max_integer"""
    def test_module_docstring(self):
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 1)

    def test_function_docstring(self):
        func_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(func_doc) > 1)

    def test_types(self):
        """confirm type errors"""
        self.assertRaises(TypeError, max_integer, 10)
        self.assertRaises(TypeError, max_integer, [{'n': 'T', 'a': 2}, 5])
        self.assertRaises(KeyError, max_integer, {'na': 'Tom', 'age': 20})
        with self.assertRaises(TypeError):
            max_integer([1, 2], [3, 4])
        with self.assertRaises(TypeError):
            max_integer([False, None])
        with self.assertRaises(TypeError):
            max_integer([5, "str"], None)

    def test_max(self):
        """comfirms valueerrors"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -5, -2, -4]), -1)
        self.assertEqual(max_integer([-1, 5, -2, 3]), 5)
        self.assertEqual(max_integer([5, 5, 3, 2, 1]), 5)
        self.asserEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([1.1, 1.2, 3.1, 4.2]), 4.2)
        self.assertEqual(max_integer([1, 2, '6', 4.0]), 4.0)
        self .asertEqual(max_integer([i for i in range(10**6)]), 999999)
        self.assertEqual(max_integer([1, 2, -float('inf'), 3, 4]), 4)
        self.assertEqual(max_integer("1234"), '4')
        self.assertEqual(max_integer("abcd"), 'd')
        self.assertEqual(max_integer(["1234", 'z']), '4')
        self.assertEqual(max_integer(["abcd", 'z'], 'z'))

        def test_lists(self):
            self.AsserEqual(max_integer(['name', 'banana']), 'name')

    if __name__ == "__main__":
        unittest.main()
