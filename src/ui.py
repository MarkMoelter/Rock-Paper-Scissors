import os


class UI:
    def __init__(self, name: str = 'Player'):
        self.player_name = name

    def tie_message(self):
        print(f'{self.player_name} tied!')

    def win_message(self):
        print(f'{self.player_name} won!')

    def lose_message(self):
        print(f'{self.player_name} lost!')

    def score_update(self, player_score, cpu_score):
        print(f"{self.player_name}'s score: {player_score}")
        print(f'Cpu score: {cpu_score}')
        print('#####')

    def entity_message(self):
        return f'{self.player_name}, please enter 0 for Rock, 1 for Paper, or 2 for Scissors: '

    @staticmethod
    def round_message(rounds):
        print(f'Round: {rounds}')
