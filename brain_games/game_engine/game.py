from prompt import string
from random import randint, choice
import operator
import math


def get_gsd_data(num1, num2):
    problem = f'{num1} {num2}'
    correct = str(math.gcd(num1, num2))
    out = (problem, correct)
    return out


def get_even_data(num1, num2):
    problem = num1 * num2
    correct = 'yes' if problem % 2 == 0 else 'no'
    out = (problem, correct)
    return out


def get_calc_data(num1, num2):
    op = [('+', operator.add),
          ('-', operator.sub),
          ('*', operator.mul)]
    expression = choice(op)
    correct = str(expression[1](num1, num2))
    problem = f'{num1} {expression[0]} {num2}'
    out = (problem, correct)
    return out


def game(player, logic):
    wins = 0
    while wins < 3:
        num1 = randint(-100, 100)
        num2 = randint(-100, 100)
        data = logic(num1, num2)
        print(f'Question: {data[0]}')
        ans = string('Your answer: ')
        wins += game_test(ans, data[1], player)
    print(f'Congratulations, {player}!')


def game_test(ans, correct, player):
    score = 0
    if ans == correct:
        score += 1
        print('Correct!')
        return score
    else:
        print(f"""'{ans}' is wrong answer ;(. Correct answer was '{correct}'.
Let's try again, {player}!""")
        quit()
