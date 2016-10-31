from random import choice, shuffle

class MarbleSet():
    def __init__(self, marble_options=None, shuffle=shuffle):
        if marble_options is None:
            self.marble_options = [0, 2]
        else:
            self.marble_options = marble_options


        self.choice = choice
        self.shuffle = shuffle
        self.make_marbles()

    def make_marbles(self):
        self.marbles = [1 for x in range(12)]
        self.marbles[0] = self.choice(self.marble_options)
        self.shuffle(self.marbles)


    def checkSolution(self, solution):
        if solution[1]:
            return self.marbles[solution[0]] > 1
        else:
            return self.marbles[solution[0]] < 1
