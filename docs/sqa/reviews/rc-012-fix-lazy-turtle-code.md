# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Claude (AI) for S01 | AI as stand-in for S01 | Initial review record: Go | pending |

---

## Artifact Under Review

- Instance reviewed: turtle_screen.py and tests/test_main.py changed by the CI fix (branch fix-ci-lazy-turtle)
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
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | ruff format and check clean; the one suppression (`# noqa: PLC0415`) carries its reason: Tk may be missing at import time. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | All signatures annotated incl. `-> None`; mypy --strict passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | N-A | No exception handling added; a missing data file raises to the caller. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No mutable defaults (Path defaults are immutable); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | Pass | No unmanaged resources; the window is closed in a `finally` in main(). |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Docstrings with @param/@return on public items. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | Pass | Click coordinates use `logging`; no print in the package. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No Design Class Diagram exists; the Protocol and TurtleScreen are recorded in the module docstrings. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | 34 tests; a new subprocess test blocks tkinter and imports the program; the suite also passes with tkinter blocked. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | mypy strict reports no issues. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependencies. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | Titles, prompts, font and sizes defined once in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | turtle is imported lazily inside TurtleScreen.__init__, so importing main and game needs no Tk library; game.py still depends on the Protocol. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | game.py loop, storage, screen and composition root each have one reason to change; the loop depends on the GameScreen Protocol and receives its implementation. |

## Overall Verdict

Go - Fix review: turtle is imported lazily so CI without a Tk library passes. Mandatory criteria pass (ruff, mypy --strict, 34 pytest tests, doxygen clean). CI failure cause: libtk8.6 missing on the runner.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
