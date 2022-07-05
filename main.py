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

    # play the game
    Game(user_interface).game_loop()


if __name__ == '__main__':
    main()
