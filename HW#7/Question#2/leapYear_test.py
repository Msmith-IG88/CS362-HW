import unittest
import LeapYear

class test(unittest.TestCase):
    def test_inputError(self):
        result = LeapYear.leap_year("test")
        self.assertEqual(result, "Invalid input")

    def test_leapYear(self):
        result = LeapYear.leap_year("2000")
        self.assertEqual(result, "2000 is a leap year")