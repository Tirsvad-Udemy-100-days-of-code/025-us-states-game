"""Tests of the display-free dialog focus helpers in `turtle_screen`."""

from collections.abc import Callable, Sequence

from us_states_game.turtle_screen import DialogWidget, find_widgets, focus_dialog


class FakeWidget:
    """A Tk widget stand-in that records the calls made on it."""

    def __init__(self, tk_class: str, children: Sequence["FakeWidget"] = ()) -> None:
        self.tk_class = tk_class
        self.children = list(children)
        self.calls: list[str] = []

    def winfo_class(self) -> str:
        return self.tk_class

    def winfo_children(self) -> Sequence[DialogWidget]:
        return self.children

    def after(
        self, ms: int, func: Callable[[DialogWidget], None], widget: DialogWidget
    ) -> str:
        return ""

    def lift(self) -> None:
        self.calls.append("lift")

    def focus_force(self) -> None:
        self.calls.append("focus_force")


def test_find_widgets_returns_nested_matches_in_order() -> None:
    entry = FakeWidget("Entry")
    frame = FakeWidget("Frame", [entry])
    dialog = FakeWidget("Toplevel", [frame])
    root = FakeWidget("Tk", [FakeWidget("Canvas"), dialog])

    assert find_widgets(root, ("Entry", "TEntry")) == [entry]
    assert find_widgets(root, "Toplevel") == [dialog]


def test_focus_dialog_lifts_dialog_and_focuses_entry() -> None:
    entry = FakeWidget("Entry")
    dialog = FakeWidget("Toplevel", [FakeWidget("Frame", [entry])])
    root = FakeWidget("Tk", [dialog])

    focus_dialog(root)

    assert dialog.calls == ["lift", "focus_force"]
    assert entry.calls == ["focus_force"]


def test_focus_dialog_uses_newest_dialog() -> None:
    old = FakeWidget("Toplevel")
    new = FakeWidget("Toplevel")

    focus_dialog(FakeWidget("Tk", [old, new]))

    assert old.calls == []
    assert new.calls == ["lift", "focus_force"]


def test_focus_dialog_does_nothing_without_dialog() -> None:
    canvas = FakeWidget("Canvas")

    focus_dialog(FakeWidget("Tk", [canvas]))

    assert canvas.calls == []
