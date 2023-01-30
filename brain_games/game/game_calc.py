from random import choice, randint
import operator


def calc_expression():
    num1 = randint(-100, 100)
    num2 = randint(-100, 100)
    operators = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    operation = choice(operators)
    problem_calc = f'{num1} {operation[0]} {num2}'
    correct_calc = str(operation[1](num1, num2))
    return problem_calc, correct_calc


CALC_QUESTION = 'What is the result of the expression?'
