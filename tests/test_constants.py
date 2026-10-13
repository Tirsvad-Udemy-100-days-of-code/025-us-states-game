"""Smoke test: the constants point at the assignment files that ship with the game."""

from us_states_game import constants


def test_data_files_exist() -> None:
    assert constants.STATES_CSV_PATH.is_file()
    assert constants.MAP_IMAGE_PATH.is_file()


def test_states_csv_has_all_states() -> None:
    lines = constants.STATES_CSV_PATH.read_text(encoding="utf-8").strip().splitlines()
    assert (
        lines[0]
        == f"{constants.STATE_COLUMN},{constants.X_COLUMN},{constants.Y_COLUMN}"
    )
    assert len(lines) - 1 == constants.NUMBER_OF_STATES
