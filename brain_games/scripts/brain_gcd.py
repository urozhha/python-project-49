#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.game.game_gcd import GSD_QUESTION, gcd_game


def main():
    run_game(GSD_QUESTION, gcd_game)


if __name__ == '__main__':
    main()
