"""Tests of the entry point in main.py, with a fake screen."""

import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

import pytest

from us_states_game import main as main_module
from us_states_game.states import State
from us_states_game.storage import load_states


class FakeTurtleScreen:
    """Stands in for TurtleScreen: scripted answers, no display."""

    instances: list["FakeTurtleScreen"] = []
    answers: Sequence[str | None] = []

    def __init__(self) -> None:
        self._answers = iter(self.answers)
        self.written: list[State] = []
        self.coordinates_enabled = False
        self.closed = False
        FakeTurtleScreen.instances.append(self)

    def ask_state_name(self, title: str, prompt: str) -> str | None:
        return next(self._answers)

    def write_state(self, state: State) -> None:
        self.written.append(state)

    def enable_click_coordinates(self) -> None:
        self.coordinates_enabled = True

    def close(self) -> None:
        self.closed = True


@pytest.fixture
def fake_screen(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> type[FakeTurtleScreen]:
    FakeTurtleScreen.instances = []
    monkeypatch.setattr(main_module, "TurtleScreen", FakeTurtleScreen)
    monkeypatch.chdir(tmp_path)
    return FakeTurtleScreen


def test_main_writes_states_to_learn_and_returns_zero(
    fake_screen: type[FakeTurtleScreen], tmp_path: Path
) -> None:
    fake_screen.answers = ["Ohio", "texas", "exit"]
    assert main_module.main([]) == 0
    lines = (tmp_path / "states_to_learn.csv").read_text(encoding="utf-8").splitlines()
    expected = [s.name for s in load_states() if s.name not in {"Ohio", "Texas"}]
    assert lines == ["state", *expected]
    assert len(expected) == 48


def test_main_closes_screen_after_game(fake_screen: type[FakeTurtleScreen]) -> None:
    fake_screen.answers = ["exit"]
    main_module.main([])
    assert fake_screen.instances[0].closed


def test_main_enables_click_coordinates_with_flag(
    fake_screen: type[FakeTurtleScreen],
) -> None:
    fake_screen.answers = ["exit"]
    main_module.main(["--show-coordinates"])
    assert fake_screen.instances[0].coordinates_enabled


def test_main_leaves_click_coordinates_off_by_default(
    fake_screen: type[FakeTurtleScreen],
) -> None:
    fake_screen.answers = ["exit"]
    main_module.main([])
    assert not fake_screen.instances[0].coordinates_enabled


def test_game_and_states_modules_do_not_import_turtle() -> None:
    code = (
        "import sys, us_states_game.game, us_states_game.states, "
        "us_states_game.storage; "
        "sys.exit(1 if 'turtle' in sys.modules else 0)"
    )
    result = subprocess.run([sys.executable, "-c", code], check=False)
    assert result.returncode == 0
