import logging

from entities import Entities
from outcomes import Outcomes

logger = logging.getLogger(__name__)


class Rules:
    def __init__(self, player: Entities, cpu: Entities):
        self.player = player
        self.cpu = cpu

    def __winning_entity(self):
        """Return the winning Entity, regardless of order"""
        # paper vs rock
        if self.player in {Entities.PAPER, Entities.ROCK} and self.cpu in {Entities.PAPER, Entities.ROCK}:
            return Entities.PAPER
        # paper vs scissors
        elif self.player in {Entities.PAPER, Entities.SCISSORS} and self.cpu in {Entities.PAPER, Entities.SCISSORS}:
            return Entities.SCISSORS
        # scissors vs rock
        elif self.player in {Entities.SCISSORS, Entities.ROCK} and self.cpu in {Entities.SCISSORS, Entities.ROCK}:
            return Entities.ROCK
        raise TypeError('Wrong Type')

    def get_winner(self):
        """Return win, lose, or tie"""
        if self.player == self.cpu:
            return Outcomes.TIE
        if self.player == self.__winning_entity():
            return Outcomes.WIN
        return Outcomes.LOSE
