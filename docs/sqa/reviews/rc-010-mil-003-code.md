# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Claude (AI) for S01 | AI as stand-in for S01 | Initial review record: Go | [02b537e] |

---

## Artifact Under Review

- Instance reviewed: source and tests delivered by MIL-003 (branch mil-003-turtle-game)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

### QC-PY-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | PEP 8 casing; ruff N rules pass. `get_mouse_click_coor` keeps the assignment's name. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose; assignment names guessed_states and missing_states kept. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | ruff format and check clean, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | All signatures annotated incl. `-> None`; mypy --strict passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | N-A | No exception handling added; a missing data file raises to the caller. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable defaults (Path defaults are immutable); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | Pass | No unmanaged resources; the window is closed in a `finally` in main(). |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Docstrings with @param/@return on public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | Click coordinates use `logging`; no print in the package. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No Design Class Diagram exists; the Protocol and TurtleScreen are recorded in the module docstrings. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | 15 new tests with a fake screen and monkeypatched TurtleScreen; no display, network or order dependence. TurtleScreen itself is verified by the manual run. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | mypy strict reports no issues. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependencies. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | Titles, prompts, font and sizes defined once in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | Only turtle_screen.py imports turtle; game.py depends on a Protocol. game.py imports storage (stdlib csv file output) directly: accepted for a program of this size, noted as a stand-in decision. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | game.py loop, storage, screen and composition root each have one reason to change; the loop depends on the GameScreen Protocol and receives its implementation. |

## Overall Verdict

Go - Mandatory criteria pass for game.py, turtle_screen.py, main.py and their tests (ruff, mypy --strict, 33 pytest tests, doxygen without warnings). Manual run: the real window opened with the blank map and the prompt dialog titled 0/50 States Correct; the game process was then stopped.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[02b537e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/02b537e5384560a4e55fac137e8ad4fa236e6031
