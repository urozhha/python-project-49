from random import randint, choice


def progression():
    stop = randint(5, 10)
    start = randint(-100, 100)
    diff = randint(-10, 10)
    arithmetic_progression = [start]
    while len(arithmetic_progression) < stop:
        start += diff
        arithmetic_progression.append(start)
    gap = choice(arithmetic_progression)
    arithmetic_progression[arithmetic_progression.index(gap)] = '..'
    problem = ' '.join(str(x) for x in arithmetic_progression)
    correct = str(gap)
    return problem, correct


PROGRESSION_QUESTION = 'What number is missing in the progression?'
