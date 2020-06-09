#!/usr/bin/python3
""" Modules """

import unittest
from models.base import Base


class TestCasesBase(unittest.TestCase):

    b = Base()
    b1 = Base(12)
    b2 = Base()
    b3 = Base()
    b4 = Base(18)
    b5 = Base(19)
    b6 = Base()
    b7 = Base()

    def test_Base_creation(self):
        """ method to test that base class exist"""
        self.assertIsInstance(self.b, Base)

    def test_id_handling(self):
        """ method to test that the id functions properly"""
        self.assertTrue(self.b.id, 1)
        self.assertTrue(self.b2.id, 2)
        self.assertTrue(self.b3.id, 3)
        self.assertTrue(self.b4.id, 18)
        self.assertTrue(self.b5.id, 19)

    def test_to_json_string(self):
        """ test to check json string"""
        b8 = Base()
        d12 = b8.__dict__
        self.assertTrue(type(d12) is dict)
        j13 = Base.to_json_string([d12])
        self.assertTrue(type(j13) is str)

    def test_from_json_string(self):
        """ test to check from json string"""
        b9 = Base(12)
        d14 = b9.__dict__
        j15 = Base.to_json_string([d14])
        j_to_d = Base.from_json_string(j15)
        self.assertTrue(type(j15) is str)
        self.assertTrue(type(j_to_d) is list)


if __name__ == "__main__":
    unittest.main()
