import logging

logger = logging.getLogger(__name__)


class UI:
    def get_tie_message(self):
        pass

    def get_win_message(self):
        pass

    def get_lose_message(self):
        pass

    @staticmethod
    def game_start_message():
        return 'Please enter 0 for Rock, 1 for Paper, or 2 for Scissors'
