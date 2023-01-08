from math import gcd


def gcd_game(num1, num2):
    problem_gcd = f'{num1} {num2}'
    correct_gcd = str(gcd(num1, num2))
    gcd_out = (problem_gcd, correct_gcd)
    return gcd_out


GSD_QUESTION = 'Find the greatest common divisor of given numbers.'
