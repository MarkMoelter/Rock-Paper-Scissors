import unittest

from entities import Entities
from outcomes import Outcomes
from rules import Rules


class TestRules(unittest.TestCase):
    def test_winning_entities(self):
        """Check the winning entities"""
        assert Rules(Entities.ROCK, Entities.PAPER).winning_entity() == Entities.PAPER
        assert Rules(Entities.SCISSORS, Entities.PAPER).winning_entity() == Entities.SCISSORS
        assert Rules(Entities.ROCK, Entities.SCISSORS).winning_entity() == Entities.ROCK

    def test_get_winner(self):
        """Check wins, losses, and ties"""

        # test wins
        assert Rules(Entities.PAPER, Entities.ROCK).get_winner() == Outcomes.WIN
        assert Rules(Entities.SCISSORS, Entities.PAPER).get_winner() == Outcomes.WIN
        assert Rules(Entities.ROCK, Entities.SCISSORS).get_winner() == Outcomes.WIN

        # test losses
        assert Rules(Entities.ROCK, Entities.PAPER).get_winner() == Outcomes.LOSE
        assert Rules(Entities.PAPER, Entities.SCISSORS).get_winner() == Outcomes.LOSE
        assert Rules(Entities.SCISSORS, Entities.ROCK).get_winner() == Outcomes.LOSE

        # test ties
        assert Rules(Entities.ROCK, Entities.ROCK).get_winner() == Outcomes.TIE
        assert Rules(Entities.PAPER, Entities.PAPER).get_winner() == Outcomes.TIE
        assert Rules(Entities.SCISSORS, Entities.SCISSORS).get_winner() == Outcomes.TIE


if __name__ == '__main__':
    unittest.main()
