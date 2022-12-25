from random import randint
from prompt import string


def game_even(player):
    wins = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while wins < 3:
        even_que = randint(0, 1000)
        wrong = 'yes' if even_que % 2 == 0 else 'no'
        print(f'Question: {even_que}')
        ans = string('Your answer: ')
        if ans == wrong:
            print('Correct!')
            wins += 1
        else:
            print(f"""'{ans}' is wrong answer ;(. Correct answer was '{wrong}'.
    Let's try again, {player}!""")
            quit()
    print(f'Congratulations, {player}!')
