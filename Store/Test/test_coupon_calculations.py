"""
This file (test_coupon_calculations.py) if for the purpose of testing the
calculate_price() function from the coupon_calculations.py file
"""

import unittest
from Store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        self.assertAlmostEqual(calculate_price(10, 5, .1), 10.72, places=1)
        self.assertAlmostEqual(calculate_price(10, 5, .15), 10.46, places=1)
        self.assertAlmostEqual(calculate_price(10, 5, .2), 10.19, places=1)
        self.assertAlmostEqual(calculate_price(10, 10, .1), 5.95, places=1)
        self.assertAlmostEqual(calculate_price(10, 9, .15), 6.85, places=1)
        self.assertAlmostEqual(calculate_price(10, 8, .2), 7.65, places=1)

if __name__ == '__main__':
    unittest.main()
