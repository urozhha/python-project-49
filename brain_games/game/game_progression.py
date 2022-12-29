from random import randint, choice


def get_progression(num1, num2):
    stop = randint(5, 10)
    start = num1 - num2
    diff = randint(-10, 10)
    progression = [start]
    while len(progression) < stop:
        start += diff
        progression.append(start)
    gap = choice(progression)
    progression[progression.index(gap)] = '..'
    problem = ' '.join(str(x) for x in progression)
    correct = str(gap)
    out = (problem, correct)
    return out
