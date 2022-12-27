#!/usr/bin/env python3
from brain_games.game_engine.game import game, get_even_data
from brain_games.game_engine.greeting import get_name, say_hello


def main():
    player = get_name()
    print(say_hello(player))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(player, get_even_data)


if __name__ == '__main__':
    main()
