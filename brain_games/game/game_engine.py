from prompt import string
from random import randint


def run_game(main_question, logic):
    player = string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {player}!')
    print(main_question)
    wins = 0
    while wins < 3:
        first = randint(-100, 100)
        second = randint(-100, 100)
        data = logic(first, second)
        print(f'Question: {data[0]}')
        ans = string('Your answer: ')
        correct = data[1]
        if ans == correct:
            wins += 1
            print('Correct!')
        else:
            print(
                f"""'{ans}' is wrong answer ;(. Correct answer was '{correct}'.
Let's try again, {player}!
"""
            )
            quit()
    print(f'Congratulations, {player}!')
