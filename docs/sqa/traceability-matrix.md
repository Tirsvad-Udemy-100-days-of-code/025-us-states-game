# Traceability Matrix: U.S. States Game

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [ADR-0001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the review records of the baseline (autonomous, not independent) | [a579509] |

---

## Purpose

Tracks backward and forward links between the artifact instances of U.S. States Game so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-016] (Go, re-review of the whole document), [RC-001] (Go, the first review) |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-017] (Go, re-review of the whole document), [RC-002] (Go, the first review) |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-018] (Go, review of the whole document; the plan had no review record before) |
| [MIL-001] | Milestone / Gateway | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-019] (Go, re-review after the metadata change), [RC-003] (Go, the first review) |
| [MIL-002] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-001] | [MIL-003] | [RC-020] (Go, re-review after the metadata change), [RC-004] (Go, the first review) |
| [MIL-003] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-021] (Go, re-review after the metadata change), [RC-005], [RC-013], [RC-015] |
| [MIL-004] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-022] (Go, re-review after the metadata change), [RC-006], [RC-011] |
| [MIL-005] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-004] | - | [RC-023] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-005] | - | [RC-024] (Go-with-conditions) |
| [ADR-0001] | Architecture Decision Record | - | - | [BC-001], [SA-001], [MIL-002] | `src/us_states_game/storage.py` | [RC-008] |
| Constants, package marker, smoke tests, `pyproject.toml` and `.gitea/workflows/run-tests.yml` of MIL-001 | Python Source Code and CI Workflow | - | - | [MIL-001] | - | [RC-007] |
| `states.py`, `storage.py` and their tests | Python Source Code | - | - | [MIL-002], [ADR-0001] | - | [RC-009] |
| `game.py`, `turtle_screen.py`, `main.py` and their tests | Python Source Code | - | - | [MIL-003] | - | [RC-010], [RC-012], [RC-014] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] (criteria 1 to 3), [MIL-003] (criteria 1 to 5) | - | - | Covered |
| CN-002 | [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | - | - | Covered |
| CN-003 | [MIL-002], [MIL-003] | - | - | Covered |
| CN-004 | [MIL-001] (task 5), [MIL-004] (criteria 1 and 5) | - | - | Covered |
| CN-005 | [MIL-001] (criterion 4), [MIL-004] (criteria 1 to 4) | - | - | Covered |
| CN-006 | [MIL-001] (criterion 1), [MIL-002] (criterion 4) | [ADR-0001] | - | Covered |
| CN-007 | [MIL-005] (criteria 1, 3, 4 and 5) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.
- The source code and the workflow are reviewed in the records RC-007, RC-009, RC-010, RC-012 and RC-014 and not again in [MIL-005], which changes no source file. These records and this matrix have no QC checklist for themselves and are not reviewed.
- The domain of the Business Case, Stakeholder Analysis, Project Plan and milestones is `education` since [MIL-005]; the earlier review records state the former domain `it` as it was at the time.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[ADR-0001]: ../adr/adr-0001-csv-module-over-pandas.md
[MIL-001]: ../milestones/mil-001-baseline-setup.md
[MIL-002]: ../milestones/mil-002-game-core.md
[MIL-003]: ../milestones/mil-003-turtle-game.md
[MIL-004]: ../milestones/mil-004-docs-release.md
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-mil-004.md
[RC-007]: ./reviews/rc-007-mil-001-code.md
[RC-008]: ./reviews/rc-008-adr-0001.md
[RC-009]: ./reviews/rc-009-mil-002-code.md
[RC-010]: ./reviews/rc-010-mil-003-code.md
[RC-011]: ./reviews/rc-011-mil-004-rereview.md
[RC-012]: ./reviews/rc-012-fix-lazy-turtle-code.md
[RC-013]: ./reviews/rc-013-mil-003-rereview.md
[RC-014]: ./reviews/rc-014-focus-dialog-code.md
[RC-015]: ./reviews/rc-015-mil-003-rereview-2.md
[RC-016]: ./reviews/rc-016-business-case-baseline.md
[RC-017]: ./reviews/rc-017-stakeholder-analysis-baseline.md
[RC-018]: ./reviews/rc-018-project-plan-baseline.md
[RC-019]: ./reviews/rc-019-milestone-001-baseline.md
[RC-020]: ./reviews/rc-020-milestone-002-baseline.md
[RC-021]: ./reviews/rc-021-milestone-003-baseline.md
[RC-022]: ./reviews/rc-022-milestone-004-baseline.md
[RC-023]: ./reviews/rc-023-milestone-005.md
[RC-024]: ./reviews/rc-024-wiki.md
[a579509]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/a5795093e1d293da9d29fced5cb24621b0a4c5bd
