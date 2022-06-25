from entities import Entities


class ObjectRules:
    rules = {
        (Entities.PAPER, Entities.ROCK): Entities.PAPER,
        (Entities.SCISSORS, Entities.PAPER): Entities.SCISSORS,
        (Entities.ROCK, Entities.SCISSORS): Entities.ROCK
    }

    def __init__(self, rules, player: Entities, cpu: Entities):
        self.player = player
        self.cpu = cpu

    def get_winner(self):
        if self.player == self.cpu:
            return 'Tie'

        # fixme the sets dont work, try lists and check if both elements are in list
        winner = ObjectRules.rules[{self.player, self.cpu}]


entity = ObjectRules(Entities.ROCK, Entities.PAPER)
print(entity.get_winner())
