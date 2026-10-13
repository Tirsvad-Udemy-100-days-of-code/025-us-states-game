"""Game loop of the U.S. States Game, independent of any screen technology.

@file game.py
@brief Guess loop and the end-of-game export of the states to learn.

The loop talks to the player through the `GameScreen` port, so it runs under
test with a fake screen and no display.
"""

from collections.abc import Sequence
from pathlib import Path
from typing import Protocol

from us_states_game.constants import (
    ANSWER_PROMPT,
    EXIT_COMMAND,
    NUMBER_OF_STATES,
    STATES_TO_LEARN_FILENAME,
    TITLE_FORMAT,
)
from us_states_game.states import State, find_state, get_missing_states
from us_states_game.storage import save_states_to_learn


class GameScreen(Protocol):
    """What the game loop needs from the screen."""

    def ask_state_name(self, title: str, prompt: str) -> str | None:
        """Ask the player for a state name.

        @param title Title of the dialog, showing the progress.
        @param prompt Question shown to the player.
        @return The typed text, or None if the player cancelled.
        """
        ...

    def write_state(self, state: State) -> None:
        """Write the name of a state at its coordinates on the map.

        @param state The state to write.
        """
        ...


def play(screen: GameScreen, states: Sequence[State]) -> list[str]:
    """Run the guess loop until all states are guessed or the player exits.

    @param screen Screen used to ask for answers and to write names.
    @param states All states of the game.
    @return Names of the states guessed, in guessing order.
    """
    guessed_states: list[str] = []
    while len(guessed_states) < NUMBER_OF_STATES:
        title = TITLE_FORMAT.format(guessed=len(guessed_states), total=NUMBER_OF_STATES)
        answer = screen.ask_state_name(title, ANSWER_PROMPT)
        if answer is None or answer.strip().casefold() == EXIT_COMMAND:
            break
        state = find_state(answer, states)
        if state is None or state.name in guessed_states:
            continue
        screen.write_state(state)
        guessed_states.append(state.name)
    return guessed_states


def run_game(
    screen: GameScreen,
    states: Sequence[State],
    output_path: Path = Path(STATES_TO_LEARN_FILENAME),
) -> list[str]:
    """Play the game and save the states the player missed.

    @param screen Screen used to ask for answers and to write names.
    @param states All states of the game.
    @param output_path File that receives the states to learn.
    @return Names of the states not guessed.
    """
    guessed_states = play(screen, states)
    missing_states = get_missing_states(states, guessed_states)
    save_states_to_learn(missing_states, output_path)
    return missing_states
