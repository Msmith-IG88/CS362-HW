"""
Name: Michael Smith
Instructions:
1. Make sure you are inside the Question#2 directory.
2. Run "python3 -m unittest test_avg.py
3. All three test should have been ran without any failures.
"""
import unittest
import average

class test(unittest.TestCase):
    def test_calculation(self):
        test = [10,20,30,40,50,70]
        result = average.calc_avg(test)
        self.assertEqual(result, 36.666666666666664)

    def test_content(self):
        test = [10,16,'g',7,'d']
        result = average.calc_avg(test)
        self.assertEqual(result, "input invalid")

    def test_empty_list(self):
        test = []
        result = average.calc_avg(test)
        self.assertEqual(result, "input invalid")
