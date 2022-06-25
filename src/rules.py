from ui import UI
from entities import Entities


class WinConditions:
    def __init__(self, player, cpu):
        self.player = player
        self.cpu = cpu

    def tie(self):
        if self.player == self.cpu:
            return True



