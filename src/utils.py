from random import random


def rand_state(probability) -> int:
    return int(random() < probability)
