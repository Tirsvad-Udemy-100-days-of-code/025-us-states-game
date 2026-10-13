"""Tests of the CSV input and output in storage.py."""

import csv
from pathlib import Path

from us_states_game.constants import NUMBER_OF_STATES, STATE_COLUMN
from us_states_game.states import State, get_missing_states
from us_states_game.storage import load_states, save_states_to_learn


def _read_rows(path: Path) -> list[list[str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.reader(file))


def test_load_states_returns_all_states() -> None:
    assert len(load_states()) == NUMBER_OF_STATES


def test_load_states_reads_alabama_coordinates() -> None:
    assert load_states()[0] == State("Alabama", 139, -77)


def test_load_states_reads_custom_path(tmp_path: Path) -> None:
    path = tmp_path / "states.csv"
    path.write_text("state,x,y\nOhio,10,-20\n", encoding="utf-8")
    assert load_states(path) == [State("Ohio", 10, -20)]


def test_save_states_to_learn_writes_header_and_states(tmp_path: Path) -> None:
    path = tmp_path / "learn.csv"
    save_states_to_learn(["Ohio", "Texas"], path)
    assert _read_rows(path) == [[STATE_COLUMN], ["Ohio"], ["Texas"]]


def test_save_states_to_learn_writes_only_header_when_nothing_missing(
    tmp_path: Path,
) -> None:
    path = tmp_path / "learn.csv"
    save_states_to_learn([], path)
    assert _read_rows(path) == [[STATE_COLUMN]]


def test_save_states_to_learn_lists_47_rows_after_three_guesses(
    tmp_path: Path,
) -> None:
    path = tmp_path / "learn.csv"
    missing = get_missing_states(load_states(), ["Alabama", "Ohio", "Texas"])
    save_states_to_learn(missing, path)
    assert len(_read_rows(path)) - 1 == NUMBER_OF_STATES - 3
