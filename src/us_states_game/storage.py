"""CSV input and output of the U.S. States Game, using the csv module.

@file storage.py
@brief Loads the states from CSV and saves the states to learn.

Uses the standard library `csv` module, not pandas (see ADR-0001).
"""

import csv
from collections.abc import Iterable
from pathlib import Path

from us_states_game.constants import (
    STATE_COLUMN,
    STATES_CSV_PATH,
    STATES_TO_LEARN_FILENAME,
    X_COLUMN,
    Y_COLUMN,
)
from us_states_game.states import State


def load_states(path: Path = STATES_CSV_PATH) -> list[State]:
    """Read the states and their map coordinates from a CSV file.

    @param path CSV file with the state, x and y columns.
    @return The states, in file order.
    """
    with path.open(newline="", encoding="utf-8") as file:
        return [
            State(row[STATE_COLUMN], int(row[X_COLUMN]), int(row[Y_COLUMN]))
            for row in csv.DictReader(file)
        ]


def save_states_to_learn(
    missing_states: Iterable[str],
    path: Path = Path(STATES_TO_LEARN_FILENAME),
) -> None:
    """Write the missing states to a one-column CSV file.

    @param missing_states Names of the states the player missed.
    @param path File to write; an existing file is replaced.
    """
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([STATE_COLUMN])
        writer.writerows([name] for name in missing_states)
