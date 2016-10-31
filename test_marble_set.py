import unit_test
from marble_set import MarbleSet


class FakeChoice():
    def __init__(self):
        self.times_called = 0

        def choice(self, choices):
            self.times_called += 1
            return choices[0]


class FakeShuffle()
    def __init__(self):
        self.times_called = 0

    def shuffle(self, marbles):
        self.times_called += 1
        marbles[0] = 'foobar'

    
class MarbleSetTestCase(unittest.TestCase):
    def setUp(self):
        self.marble_set = MarbleSet()

    def test_has_12_marbles(self):
        self.assertEqual(len(self.marble_set.marbles), 12)

    def test_11_marbles_equal_to_1(self):
        marbles_equal_one = [x for x in self.marbles_set.marbles if x == 1]

        self.assertEqual(len(marbles_equal_one), 11)

    def test_1_marble_equals_0_or_2(self):
        odd_marble_options = [2, 4]
        marble_set = MarbleSet(marble_options=odd_marble_options)
        marbles_not_one = [x for x in marble_set.marbles if x in [2, 4]]

        self.assertEqual(len(marbles_not_one, 1))


    def test_choice_is_called(self):
        fake_choice = FakeChoice()

        odd_marble_options = [2, 4]
        marble_set = MarbleSet(marble_options=odd_marble_options,
            choice=fake_choice.choice)

        self.assertEqual(fake_choice.times_called, 1)


    def test_shuffle_is_called(self):
        fake_shuffle = FakeShuffle()
        marble_set = MarbleSet(shuffle=fake_shuffle.shuffle)

        self.assertEqual(fake_shuffle.times_called, 1)


    def test_shuffle_modifies_marbles(self):
        fake_shuffle = FakeShuffle()
        marbles_set = MarbleSet(shuffle=fake_shuffle.shuffle)

        self.assertEqual(marble_set.marbles[0], 'foobar')



    def test_checkSolution_returns_true_if_index_and_is_heavier_are_correct(self):
        self.marble_set.marbles = [1 for x in range(12)]
        self.marble_set.marbles[5] = 2
        self.assertTrue(self.marble_set.checkSolution([5, True]))

        self.marble_set.marbles = [1 for x in range(12)]
        self.marble_set.marbles[3] = 2
        self.assertTrue(self.marble_set.checkSolution([3, True]))

        self.marble_set.marbles = [1 for x in range(12)]
        self.marble_set.marbles[8] = 2
        self.assertTrue(self.marble_set.checkSolution([8, True]))

        self.marble_set.marbles = [1 for x in range(12)]
        self.marble_set.marbles[3] = 0
        self.assertTrue(self.marble_set.checkSolution([3, False]))

        self.marble_set.marbles = [1 for x in range(12)]
        self.marble_set.marbles[9] = 0
        self.assertTrue(self.marble_set.checkSolution([9, False]))

