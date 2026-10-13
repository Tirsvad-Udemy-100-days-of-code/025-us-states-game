"""Entry point of the U.S. States Game and its composition root.

@file main.py
@brief Wires the Turtle screen, the states and the game loop together.
"""

import argparse
import logging
from collections.abc import Sequence

from us_states_game.game import run_game
from us_states_game.storage import load_states
from us_states_game.turtle_screen import TurtleScreen


def main(argv: Sequence[str] | None = None) -> int:
    """Play the game once.

    @param argv Command line arguments; defaults to `sys.argv[1:]`.
    @return Process exit code, 0 on success.
    """
    parser = argparse.ArgumentParser(description="U.S. States Game")
    parser.add_argument(
        "--show-coordinates",
        action="store_true",
        help="log the coordinates of every mouse click on the map",
    )
    args = parser.parse_args(argv)

    states = load_states()
    screen = TurtleScreen()
    if args.show_coordinates:
        logging.basicConfig(level=logging.INFO)
        screen.enable_click_coordinates()
    try:
        run_game(screen, states)
    finally:
        screen.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
