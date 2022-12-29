#!/usr/bin/env python3
from brain_games.game.greeting import get_name as get_even_player
from brain_games.game.greeting import say_hello as even_greeting
from brain_games.game.game_engine import game as even_game
from brain_games.game.game_even import get_even_data


def main():
    even_player = get_even_player()
    print(even_greeting(even_player))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(even_player, get_even_data)


if __name__ == '__main__':
    main()
