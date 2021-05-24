import random
from copy import copy
from Bot import Bot


def main():
    bot_list = []
    for i in range(5):
        bot_list.append(Bot("change this please", True,
                            [random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10),
                             random.uniform(-10, 10), random.uniform(-10, 10)]))

    while True:
        best_bots = [copy(bot_list[0]), copy(bot_list[1]), copy(bot_list[2]), copy(bot_list[3]), copy(bot_list[4])]
        new_bot_list = []
        for i in range(5):
            new_bot_list.append(Bot("Howard", False, best_bots[i].weights))
        break


if __name__ == '__main__':
    main()
