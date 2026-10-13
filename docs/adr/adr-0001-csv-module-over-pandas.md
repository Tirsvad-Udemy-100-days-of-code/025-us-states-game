# Read the states with the csv module

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-008: Go | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lectures read `50_states.csv` with pandas (`pandas.read_csv`, a DataFrame, then `DataFrame.to_csv` for `states_to_learn.csv`). The file has 50 rows and three columns (`state`, `x`, `y`). [BC-001] sets the constraint "avoid adding runtime dependencies unless they are needed", and [SA-001] records that S03 wants no runtime dependencies while S02 wants the assignment's function and variable names.

Options evaluated:

1. **pandas**: matches the lectures literally; adds a large runtime dependency (with NumPy) for 50 rows and makes installation and CI slower.
2. **Standard library `csv` module**: no dependency; a few more lines to read and write; the assignment's names (`data`, `states`, `guessed_states`, `missing_states`) can be kept.

## Decision

Read and write the CSV files with the standard library `csv` module, and keep the assignment's names for variables and functions. pandas is not a runtime dependency.

## Consequences

**Positive:**

- The game has no runtime dependencies, so S03 installs nothing and CI is fast.
- The game logic is plain functions over `str` and `int`, easy to test without a display.

**Negative:**

- The code differs from the lecture's pandas calls, so S02 compares by names and behaviour, not by line.
- Reading and writing the CSV takes a few more lines than `read_csv` and `to_csv`.

## Affected Artifacts

- [BC-001] - Success criterion 6 (no runtime dependency beyond the standard library) is met without exception.
- [SA-001] - Resolves the S02 and S03 conflict in favour of no runtime dependency.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
