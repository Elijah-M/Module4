"""
This file (test_coupon_calculations.py) if for the purpose of testing the
calculate_price() function from the coupon_calculations.py file
"""

import unittest
from Store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):
    def test_calculate_price(self):
        self.assertAlmostEqual(calculate_price(20, 5, .1), 22.26, places=1)
        self.assertAlmostEqual(calculate_price(20, 5, .15), 21.47, places=1)
        self.assertAlmostEqual(calculate_price(20, 5, .2), 20.67, places=1)
        self.assertAlmostEqual(calculate_price(20, 10, .1), 17.49, places=1)
        self.assertAlmostEqual(calculate_price(15, 9, .15), 11.36, places=1)
        self.assertAlmostEqual(calculate_price(11, 8, .2), 8.49, places=1)

if __name__ == '__main__':
    unittest.main()
