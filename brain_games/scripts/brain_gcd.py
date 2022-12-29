#!/usr/bin/env python3
from brain_games.game.greeting import get_name as get_gcd_player
from brain_games.game.greeting import say_hello as gcd_greeting
from brain_games.game.game_engine import game as gcd_game
from brain_games.game.game_gcd import get_gsd_data


def main():
    gcd_player = get_gcd_player()
    print(gcd_greeting(gcd_player))
    print('Find the greatest common divisor of given numbers.')
    gcd_game(gcd_player, get_gsd_data)


if __name__ == '__main__':
    main()
