from random import randint


def is_even():
    problem_even = randint(-100, 100)
    correct_even = 'yes' if problem_even % 2 == 0 else 'no'
    return problem_even, correct_even


EVEN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
