#!/usr/bin/env python3
from brain_games.game_engine.greeting import get_name, say_hello
from brain_games.game_engine.game import game, get_is_prime


def main():
    player = get_name()
    print(say_hello(player))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game(player, get_is_prime)


if __name__ == '__main__':
    main()
