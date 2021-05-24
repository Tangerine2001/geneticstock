import random


class Bot:
    def __init__(self, name, is_random, weights):
        self.name = name
        self.weights = weights
        if not is_random:
            for i in range(len(self.weights)):
                self.weights[i] += random.uniform(-1, 1)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "Bot(Name: {})".format(self.name)
