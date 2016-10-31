import unittest
from balance_scale import BalanceScale, BalanceUsedTooManyTimesError

class BalanceScaleTestCase(unittest.TestCase):
    def setUp(self):
        self.scale = BalanceScale()

    def test_compare_returns_negative_one_when_left_weighs_more_than_right(self):
        left = [1, 1, 2]
        right = [1, 1, 1]

        # Return -1 if fail.
        self.assertEqual(self.scale.compare(left, right), -1)

    def test_compare_returns_zero_when_left_equals_right(self):
        left = [1, 1, 1]
        right = [1, 1, 1]

        self.assertEqual(self.scale.compare(left, right), 0)


    def test_compare_returns_zero_when_left_less_than_right(self):
        left = [1, 1, 0]
        right = [1, 1, 1]

        self.assertEqual(self.scale.compare(left, right), 1)


    def test_compare_raises_ValueError_if_len_left_not_equal_len_right(self):
        left = [1]
        right = [1, 2, 3]

        self.assertRaises(ValueError, self.scale.compare(left, right))


    def test_compare_raises_BalanceUsedTooManyTimesError_if_used_more_than_3_times(self):
        self.scale.compare([0], [0])
        self.scale.compare([0], [0])
        self.scale.compare([0], [0])

        self.assertRaises(BalanceUsedTooManyTimesError, self.scale.compare, [0], [0])
            