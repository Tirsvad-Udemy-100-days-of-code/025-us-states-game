# MIL-002 Game core logic

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-004: Go | [b113e6e] |

---

## Purpose

Decide whether the game rules work and are tested without a display: loading states, checking guesses, finding missing states and writing the learning file.

## Deliverable

A display-free module with the game logic and pytest tests, plus an Architecture Decision Record (ADR) for the data library choice.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes with tests for load, guess matching, missing states and CSV export | Met | Not met |
| 2 | Guess matching is case-insensitive and ignores surrounding spaces (`ohio` matches `Ohio`) | Met | Not met |
| 3 | `states_to_learn.csv` lists exactly the 50 states minus those guessed, in one column `state` | Met | Not met |
| 4 | The logic imports no `turtle` module | Met | Not met |
| 5 | The ADR for the data library is `Accepted` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Layout, tooling and assets must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2, 3; Success criteria 1, 2, 6 | [BC-001] |

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
| 1 | Record ADR: csv module versus pandas | Decide whether to read `50_states.csv` with the standard library or pandas. S03 wants no runtime dependencies, S02 follows a pandas lecture. Record the decision and its consequences as an ADR. | No | |
| 2 | Load states data | Read `50_states.csv` into a structure keyed by state name with `x` and `y`, using paths and column names from `constants.py`. | No | |
| 3 | Check a guess | Match a typed answer to a state case-insensitively and return its coordinates, so the UI can write the name at that place (lecture 2). | No | |
| 4 | Find missing states and write states_to_learn.csv | Compute `missing_states` from all states and `guessed_states` and save them as `states_to_learn.csv` (lecture 3). | No | |
| 5 | Add pytest tests for the game core | Tests for load, guess, missing states and CSV output using a temporary directory; they must run without a display. | No | |

---

[BC-001]: ../business-case.md
[b113e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/b113e6eacd12bb08045ecf6f7822837626a7b1f7
