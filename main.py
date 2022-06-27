from src import log_init, game_loop

if __name__ == '__main__':
    # logger setup
    logger = log_init()
    # logging.disable(logging.DEBUG)

    # todo make an introductory UI, explain rules and goals
    # todo setup controller to facilitate converting player inputs into scores

    # collect the max number of rounds to be played
    n_rounds = int(input('Please enter the "best of _" rounds: '))

    # play the game
    game_loop(n_rounds)
