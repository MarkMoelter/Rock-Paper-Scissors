from enum import Enum, auto


class Entities(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


# fixme hardcoded the integer values for each entity
def int_to_entity(_int):
    """Convert input strings to Entities"""
    entity_dict = {0: Entities.ROCK, 1: Entities.PAPER, 2: Entities.SCISSORS}
    return entity_dict[_int]
