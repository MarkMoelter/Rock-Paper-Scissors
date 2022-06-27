import logging

logger = logging.getLogger(__name__)


class UI:
    @staticmethod
    def tie_message():
        print('You tied!')

    @staticmethod
    def win_message():
        print('You won!')

    @staticmethod
    def lose_message():
        print('You lost!')

    @staticmethod
    def score_update(player_score, cpu_score):
        print(f'Player score: {player_score}')
        print(f'Cpu score: {cpu_score}')
        print('#####')

    @staticmethod
    def game_start_message():
        return 'Please enter 0 for Rock, 1 for Paper, or 2 for Scissors: '

    @staticmethod
    def round_message(rounds):
        print(f'Round: {rounds}')
