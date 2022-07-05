import logging

from entities import Entities
from outcomes import Outcomes

logger = logging.getLogger(__name__)


class Rules:
    def __init__(self, player: Entities, cpu: Entities):
        self.player = player
        self.cpu = cpu

    def winning_entity(self) -> Entities:
        """Return the winning Entity, regardless of order"""

        entity_set = {self.player, self.cpu}

        # paper vs rock
        if all(i in entity_set for i in {Entities.PAPER, Entities.ROCK}):
            return Entities.PAPER

        # paper vs scissors
        if all(i in entity_set for i in {Entities.PAPER, Entities.SCISSORS}):
            return Entities.SCISSORS

        # scissors vs rock
        if all(i in entity_set for i in {Entities.SCISSORS, Entities.ROCK}):
            return Entities.ROCK

        raise TypeError('Wrong Type')

    def get_winner(self) -> Outcomes:
        """Return win, lose, or tie"""
        if self.player == self.cpu:
            return Outcomes.TIE
        if self.player == self.winning_entity():
            return Outcomes.WIN
        return Outcomes.LOSE


if __name__ == "__main__":
    print(Rules(Entities.ROCK, Entities.PAPER).winning_entity())
