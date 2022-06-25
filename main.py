import src.utils as utils
from src.gameloop import game_loop

if __name__ == '__main__':
    logger = utils.log_init()

    # todo make a UI
    #  setup controller to facilitate converting player inputs into scores
    n_rounds = input('Please enter the "best of _" rounds: ')
    game_loop(n_rounds)
