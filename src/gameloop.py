import logging

from src.outcomes import Outcomes
from src.single_game import single_game
from src.ui import UI

logger = logging.getLogger(__name__)


def best_of(max_rounds):
    """Calculate the 'best of _' number of rounds"""
    return (max_rounds // 2) + 1


def game_loop(max_rounds, player_score=0, cpu_score=0, rounds=1):
    while max(player_score, cpu_score) < best_of(max_rounds):

        # keep track of rounds
        UI().round_message(rounds)
        # play a single game
        outcome = single_game()

        # determine what happens after each round
        if outcome == Outcomes.WIN:
            player_score += 1
            rounds += 1
            UI().win_message()

        elif outcome == Outcomes.LOSE:
            cpu_score += 1
            rounds += 1
            UI().lose_message()

        else:
            UI().tie_message()

        UI().score_update(player_score, cpu_score)
