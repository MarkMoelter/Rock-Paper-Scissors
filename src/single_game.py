import random

from src.entities import int_to_entity
from src.rules import Rules
from src.ui import UI


def single_game():
    start_message = UI().game_start_message()
    input_int = int(input(start_message))
    # get entities from integers
    player_entity = int_to_entity(input_int)
    cpu_entity = int_to_entity(random.randint(0, 2))

    print(f'You selected: {player_entity}')
    print(f'CPU selected: {cpu_entity}')

    outcome = Rules(
        player=player_entity,
        cpu=cpu_entity
    ).get_winner()
    print(f'The outcome is: {outcome}')

    return outcome
