import unittest
from balance_scale import BalanceScale

class BalanceScaleTestCase(unittest.TestCase):
    def setUp(self):
        self.scale = BalanceScale()

    def test_compare_returns_negative_one_when_left_weighs_more_than_right(self):
        left = [1, 1, 2]
        right = [1, 1, 1]

        # Return -1 if fail.
        self.assertEqual(self.scale.compare(left, right, -1))

    def test_compare_returns_zero_when_left_equals_right(self):
        left = [1, 1, 2]
        right = [1, 1, 1]

        self.assertEqual(self.scale.compare(left, right), 0)
