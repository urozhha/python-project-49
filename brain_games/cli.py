from brain_games.game.greeting import get_name as get_player
from brain_games.game.greeting import say_hello as games_greeting


def welcome_user():
    return games_greeting(get_player())
