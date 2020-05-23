#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test integers """

    def test_integer(self):
        """ test integers """
        self.assertEqual(max_integer([1, 9, 8, 0]), 9)
        self.assertEqual(max_integer([11, -9, 8, 0]), 11)
        self.assertEqual(max_integer([-1, -9, -8, 0]), 0)
        self.assertEqual(max_integer([1, 9, 22, 0]), 22)
        self.assertEqual(max_integer([1, 9, 8, 10]), 10)
        self.assertEqual(max_integer([1.2, 9.2, 3, 0]), 9.2)
        self.assertEqual(max_integer(), None)
        self.assertTrue(max_integer([5, 4, 6]), int)
        self.assertFalse(max_integer([0, 0, 0]), False)
        self.assertNotIn(max_integer([5, 4, 6]), [9, 4, 2])
        self.assertIsInstance(max_integer([5, 4, 6]), int)
        self.assertNotEqual(max_integer([3, 2, 5]), 8)
        self.assertEqual(max_integer([756980, 21756, -96]), 756980)
        self.assertRaises(TypeError, max_integer, [1, 2, 'Hello'])


if __name__ == '__main__':
    unittest.main()
