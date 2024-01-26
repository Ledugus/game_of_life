from random import random


def rand_state(probability) -> int:
    """Returns 1 with probability, else 0"""
    return int(random() < probability)
