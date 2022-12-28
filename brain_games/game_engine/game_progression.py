


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