#!/usr/bin/python3
"""
    file containing Unittest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """ Unittest for Rectangle class"""

    a = 7
    b = 6
    c = 4
    r = Rectangle(5, 2)
    r2 = Rectangle(5, 2, 0, 0, 12)
    r3 = Rectangle(5, 2)
    r4 = Rectangle(5, 2, 1, 2)
    r5 = Rectangle(15, b, 0, 1, 18)
    r6 = Rectangle(a, b)
    r7 = Rectangle(5, 2, 0, c, 20)

    def test_Rectangle_Creation(self):
        """ Test to confirm Rectangle was created """
        self.assertTrue(isinstance(self.r, Rectangle))
        self.assertTrue(type(self.r2) is Rectangle)

    def test_inheritance(self):
        """ test to confirm inheritance"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_set(self):
        """" test to confirm proper handling of width"""
        self.assertEqual(self.r.width, 5)
        with self.assertRaises(ValueError):
            r8 = Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            r9 = Rectangle("10", 2)
        with self.assertRaises(TypeError):
            r10 = Rectangle([10, 2], 2)
        with self.assertRaises(TypeError):
            r11 = Rectangle((10, 2), 3)
        with self.assertRaises(ValueError):
            r12 = Rectangle(0, 11)
        with self.assertRaises(TypeError):
            r13 = Rectangle(10.01, 3)

    def test_height_set(self):
        """ test to confirm proper handling of height"""
        self.assertEqual(self.r3.height, 2)
        with self.assertRaises(ValueError):
            r14 = Rectangle(10, -2)
        with self.assertRaises(TypeError):
            r15 = Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r16 = Rectangle(10, [10, 2])
        with self.assertRaises(TypeError):
            r17 = Rectangle(10, (2, 3))
        with self.assertRaises(ValueError):
            r18 = Rectangle(10, 0)
        with self.assertRaises(TypeError):
            r19 = Rectangle(10, 3.01)

    def test_x_set(self):
        """ test to confirm proper handling of x"""
        self.assertEqual(self.r5.x, 0)
        with self.assertRaises(ValueError):
            r20 = Rectangle(10, 2, -1, 0, 12)
        with self.assertRaises(TypeError):
            r21 = Rectangle(10, 2, "7", 0, 12)
        with self.assertRaises(TypeError):
            r22 = Rectangle(10, 12, [10, 2], 0, 12)
        with self.assertRaises(TypeError):
            r23 = Rectangle(10, 11, (2, 3), 0, 12)
        with self.assertRaises(TypeError):
            r24 = Rectangle(10, 12, 3.01, 0, 12)
        self.assertEqual(self.r6.x, 0)

    def test_y_set(self):
        """ test to confirm proper handling of y"""
        self.assertEqual(self.r.y, 0)
        with self.assertRaises(ValueError):
            r25 = Rectangle(10, 2, 1, -1, 12)
        with self.assertRaises(TypeError):
            r26 = Rectangle(10, 2, 7, "0", 12)
        with self.assertRaises(TypeError):
            r27 = Rectangle(10, 12, 10, [2, 0], 12)
        with self.assertRaises(TypeError):
            r28 = Rectangle(10, 11, 2, (3, 0), 12)
        with self.assertRaises(TypeError):
            r29 = Rectangle(10, 12, 3, 5.01, 12)
        self.assertEqual(self.r7.y, 4)

    def test_id_set(self):
        """ test to confrim proper handling of id"""
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r5.id, 18)

    def test_area(self):
        """ test to confirm proper handling of area"""
        self.assertTrue(self.r.area, 10)
        self.assertTrue(self.r2.area, 10)
        self.assertTrue(self.r3.area, 10)
        self.assertTrue(self.r4.area, 10)
        self.assertTrue(self.r5.area, 90)
        self.assertTrue(self.r6.area, 42)

    def test_update(self):
        """ test to confirm proper handling of update"""
        r30 = Rectangle(5, 2, 0, 0, 65)
        self.assertEqual(r30.id, 65)
        r30.update(70)
        self.assertEqual(r30.id, 70)
        r30.update(x=1, y=2)
        self.assertEqual(r30.x, 1)
        self.assertEqual(r30.y, 2)
        r40 = Rectangle(5,2)
        with self.assertRaises(TypeError):
            r40.update(5, "10")
        with self.assertRaises(ValueError):
            r40.update(5, -1)
        with self.assertRaises(TypeError):
            r40.update(5, 4, "10")
        with self.assertRaises(ValueError):
            r40.update(5, 4, -1)
        with self.assertRaises(TypeError):
            r40.update(5, 4, 3, "1")
        with self.assertRaises(ValueError):
            r40.update(5, 4, 3, -1)
        with self.assertRaises(TypeError):
            r40.update(5, 4, 6, 7, "10")
        with self.assertRaises(ValueError):
            r40.update(5, 4, 5, 3, -1)

    def test_dictionary(self):
        """ test to confirm proper handling of dictionary"""
        r31 = Rectangle(5, 2, 0, 0, 90)
        l = r31.to_dictionary()
        self.assertTrue(type(l) is dict)

    def test_to_json_string(self):
        """ test to json string"""
        r42 = Rectangle(15, 7)
        r45 = Rectangle(5, 2)
        l1 = r42.to_dictionary()
        l2 = r45.to_dictionary()
        json_dictionary = Base.to_json_string([l1, l2])
        self.assertTrue(type(json_dictionary) is str)

    def test_to_json_file(self):
        """ test save to file"""
        import os.path
        r52 = Rectangle(5, 2)
        r65 = Rectangle(5, 3)
        Rectangle.save_to_file([r52, r65])
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_from_json_string(self):
        """ test from json string"""
        r77 = Rectangle(5, 2)
        r78 = Rectangle(5, 2)
        d1 = r77.to_dictionary()
        d2 = r78.to_dictionary()
        list_input = Rectangle.to_json_string([d1, d2])
        list_output = Rectangle.from_json_string(list_input)
        self.assertTrue(type(list_input) is str)
        self.assertTrue(type(list_output) is list)

    def test_create_method(self):
        """test create method for instance"""
        r88 = Rectangle(5, 2)
        d3 = r88.to_dictionary()
        r89 = Rectangle.create(**d3)
        self.assertIsInstance(r89, Rectangle)
        self.assertIsNot(r88, r89)

    def test_load_from_file(self):
        """ test to check load from file"""
        r95 = Rectangle(4, 5)
        r99 = Rectangle(9, 8)
        Rectangle.save_to_file([r95, r99])
        list_of_instances = Rectangle.load_from_file()
        self.assertTrue(type(list_of_instances) is list)
        for i in list_of_instances:
            self.assertIsInstance(i, Rectangle)


if __name__ == "__main__":
    unittest.main()
