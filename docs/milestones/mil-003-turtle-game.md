# MIL-003 Turtle game and entry point

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Claude (AI) for S01 | AI as stand-in for S01 | Task 7 added: CI found that importing turtle needs a Tk library the runner lacks; review RC-013: Go | [172778d] |
| 2026-10-13 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Task 8 added: the answer dialog lost keyboard focus after a wrong answer; review RC-015: Go | [0291b12] |

---

## Purpose

Decide whether the playable game works end to end: map, input prompts, drawn names, counter in the title, `exit` and the learning file.

## Deliverable

A runnable `main.py` entry point that plays the full game with Turtle, built on the tested core, with the click-coordinate helper from lecture 1.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python main.py` starts and shows the blank map titled "U.S. States Game" | Met | Not met |
| 2 | A correct guess writes the state name at its coordinates and increments the counter in the title | Met | Not met |
| 3 | A wrong guess re-opens the prompt without a crash | Met | Not met |
| 4 | Typing `exit` ends the game and writes `states_to_learn.csv` | Met | Not met |
| 5 | Guessing all 50 states ends the game | Met | Not met |
| 6 | The Turtle layer has a pytest test using a fake screen (no display needed) | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The UI is built on the tested game core |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2; Success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-13 - within the one-working-day duration constraint of [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set up screen, title and map image | Create the `screen`, set the title and register `blank_states_img.gif` as a shape (lecture 1), kept in a function with the assignment name. | No | |
| 2 | Add mouse click coordinate helper | `get_mouse_click_coor(x, y)` prints click coordinates and the screen stays open with `mainloop`, as in lecture 1. | No | |
| 3 | Implement the guess loop | While fewer than 50 states are guessed, prompt with `textinput`, title-case the answer, write the state at its coordinates and update the counter (lecture 2); `exit` breaks the loop (lecture 3). | No | |
| 4 | Add the entry point | `main.py` wires screen, loop and the learning-file export so `python main.py` runs the game after setup. | No | |
| 5 | Add UI test with a fake screen | Inject a fake screen and prompt into the loop to verify the flow without a display. | No | |
| 6 | Run the game manually | Run the real game once and note the result in the milestone review. | No | |
| 7 | Import turtle lazily so tests run without a Tk library | CI on the runner failed at test collection because `import turtle` needs `libtk8.6`. Import `turtle` when `TurtleScreen` is created, so importing the program and running its tests need no Tk library. Found after the first merge of this milestone. | No | |
| 8 | Keep keyboard focus in the answer dialog | After a wrong answer the reopened dialog had no keyboard focus, so the player had to click it. Lift the dialog and force focus onto it and its entry each time it opens. Found by S01 in manual play. | No | |

---

[BC-001]: ../business-case.md
[172778d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/172778d22b7d78fe91eb91b145055289c87ac208
[0291b12]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/0291b128845bb9a731465afbc1681809f7ba1687
