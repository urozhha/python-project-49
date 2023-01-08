#!/usr/bin/env python3
from brain_games.game.game_engine import run_game
from brain_games.game.game_calc import CALC_QUESTION, calc_expression


def main():
    run_game(CALC_QUESTION, calc_expression)


if __name__ == '__main__':
    main()
