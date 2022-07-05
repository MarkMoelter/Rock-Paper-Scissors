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
        print(f"Cpu's score: {cpu_score}")
        print('#####')

    def entity_message(self, player_entity, cpu_entity):
        print(f'{self.player_name} selected: {player_entity}')
        print(f'CPU selected: {cpu_entity}')

    def selection_message(self):
        return f'{self.player_name}, please enter 0 for Rock, 1 for Paper, or 2 for Scissors: '

    def final_win_or_lose_message(self, player_score, cpu_score):
        if player_score > cpu_score:
            print(f'Congratulations! {self.player_name} won!')
        else:
            print('Game Over')

    @staticmethod
    def round_message(rounds):
        print(f'Round: {rounds}')
