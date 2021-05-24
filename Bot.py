import random


class Bot:
    def __init__ (self, name, is_random, weights):
        self.name = name
        self.weights = weights
        if not is_random:
            self.weights += random.uniform(-1, 1)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Bot(Name: {})".format(self.name)

