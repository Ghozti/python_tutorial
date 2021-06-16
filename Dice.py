import random


class Dice:

    def __init__(self):
        pass

    dice1 = 0
    dice2 = 0

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        return self.dice1, self.dice2
