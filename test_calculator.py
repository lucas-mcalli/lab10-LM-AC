import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual((2, 5), 7)
        self.assertEqual((1,3),4)
        self.assertEqual((10,10),20)

    def test_subtract(self): # 3 assertions
        self.assertEqual((5,2),3)
        self.assertEqual((10,10),0)
        self.assertEqual((5,4),1)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual((100, 10), 2)
        self.assertEqual((1,5),0)
        self.assertEqual((8,2),3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1, 1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()