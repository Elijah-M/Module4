from input_validation.validation_with_try import average
import unittest

class input_validation_test(unittest.TestCase):
    def test_average_negitive_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

if __name__ == '__main__':
    unittest.main()
