"""Pure domain logic of the U.S. States Game: states, answers and misses.

@file states.py
@brief State model, answer matching and the list of missing states.

Nothing here reads files or touches the screen, so the rules run under test
with no display and no file system.
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class State:
    """A U.S. state and the position of its name on the map.

    @param name Name of the state, for example "Ohio".
    @param x Horizontal map coordinate of the state.
    @param y Vertical map coordinate of the state.
    """

    name: str
    x: int
    y: int


def find_state(answer: str, states: Iterable[State]) -> State | None:
    """Find the state the player named, ignoring case and surrounding spaces.

    @param answer Text the player typed.
    @param states The states to search.
    @return The matching state, or None if the answer matches no state.
    """
    wanted = answer.strip().casefold()
    if not wanted:
        return None
    for state in states:
        if state.name.casefold() == wanted:
            return state
    return None


def get_missing_states(
    states: Iterable[State], guessed_states: Iterable[str]
) -> list[str]:
    """List the names of the states the player did not guess.

    @param states All states of the game, in the order to report them.
    @param guessed_states Names of the states the player guessed.
    @return Names of the states not guessed, in the order of `states`.
    """
    guessed = set(guessed_states)
    return [state.name for state in states if state.name not in guessed]
