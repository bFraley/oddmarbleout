class BalanceUsedTooManyTimesError(Exception):
    pass

class BalanceScale():

    def __init__(self):
        self.times_left = 3

    def compare(self, left, right):
        if len(left) != len(right):
            raise ValueError

        if self.times_left <= 0:
            raise BalanceUsedTooManyTimesError

        self.times_left -= 1

        left_sum = sum(left)
        right_sum = sum(right)

        if left_sum > right_sum:
            return -1
        elif left_sum < right_sum:
            return 1
        else:
            return 0
