from prompt import string


def welcome_user():
    player = string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {player}!')
