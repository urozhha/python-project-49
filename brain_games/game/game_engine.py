from prompt import string
from random import randint


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
