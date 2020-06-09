#!/usr/bin/python3
"""
    file containing unittest for Square class
"""

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """ Unittest for Square class"""

    a = 7
    b = 6
    c = 4
    s = Square(15)
    s2 = Square(15, 0, 0, 12)
    s3 = Square(17)
    s4 = Square(17, 1, 2)
    s13 = Square(a)
    s14 = Square(15, b, 0, 18)
    s15 = Square(12, 0, c, a)

    def test_Square_Creation(self):
        """ test to confirm square was made"""
        self.assertTrue(type(self.s) is Square)
        self.assertTrue(isinstance(self.s2, Square))

    def test_inheritance(self):
        """ test to confirm inheritance"""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_size_set(self):
        """test to confirm proper handling of size"""
        hello = "hello"
        self.assertTrue(self.s3.size, 17)
        with self.assertRaises(ValueError):
            s5 = Square(-10)
        with self.assertRaises(ValueError):
            s6 = Square(0)
        with self.assertRaises(TypeError):
            s7 = Square(10.02)
        with self.assertRaises(TypeError):
            s8 = Square("1")
        with self.assertRaises(TypeError):
            s9 = Square([1])
        with self.assertRaises(TypeError):
            s10 = Square((1, 2))
        with self.assertRaises(TypeError):
            s11 = Square({'1': 5})
        with self.assertRaises(TypeError):
            s12 = Square(hello)

    def test_x_set(self):
        """ test to confirm proper handling of x"""
        self.assertEqual(self.s.x, 0)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s4.x, 1)
        self.assertEqual(self.s14.x, 6)
        with self.assertRaises(ValueError):
            s16 = Square(10, -1, 0, 5)
        with self.assertRaises(TypeError):
            s17 = Square(10, "1", 0, 25)
        with self.assertRaises(TypeError):
            s18 = Square(10, [1, 2], 0, 26)
        with self.assertRaises(TypeError):
            s19 = Square(10, (1, 0), 0, 27)
        with self.assertRaises(TypeError):
            s20 = Square(10, 1.32, 0, 28)
        with self.assertRaises(TypeError):
            s21 = Square(10, {"2": 4}, 0, 29)

    def test_y_set(self):
        """ test to confirm proper handling of y"""
        self.assertEqual(self.s.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s4.y, 2)
        self.assertEqual(self.s15.y, 4)
        with self.assertRaises(ValueError):
            sq1 = Square(10, 0, -1, 50)
        with self.assertRaises(TypeError):
            sq2 = Square(10, 0, "1", 51)
        with self.assertRaises(TypeError):
            sq3 = Square(10, 0, [1, 2], 52)
        with self.assertRaises(TypeError):
            sq4 = Square(10, 0, (1, 2), 53)
        with self.assertRaises(TypeError):
            sq5 = Square(10, 0, 1.345, 54)
        with self.assertRaises(TypeError):
            sq6 = Square(10, 0, {"h": 5}, 55)

    def test_id_set(self):
        """ test to confirm proper handling of id"""
        self.assertTrue(self.s.id, 1)
        self.assertTrue(self.s2.id, 12)
        self.assertTrue(self.s3.id, 2)
        self.assertTrue(self.s4.id, 3)
        self.assertTrue(self.s13.id, 4)

    def test_area(self):
        """ test to confirm proper handling of area"""
        self.assertTrue(self.s.area, 255)
        self.assertTrue(self.s2.area, 255)
        self.assertTrue(self.s3.area, 289)
        self.assertTrue(self.s4.area, 289)
        self.assertTrue(self.s13.area, 49)
        self.assertTrue(self.s15.area, 144)

    def test_update(self):
        """ test to confirm proper handling of update method"""
        sq7 = Square(10, 0, 0, 65)
        self.assertEqual(sq7.id, 65)
        sq7.update(70)
        self.assertEqual(sq7.id, 70)
        sq7.update(x=1, y=2)
        self.assertEqual(sq7.x, 1)
        self.assertEqual(sq7.y, 2)

    def test_dictionary(self):
        """ test to confirm proper dictionary output"""
        sq8 = Square(10, 1, 2, 80)
        l = sq8.to_dictionary()
        self.assertTrue(type(l) is dict)

    def test_to_json_string(self):
        """ test to json string"""
        sq8 = Square(5)
        sq9 = Square(7)
        d1 = sq8.to_dictionary()
        d2 = sq9.to_dictionary()
        json_dict = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_dict), str)

    def test_to_json_file(self):
        """ test save to file"""
        import os
        su1 = Square(5)
        su2 = Square(8)
        Square.save_to_file([su1, su2])
        self.assertTrue(os.path.isfile("Square.json"))

    def test_from_json_string(self):
        """ test from json string"""
        sp1 = Square(8)
        sp2 = Square(9)
        dd = sp1.to_dictionary()
        dd1 = sp2.to_dictionary()
        list_input = Square.to_json_string([dd, dd1])
        list_output = Square.from_json_string(list_input)
        self.assertTrue(type(list_input) is str)
        self.assertTrue(type(list_output) is list)

    def test_create_method(self):
        """ test create method for instance"""
        sp3 = Square(8)
        dd3 = sp3.to_dictionary()
        sp4 = Square.create(**dd3)
        self.assertIsInstance(sp4, Square)
        self.assertIsNot(sp3, sp4)

    def test_load_from_file(self):
        """ test to check load from file"""
        sp5 = Square(7)
        sp6 = Square(6)
        Square.save_to_file([sp5, sp6])
        list_of_instances = Square.load_from_file()
        self.assertTrue(type(list_of_instances) is list)
        for i in list_of_instances:
            self.assertIsInstance(i, Square)

    def test_raises_strings(self):
        """ test to make sure strings print with raises"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sp7 = Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sp8 = Square(-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sp8 = Square(10, "9")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sp8 = Square(10, -9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sp9 = Square(10, 8, "9")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sp10 = Square(10, 7, -8)

    def test_id_not_int(self):
            sl = Square(10, 2, 3)
            self.assertIsNot(sl.id, None)


if __name__ == "__main__":
    unittest.main()
