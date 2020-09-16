"""
This file (test_coupon_calculations.py) if for the purpose of testing the
calculate_price() function from the coupon_calculations.py file
"""

import unittest
from Store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        self.assertAlmostEqual(calculate_price(60, 5, .1), 45.34, places=1)
        self.assertAlmostEqual(calculate_price(70, 5, .15), 39.49, places=1)
        self.assertAlmostEqual(calculate_price(80, 5, .2), 37.63, places=1)
        self.assertAlmostEqual(calculate_price(90, 10, .1), 36.57, places=1)
        self.assertAlmostEqual(calculate_price(105, 9, .15), 44.39, places=1)
        self.assertAlmostEqual(calculate_price(1203, 8, .2), 30.85, places=1)

if __name__ == '__main__':
    unittest.main()
