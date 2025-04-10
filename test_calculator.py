# https://github.com/lucas-mcalli/lab10-LM-AC.git
# Partner 1: Lucas McAllister
# Partner 2: Aidan Chiodo

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,1), 1)
        self.assertEqual(mul(1,9), 9)
        self.assertEqual(mul(9,9), 81)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(9,81), (1/9))
        self.assertEqual(div(5,5), 1)
        self.assertAlmostEqual(div(1,3), 0.333)


    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(2,2), math.sqrt(8))
        self.assertEqual(hypotenuse(2,3), math.sqrt(13))
        self.assertEqual(hypotenuse(10,10), math.sqrt(200))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(2), 4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()