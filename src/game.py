import random
import os

from src.entities import int_to_entity
from src.outcomes import Outcomes
from src.rules import Rules
from src.ui import UI


class Game:
    def __init__(self, max_rounds: int, ui: UI):
        """
        Overarching game structure.

        :param max_rounds: The maximum number of games that can be played.
        """
        self.max_rounds = max_rounds
        self.ui = ui
        # todo integrate UI into code

    def __best_of(self) -> int:
        """Formula to calculate the 'best of _' number of rounds"""
        return (self.max_rounds // 2) + 1

    def single_game(self):
        """
        Plays a single game of Rock Paper Scissors.

        :return: The outcome of the game
        """

        player_input = int(input(self.ui.entity_message()))

        # convert int to the corresponding entities
        player_entity = int_to_entity(player_input)
        cpu_entity = int_to_entity(random.randint(0, 2))

        print(f'You selected: {player_entity}')
        print(f'CPU selected: {cpu_entity}')

        outcome = Rules(
            player=player_entity,
            cpu=cpu_entity
        ).get_winner()
        print(f'The outcome is: {outcome}')

        return outcome

    def game_loop(self, player_score=0, cpu_score=0) -> None:
        """
        Multi-game loop. Stops when the player or cpu reaches n/2 + 1.

        :param player_score: Initialize the starting scores of the player for convenience.
        :param cpu_score: Initialize the starting scores for the cpu.
        """

        rounds = 1
        while max(player_score, cpu_score) < self.__best_of():
            # keep track of rounds
            self.ui.round_message(rounds)

            # play a single game
            outcome = self.single_game()
            os.system('cls')

            # determine what happens after each round
            if outcome == Outcomes.WIN:
                player_score += 1
                rounds += 1
                self.ui.win_message()

            elif outcome == Outcomes.LOSE:
                cpu_score += 1
                rounds += 1
                self.ui.lose_message()

            else:
                self.ui.tie_message()

            self.ui.score_update(player_score, cpu_score)

        if player_score > cpu_score:
            print('Congratulations! You won!')
        else:
            print('Game Over')
