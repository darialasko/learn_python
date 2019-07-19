from random import random


def coin_flip():
    if random() > 0.5:
        return "heads"
    else:
        return "tails"


print(coin_flip())
