#!/usr/bin/env python3
from brain_games.game_engine.logic_even import game_even
from brain_games.game_engine.greeting import name, say_hello


def main():
    player = name
    print(say_hello(player))
    game_even(player)


if __name__ == '__main__':
    main()
