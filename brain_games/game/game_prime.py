from random import randint


def is_prime():
    correct_prime = ''
    problem_prime = randint(0, 100)
    for i in range(2, problem_prime):
        if problem_prime % i == 0:
            correct_prime = 'no'
            break
        else:
            correct_prime = 'yes'
    return problem_prime, correct_prime


PRIME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
