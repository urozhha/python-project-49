#!/usr/bin/env python3
from brain_games.game.greeting import get_name as get_prime_player
from brain_games.game.greeting import say_hello as prime_greeting
from brain_games.game.game_engine import game as prime_game
from brain_games.game.game_prime import get_is_prime


def main():
    prime_player = get_prime_player()
    print(prime_greeting(prime_player))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_game(prime_player, get_is_prime)


if __name__ == '__main__':
    main()
