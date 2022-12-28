#!/usr/bin/env python3
from brain_games.game_engine.greeting import get_name, say_hello
from brain_games.game_engine.game import game, get_progression


def main():
    player = get_name()
    print(say_hello(player))
    print('What number is missing in the progression?')
    game(player, get_progression)


if __name__ == '__main__':
    main()
