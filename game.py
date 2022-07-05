import os
import random

from entities import Entities
from outcomes import Outcomes
from rules import Rules
from ui import UI


class Game:
    def __init__(self, ui: UI):
        """
        Overarching game structure.

        :param ui: User interface
        """
        self.ui = ui
        self.win_rounds = int(input('Please enter the "first to _" rounds: '))

    def single_game(self) -> Outcomes:
        """
        Plays a single game of Rock Paper Scissors.

        :return: The outcome of the game
        """
        player_input = int(input(self.ui.selection_message()))

        # convert int to the corresponding entities
        player_entity = Entities(player_input)
        cpu_entity = Entities(random.randint(0, 2))

        self.ui.entity_message(player_entity, cpu_entity)

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

        while max(player_score, cpu_score) < self.win_rounds:

            # keep track of rounds
            self.ui.round_message(player_score + cpu_score + 1)  # starts on round 1

            # play a single game
            outcome = self.single_game()
            os.system('cls')

            # determine what happens after each round
            if outcome == Outcomes.WIN:
                player_score += 1
                self.ui.win_message()

            elif outcome == Outcomes.LOSE:
                cpu_score += 1
                self.ui.lose_message()

            else:
                self.ui.tie_message()

            self.ui.score_update(player_score, cpu_score)

        # fixme set win condition in UI
        self.ui.final_win_or_lose_message(player_score, cpu_score)
