# MIL-001 Baseline and repository setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-003: Go | [b113e6e] |

---

## Purpose

Decide whether the repository is ready to build in: tooling, layout, assignment assets, continuous integration (CI) and the public repository surface exist before any game code.

## Deliverable

A repository with `src/`, `tests/`, `docs/`, `.gitignore`, `pyproject.toml`, `constants.py`, the assignment assets, a `Doxyfile`, a README skeleton, a CI workflow, and a description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e ".[dev]"` and `pytest` run in a fresh `.venv` on Python 3.13 or newer (zero tests collected is acceptable) | Met | Not met |
| 2 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` and `docs/build` | Met | Not met |
| 3 | `doxygen Doxyfile` runs without error | Met | Not met |
| 4 | The repository description and at least 5 topics are visible on the git host | Met | Not met |
| 5 | The CI workflow file exists and installs and runs pytest | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4; Success criteria 3, 5, 6 | [BC-001] |

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
| 1 | Set repository description and topics | Set a one-sentence description and topics (`python`, `turtle-graphics`, `quiz-game`, `udemy`, `100-days-of-code`, `us-states`) through the git host API. The token is read from `.env` by the shell only; it is never imported, tested, printed or committed. Serves S03. | No | |
| 2 | Add .gitignore, pyproject.toml and project layout | Python `.gitignore`; `pyproject.toml` with `requires-python = ">=3.13"` and a `dev` extra with pytest; `src/` package and `tests/` folder. Constants live in `constants.py`. Serves the Business Case constraints. | No | |
| 3 | Add assignment assets | Unpack `50_states.csv` and `blank_states_img.gif` from the course zip into the package data folder. They are course-provided inputs the game needs at run time. | No | |
| 4 | Add Doxyfile | Configuration so `doxygen Doxyfile` builds the source reference from `src/` into `docs/build/doxygen`, with Python Doxygen comments (`##` and `@param`) supported. | No | |
| 5 | Add README skeleton and venv instructions | Create `README.md` from the framework template with every required section, including how to create a local `.venv` and run `python -m pip install --upgrade pip` on Windows PowerShell, Linux Debian and macOS. Filled in with screenshots in MIL-004. | No | |
| 6 | Add continuous integration workflow | A Gitea Actions workflow that sets up Python 3.13, installs the project with the dev extra and runs pytest, so the README Continuous integration section has something to describe. | No | |

---

[BC-001]: ../business-case.md
[b113e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/b113e6eacd12bb08045ecf6f7822837626a7b1f7
