import prompt


def say_hello(player):
    greeting = f'Hello, {player}!'
    return greeting


def get_name():
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    return name
