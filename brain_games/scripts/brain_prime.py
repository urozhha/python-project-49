#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.game.game_prime import PRIME_QUESTION, is_prime


def main():
    run_game(PRIME_QUESTION, is_prime)


if __name__ == '__main__':
    main()
