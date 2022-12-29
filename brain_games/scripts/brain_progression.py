#!/usr/bin/env python3
from brain_games.game.greeting import get_name as get_progression_name
from brain_games.game.greeting import say_hello as progression_greeting
from brain_games.game.game_engine import game as progression_game
from brain_games.game.game_engine import get_progression


def main():
    progression_player = get_progression_name()
    print(progression_greeting(progression_player))
    print('What number is missing in the progression?')
    progression_game(progression_player, get_progression)


if __name__ == '__main__':
    main()
