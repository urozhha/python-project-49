#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.game.game_even import EVEN_QUESTION, is_even


def main():
    run_game(EVEN_QUESTION, is_even)


if __name__ == '__main__':
    main()
