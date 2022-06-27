import logging

from src.outcomes import Outcomes
from src.single_game import single_game


def best_of(max_rounds):
    """Calculate the 'best of _' number of rounds"""
    return (max_rounds // 2) + 1


def game_loop(max_rounds, player_score=0, cpu_score=0):
    # todo put in init to calc the conditions for breaking in loop
    logger = logging.getLogger(__name__)

    while max(player_score, cpu_score) < best_of(max_rounds):
        outcome = single_game()

        # what happens after each game
        if outcome == Outcomes.WIN:
            player_score += 1
            print('You won!')
        elif outcome == Outcomes.LOSE:
            cpu_score += 1
            print('You lost!')
        else:
            print('You tied!')

    # score update
    logger.debug('Final Scores: ')
    logger.debug(f'Player: {player_score}')
    logger.debug(f'Computer: {cpu_score}')
