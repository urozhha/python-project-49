#!/usr/bin/env python3
from brain_games.game_engine.greeting import get_name, say_hello
from brain_games.game_engine.game import game, get_calc_data


def main():
    player = get_name()
    print(say_hello(player))
    print('What is the result of the expression?')
    game(player, get_calc_data)


if __name__ == '__main__':
    main()
