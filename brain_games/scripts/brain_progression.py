#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.game.game_progression import PROGRESSION_QUESTION, progression


def main():
    run_game(PROGRESSION_QUESTION, progression)


if __name__ == '__main__':
    main()
