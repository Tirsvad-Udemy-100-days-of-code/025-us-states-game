"""Turtle implementation of the game screen.

@file turtle_screen.py
@brief The only module that uses turtle; draws the map and asks questions.

turtle is imported when `TurtleScreen` is created, not when this module is
imported, so the rest of the program and its tests need no Tk library.
"""

import logging
from collections.abc import Callable, Sequence
from typing import Protocol

from us_states_game.constants import (
    DIALOG_ENTRY_CLASSES,
    DIALOG_FOCUS_DELAY_MS,
    DIALOG_TOPLEVEL_CLASS,
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


class DialogWidget(Protocol):
    """The part of a Tk widget that the dialog focus helpers use."""

    def winfo_class(self) -> str:
        """Return the Tk class name of the widget."""
        ...

    def winfo_children(self) -> Sequence["DialogWidget"]:
        """Return the child widgets."""
        ...

    def after(
        self, ms: int, func: Callable[["DialogWidget"], None], widget: "DialogWidget"
    ) -> str:
        """Call func(widget) once after ms milliseconds; return the timer id."""
        ...

    def lift(self) -> None:
        """Raise the widget above its siblings."""
        ...

    def focus_force(self) -> None:
        """Give the widget the keyboard focus, even if the app has none."""
        ...


def find_widgets(
    root: DialogWidget, tk_class: str | tuple[str, ...]
) -> list[DialogWidget]:
    """Find all descendants of a widget whose Tk class is one of the given.

    @param root Widget whose descendants are searched.
    @param tk_class One Tk class name, or a tuple of them.
    @return Matching descendants in creation order, depth first.
    """
    classes = (tk_class,) if isinstance(tk_class, str) else tk_class
    found: list[DialogWidget] = []
    for child in root.winfo_children():
        if child.winfo_class() in classes:
            found.append(child)
        found.extend(find_widgets(child, classes))
    return found


def focus_dialog(root: DialogWidget) -> None:
    """Raise the newest dialog under root and give its entry the keyboard focus.

    Does nothing if no dialog is open.

    @param root The Tk root window of the game.
    """
    dialogs = find_widgets(root, DIALOG_TOPLEVEL_CLASS)
    if not dialogs:
        return
    dialog = dialogs[-1]
    dialog.lift()
    dialog.focus_force()
    entries = find_widgets(dialog, DIALOG_ENTRY_CLASSES)
    if entries:
        entries[0].focus_force()


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
        # The dialog is modal, so focus is claimed from a timer that fires while
        # it waits; without it Windows leaves the focus on another window.
        root: DialogWidget = self.screen.getcanvas().winfo_toplevel()
        root.after(DIALOG_FOCUS_DELAY_MS, focus_dialog, root)
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
