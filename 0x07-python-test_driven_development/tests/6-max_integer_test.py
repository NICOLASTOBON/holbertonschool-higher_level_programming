#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test integers """

    def test_max_integer(self):
        """ test integers """

        self.assertEqual(max_integer([1, 9, 8, 0]), 9)
        self.assertEqual(max_integer([11, -9, 8, 0]), 11)
        self.assertEqual(max_integer([-1, -9, -8, 0]), 0)
        self.assertEqual(max_integer([1, 9, 22, 0]), 22)
        self.assertEqual(max_integer([1, 9, 8, 10]), 10)
        self.assertEqual(max_integer([1.2, 9.2, 3, 0]), 9.2)
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
