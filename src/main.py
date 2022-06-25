import utils
from entities import Entities
from rules import Rules

if __name__ == '__main__':
    logger = utils.log_init()

    # generate instance of rules
    rule_object = Rules(player=Entities.ROCK, cpu=Entities.SCISSORS)
    winner = rule_object.get_winner()

    # log winner
    logger.debug(winner)
