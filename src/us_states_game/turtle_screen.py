"""Turtle implementation of the game screen.

@file turtle_screen.py
@brief The only module that uses turtle; draws the map and asks questions.

turtle is imported when `TurtleScreen` is created, not when this module is
imported, so the rest of the program and its tests need no Tk library.
"""

import logging

from us_states_game.constants import (
    LOGGER_NAME,
    MAP_SHAPE_NAME,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
    STATE_ALIGNMENT,
    STATE_FONT,
)
from us_states_game.states import State

logger = logging.getLogger(LOGGER_NAME)


def get_mouse_click_coor(x: float, y: float) -> None:
    """Log the coordinates of a mouse click on the map.

    @param x Horizontal coordinate of the click.
    @param y Vertical coordinate of the click.
    """
    logger.info("Clicked at x=%s, y=%s", x, y)


class TurtleScreen:
    """Game screen drawn with Turtle graphics; implements `GameScreen`."""

    def __init__(self) -> None:
        """Open the window with the blank map.

        turtle (and so Tk) is imported here, at runtime.
        """
        import turtle  # noqa: PLC0415  # deferred: Tk may be missing at import time

        self.screen = turtle.Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title(SCREEN_TITLE)
        self.screen.addshape(MAP_SHAPE_NAME)
        self._map = turtle.Turtle()
        self._map.shape(MAP_SHAPE_NAME)
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.penup()

    def ask_state_name(self, title: str, prompt: str) -> str | None:
        """Ask the player for a state name in a text dialog.

        @param title Title of the dialog.
        @param prompt Question shown to the player.
        @return The typed text, or None if the player cancelled.
        """
        answer: str | None = self.screen.textinput(title, prompt)
        return answer

    def write_state(self, state: State) -> None:
        """Write the state name on the map at its coordinates.

        @param state The state to write.
        """
        self._pen.goto(state.x, state.y)
        self._pen.write(state.name, align=STATE_ALIGNMENT, font=STATE_FONT)

    def enable_click_coordinates(self) -> None:
        """Log the coordinates of every mouse click on the map."""
        self.screen.onscreenclick(get_mouse_click_coor)

    def close(self) -> None:
        """Close the window."""
        self.screen.bye()
