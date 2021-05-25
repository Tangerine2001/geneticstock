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
        # A natural problem that arises is that difference stocks
        # are worth a different amount. To offset this, the easiest
        # method would be to simply uses percentage change. But the
        # problem then lies in how to compute a double score with
        # a percentage? We used a normalized score to account for
        # for higher or lower value stocks in reference to their
        # percent changes
        score = 0
        normalized_score = 1

        # stock_data should contain 7 data points
        # [12 months ago closing, 9, 6, 3, 2, 1, 0 (now)]
        # Weights list should have length seven.
        # Create factor list as:
        # [12 - 0, 12 - 9, 9 - 6, 6 - 3, 3 - 0, 2 - 0, 1 - 0]
        # as indices:
        # [0 - 6, 0 - 1, 1 - 2, 2 - 3, 3 - 6, 4 - 6, 5 - 6]
        # Rules are determined below to calculate a score
        # return the score

        factor_list = [stock_data[0] - stock_data[6],
                       stock_data[0] - stock_data[1],
                       stock_data[1] - stock_data[2],
                       stock_data[2] - stock_data[3],
                       stock_data[3] - stock_data[6],
                       stock_data[4] - stock_data[6],
                       stock_data[5] - stock_data[6]]

        # With 7 factors there's a limited amount of rule sets
        # that would actually matter. Let's say for example
        # from months 12 - 9 the stock goes up, then we would
        # check if it continues going up from 9 - 6 and so on.
        # The longer the same trend occurs, the greater the
        # effect it would have the overall score.

        if factor_list[1] > 0:
            if factor_list[2] > 0:
                if factor_list[3] > 0:
                    if factor_list[4] > 0:
                        score += normalized_score * 16
                    else:
                        score += normalized_score * 8
                else:
                    score += normalized_score * 4
            else:
                score += normalized_score * 2
        else:
            if factor_list[2] < 0:
                if factor_list[3] < 0:
                    if factor_list[4] < 0:
                        score -= normalized_score * 16
                    else:
                        score -= normalized_score * 8
                else:
                    score -= normalized_score * 4
            else:
                score -= normalized_score * 2

        # The if statement mess above does not have any rules in places for
        # variables changes or account for the first and the last 2 factors.
        # A prototype ruleset for the variables changes among the first 5
        # factors are as follows

        # If the stock went up over a year but has been decreasing recently,
        # the score of the stock should go down but not by a lot.
        if factor_list[0] > 0 and factor_list[4] < 0:
            if factor_list[6] < 0:
                score -= normalized_score * 4

        # Add more variable rules

        # The last 2 factors are simple enough. The last factor should have
        # a slightly stronger effect the second to last factor.
        if factor_list[6] > 0:
            score += normalized_score * 5
            if factor_list[5] < 0:
                score -= normalized_score * 3
        else:
            score -= normalized_score * 5
            if factor_list[5] > 0:
                score += normalized_score * 3

        # Apply the weights to the factors.
        # I'm thinking I should change the weights being applied
        # to the factor to being applies to the normalized_scores
        products = []
        for i in range(7):
            products.append(self.weights[i] * factor_list[i])

        # Normalize the scores by dividing them all by the current value of the stock.
        for i in range(len(products)):
            products[i] /= stock_data[6]

        return score + sum(products)
