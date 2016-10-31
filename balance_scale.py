class BalanceScale():
    def compare(self, left, right):
        left_sum = sum(left)
        right_sum = sum(right)

        if left_sum > right_sum:
            return -1
        else:
            return 0
            