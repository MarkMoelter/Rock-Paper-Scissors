import logging

from game import Game
from ui import UI
from utils import log_init


def main() -> None:
    # logger setup
    logger = log_init()
    logging.disable(logging.DEBUG)

    # instantiate the user interface
    user_interface = UI(input('Please enter your name: '))

    # collect the max number of rounds to be played
    n_rounds = int(input('Please enter the "best of _" rounds: '))

    # play the game
    Game(n_rounds, user_interface).game_loop()


if __name__ == '__main__':
    main()
