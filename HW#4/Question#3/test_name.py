"""
Name: Michael Smith
Instructions:
1. Make sure you are inside the Question#3 directory.
2. Run "python3 -m unittest test_name.py
3. All three test should have been ran without any failures.
"""
import unittest
import name

class test(unittest.TestCase):
    def test_name(self):
        test1 = "Darth"
        test2 = "Vader"
        result = name.create_name(test1, test2)
        self.assertEqual(result, "Darth Vader")

    def test_strings(self):
        test1 = 23
        test2 = "jordan"
        result = name.create_name(test1, test2)
        self.assertEqual(result, "input invalid")

    def test_capitalization(self):
        test1 = "lUkE"
        test2 = "skYWaLkEr"
        result = name.create_name(test1, test2)
        self.assertEqual(result, "Luke Skywalker")
