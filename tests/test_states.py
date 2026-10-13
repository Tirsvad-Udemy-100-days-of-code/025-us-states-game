"""Tests of the pure game logic in states.py."""

from us_states_game.states import State, find_state, get_missing_states

STATES = [State("Alabama", 139, -77), State("Ohio", 100, 20), State("Texas", -50, -120)]


def test_find_state_matches_exact_name() -> None:
    assert find_state("Ohio", STATES) == State("Ohio", 100, 20)


def test_find_state_ignores_case() -> None:
    assert find_state("oHiO", STATES) == State("Ohio", 100, 20)


def test_find_state_ignores_surrounding_whitespace() -> None:
    assert find_state("  ohio \n", STATES) == State("Ohio", 100, 20)


def test_find_state_returns_none_for_unknown_answer() -> None:
    assert find_state("Atlantis", STATES) is None


def test_find_state_returns_none_for_empty_answer() -> None:
    assert find_state("", STATES) is None


def test_find_state_returns_none_for_blank_answer() -> None:
    assert find_state("   ", STATES) is None


def test_get_missing_states_keeps_order_of_states() -> None:
    assert get_missing_states(STATES, ["Ohio"]) == ["Alabama", "Texas"]


def test_get_missing_states_is_empty_when_all_guessed() -> None:
    assert get_missing_states(STATES, ["Texas", "Ohio", "Alabama"]) == []


def test_get_missing_states_returns_all_when_none_guessed() -> None:
    assert get_missing_states(STATES, []) == ["Alabama", "Ohio", "Texas"]
