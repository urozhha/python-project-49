#!/usr/bin/env python3
from brain_games.game.greeting import get_name as get_calc_player
from brain_games.game.greeting import say_hello as calc_greeting
from brain_games.game.game_engine import game as calc_game
from brain_games.game.game_calc import get_calc_data


def main():
    calc_player = get_calc_player()
    print(calc_greeting(calc_player))
    print('What is the result of the expression?')
    calc_game(calc_player, get_calc_data)


if __name__ == '__main__':
    main()
