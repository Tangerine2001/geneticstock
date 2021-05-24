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

    def determine_score(self, stock_data):
        # stock_data should contain 7 data points
        # [12 months ago closing, 9, 6, 3, 2, 1, 0 (now)]
        # weights list should have length seven
        # create factor list as:
        # [12 - 0, 12 - 9, 9 - 6, 6 - 3, 3 - 0, 2 - 0, 1 - 0]
        # as indices:
        # [0 - 6, 0 - 1, 1 - 2, 2 - 3, 3 - 6, 4 - 6, 5 - 6]
        # straight up multiply indices together
        # return the sum

        factor_list = [stock_data[0] - stock_data[6],
                       stock_data[0] - stock_data[1],
                       stock_data[1] - stock_data[2],
                       stock_data[2] - stock_data[3],
                       stock_data[3] - stock_data[6],
                       stock_data[4] - stock_data[6],
                       stock_data[5] - stock_data[6]]

        products = []
        for i in range(7):
            products.append(self.weights[i] * factor_list[i])
        return sum(products)
