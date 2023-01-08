from random import randint, choice


def progression(num1, num2):
    stop = randint(5, 10)
    start = num1 - num2
    diff = randint(-10, 10)
    arithmetic_progression = [start]
    while len(arithmetic_progression) < stop:
        start += diff
        arithmetic_progression.append(start)
    gap = choice(arithmetic_progression)
    arithmetic_progression[arithmetic_progression.index(gap)] = '..'
    problem = ' '.join(str(x) for x in arithmetic_progression)
    correct = str(gap)
    out = (problem, correct)
    return out


PROGRESSION_QUESTION = 'What number is missing in the progression?'
