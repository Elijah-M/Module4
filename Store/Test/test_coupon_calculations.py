"""
This file (test_coupon_calculations.py) if for the purpose of testing the
calculate_price() function from the coupon_calculations.py file
"""

import unittest
from Store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        self.assertAlmostEqual(calculate_price(60, 5, .1), 64.42, places=1)
        self.assertAlmostEqual(calculate_price(70, 5, .15), 58.57, places=1)
        self.assertAlmostEqual(calculate_price(80, 5, .2), 63.60, places=1)
        self.assertAlmostEqual(calculate_price(90, 10, .1), 76.32, places=1)
        self.assertAlmostEqual(calculate_price(105, 9, .15), 86.50, places=1)
        self.assertAlmostEqual(calculate_price(1203, 8, .2), 1013.36, places=1)

if __name__ == '__main__':
    unittest.main()
