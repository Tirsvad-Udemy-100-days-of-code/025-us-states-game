"""Tests of the guess loop and the end-of-game export in game.py."""

import csv
from collections.abc import Sequence
from pathlib import Path

from us_states_game.constants import ANSWER_PROMPT, NUMBER_OF_STATES
from us_states_game.game import play, run_game
from us_states_game.states import State

STATES = [State("Alabama", 139, -77), State("Ohio", 100, 20), State("Texas", -50, -120)]
ALL_STATES = [State(f"State {n}", n, -n) for n in range(NUMBER_OF_STATES)]


class FakeScreen:
    """Records what the loop asks and writes, and returns scripted answers."""

    def __init__(self, answers: Sequence[str | None]) -> None:
        self._answers = iter(answers)
        self.titles: list[str] = []
        self.prompts: list[str] = []
        self.written: list[State] = []

    def ask_state_name(self, title: str, prompt: str) -> str | None:
        self.titles.append(title)
        self.prompts.append(prompt)
        return next(self._answers)

    def write_state(self, state: State) -> None:
        self.written.append(state)


def read_names(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as file:
        return [row[0] for row in csv.reader(file)]


def test_play_writes_correct_guess_at_its_coordinates() -> None:
    screen = FakeScreen(["Ohio", "exit"])
    assert play(screen, STATES) == ["Ohio"]
    assert screen.written == [State("Ohio", 100, 20)]


def test_play_increments_counter_in_title_after_correct_guess() -> None:
    screen = FakeScreen(["ohio", "texas", "exit"])
    play(screen, STATES)
    assert screen.titles == [
        "0/50 States Correct",
        "1/50 States Correct",
        "2/50 States Correct",
    ]
    assert set(screen.prompts) == {ANSWER_PROMPT}


def test_play_uses_canonical_name_for_case_insensitive_guess() -> None:
    assert play(FakeScreen(["oHiO", "exit"]), STATES) == ["Ohio"]


def test_play_asks_again_without_writing_for_wrong_guess() -> None:
    screen = FakeScreen(["Atlantis", "exit"])
    assert play(screen, STATES) == []
    assert screen.written == []
    assert screen.titles == ["0/50 States Correct", "0/50 States Correct"]


def test_play_counts_duplicate_guess_once() -> None:
    screen = FakeScreen(["Ohio", "ohio", " OHIO ", "exit"])
    assert play(screen, STATES) == ["Ohio"]
    assert len(screen.written) == 1
    assert screen.titles[-1] == "1/50 States Correct"


def test_play_ends_on_exit_command() -> None:
    screen = FakeScreen(["exit"])
    assert play(screen, STATES) == []
    assert len(screen.titles) == 1


def test_play_ends_on_exit_command_in_any_case() -> None:
    assert play(FakeScreen(["Ohio", "EXIT"]), STATES) == ["Ohio"]


def test_play_ends_when_player_cancels() -> None:
    assert play(FakeScreen(["Ohio", None]), STATES) == ["Ohio"]


def test_play_ends_without_asking_again_when_all_states_are_guessed() -> None:
    screen = FakeScreen([state.name for state in ALL_STATES])
    assert len(play(screen, ALL_STATES)) == NUMBER_OF_STATES
    assert len(screen.titles) == NUMBER_OF_STATES


def test_run_game_writes_exactly_the_missing_states(tmp_path: Path) -> None:
    output = tmp_path / "states_to_learn.csv"
    missing = run_game(FakeScreen(["Ohio", "exit"]), STATES, output)
    assert missing == ["Alabama", "Texas"]
    assert read_names(output) == ["state", "Alabama", "Texas"]


def test_run_game_writes_header_only_when_all_states_guessed(tmp_path: Path) -> None:
    output = tmp_path / "states_to_learn.csv"
    screen = FakeScreen([state.name for state in ALL_STATES])
    assert run_game(screen, ALL_STATES, output) == []
    assert read_names(output) == ["state"]
