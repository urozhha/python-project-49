from math import gcd


def get_gsd_data(num1, num2):
    problem_gcd = f'{num1} {num2}'
    correct_gcd = str(gcd(num1, num2))
    gcd_out = (problem_gcd, correct_gcd)
    return gcd_out
