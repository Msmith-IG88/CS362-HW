import unittest
import FizzBuzz

class test(unittest.TestCase):
    def test_divByThree(self):
        result = FizzBuzz.Fizz_Buzz()
        x = 0
        for i in result:
            if i == "fizz":
                x += 1
        self.assertEqual(x,27)