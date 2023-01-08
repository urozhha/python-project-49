from random import choice
import operator


def calc_expression(num1, num2):
    operators = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]
    operation = choice(operators)
    problem_calc = f'{num1} {operation[0]} {num2}'
    correct_calc = str(operation[1](num1, num2))
    calc_out = (problem_calc, correct_calc)
    return calc_out


CALC_QUESTION = 'What is the result of the expression?'
