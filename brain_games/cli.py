from brain_games.game_engine.greeting import get_name
from brain_games.game_engine.greeting import say_hello


def welcome_user():
    return say_hello(get_name())
