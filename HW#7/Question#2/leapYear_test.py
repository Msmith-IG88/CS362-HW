import unittest
import LeapYear

class test(unittest.TestCase):
    def test_inputError(self):
        result = LeapYear.leap_year("test")
        self.assertEqual(result, "Invalid input")