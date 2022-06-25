import random
import logging

logger = logging.getLogger(__name__)


def best_of(max_rounds):
    """Calculate the 'best of _' number of rounds"""
    return (max_rounds // 2) + 1


def game_loop(max_rounds, player_score=0, cpu_score=0):
    # todo put in init to calc the conditions for breaking in loop

    idx = 0
    while max(player_score, cpu_score) < best_of(max_rounds):
        # todo use random to increase player score or cpu score to test condition
        print(idx)

        # randomly assign scores to the player or cpu
        if random.randint(0, 1) == 0:
            player_score += 1
        else:
            cpu_score += 1

        # increment index
        idx += 1

    # score update
    logger.info('Final Scores: ')
    logger.info(f'Player: {player_score}')
    logger.info(f'Computer: {cpu_score}')

    # todo put in winner
