from prompt import string
from random import randint, choice
import operator
import math


def get_progression(num1, num2):
    stop = randint(5, 10)
    start = num1 - num2
    diff = randint(-10, 10)
    prg = [start]
    while len(prg) < stop:
        start += diff
        prg.append(start)
    gap = choice(prg)
    prg[prg.index(gap)] = '..'
    problem = ' '.join(str(x) for x in prg)
    correct = str(gap)
    out = (problem, correct)
    return out


def get_is_prime(num1, num2):
    correct = ''
    problem = abs(num1 - num2)
    for i in range(2, problem):
        if problem % i == 0:
            correct = 'no'
            break
        else:
            correct = 'yes'
    out = (problem, correct)
    return out


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
        first = randint(-100, 100)
        second = randint(-100, 100)
        data = logic(first, second)
        print(f'Question: {data[0]}')
        answer = string('Your answer: ')
        wins += game_test(answer, data[1], player)
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
