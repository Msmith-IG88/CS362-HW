"""
Name: Michael Smith
Instructions:
1. Make sure you are inside the Question#1 directory.
2. Run "python3 -m unittest test_cube.py
3. All three test should have been ran without any failures.
"""
import unittest
import cube

class test(unittest.TestCase):
    def test_calculation(self):
        result = cube.calc_cube(2)
        self.assertEqual(result, 8)

    def test_negative(self):
        result = cube.calc_cube(-2)
        self.assertEqual(result, "input invalid")

    def test_string(self):
        result = cube.calc_cube("test")
        self.assertEqual(result, "input invalid")

