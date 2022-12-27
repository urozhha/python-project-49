#!/usr/bin/env python3
from brain_games.game_engine.greeting import get_name, say_hello
from brain_games.game_engine.game import game, get_gsd_data


def main():
    player = get_name()
    print(say_hello(player))
    print('Find the greatest common divisor of given numbers.')
    game(player, get_gsd_data)


if __name__ == '__main__':
    main()
