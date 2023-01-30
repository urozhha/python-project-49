from math import gcd
from random import randint


def gcd_game():
    first = randint(-100, 100)
    second = randint(-100, 100)
    problem_gcd = f'{first} {second}'
    correct_gcd = str(gcd(first, second))
    return problem_gcd, correct_gcd


GSD_QUESTION = 'Find the greatest common divisor of given numbers.'
