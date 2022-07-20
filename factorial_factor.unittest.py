import unittest
from factorial_factor import *


class Testfunctions(unittest.TestCase):

    def test_case_factorial(self):
        self.assertEqual(factorial(10), 3628800)
    def test_case_factorial_0(self):
        self.assertEqual(factorial(0), 1)
    def test_case_factorial_1(self):
        self.assertEqual(factorial(1), 1)
    def test_case_factorial_negative(self):
        self.assertEqual(factorial(-10), None)

    def test_case_factors(self):
        self.assertEqual(factors(10), [1, 2, 5, 10])
    def test_case_factors_0(self):
        self.assertEqual(factors(0), None)
    def test_case_factors_negative(self):
        self.assertEqual(factors(-10), None)

if __name__ == '__main__':
    unittest.main()
