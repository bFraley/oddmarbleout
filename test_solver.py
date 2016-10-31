import unittest

from solver import solve
from marble_set import MarbleSet
from balance_scale import BalanceScale

class solveTestCase(unittest.TestCase):

    def test_solve_return_list_of_two_items(self):
        result = solve(MarbleSet(), BalanceScale())

        self.assertEqual(len(result), 2)

    @unittest.skip("skip until we have started our solution")
    def test_solve_returns_the_correct_solution(self):
        marble_set = MarbleSet()
        result = solve(marble_set, BalanceScale())

        self.assertTrue(marble_set.checkSolution(result))