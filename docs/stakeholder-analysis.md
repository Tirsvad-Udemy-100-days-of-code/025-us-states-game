# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-002: Go | [b113e6e] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table and a conflict about the stand-in reviewer; set the domain to education; reviewed in autonomous mode, not independent | [a579509] |

---

## Purpose

Identify who is affected by the U.S. States Game project, who decides and who reviews, so each artifact can cite stable IDs. Method: Mendelow power/interest grid, concerns mapped to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A finished, correct, well-documented exercise delivered through a reviewed process |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy 100 Days of Code community | LOW | HIGH | Keep Informed | Readable, runnable code that keeps the assignment's function names, with README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies to install |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, reviews and accepts every artifact.
- **Keep Informed (S02):** cannot change scope but is the main consumer; their needs shape code naming and README.
- **Monitor (S03):** casual consumers; served by the public repository surface.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Game behaves as in the lectures | Functionality |
| CN-002 | S01 | Work traceable through plan, review and pull requests | Supportability |
| CN-003 | S02 | Readable code with the assignment's function names | Supportability |
| CN-004 | S02 | Easy to run from README instructions | Usability |
| CN-005 | S03 | Clear description, topics, README | Usability |
| CN-006 | S03 | No runtime dependencies to install | Supportability |
| CN-007 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's location | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat session | At plan acceptance and at the final summary | Plan, review records, run summary | All milestones |
| S02 | README, wiki (en, da, ms) | Once per release | Run instructions, screenshots | MIL-004 |
| S03 | Repository description, topics, README | Once per release | Repository surface | MIL-004 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-005] |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | [MIL-005] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| The assignment uses pandas, but viewers want no runtime dependencies | S02, S03 | Record the choice in an ADR; keep the assignment's function and variable names regardless of the library |
| Full process documents add weight to a small exercise | S01, S03 | Keep documents short; the repository surface (README, wiki) stays the first thing viewers see |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct game (CN-001) | [BC-001] Objectives 1, 3 |
| S01 | Process and traceability (CN-002) | [BC-001] Objective 4 |
| S02 | Comparable, runnable code (CN-003, CN-004) | [BC-001] Objectives 1, 2 |
| S03 | Clear repository surface (CN-005) | [BC-001] Objective 4 |
| S03 | No runtime dependencies to install (CN-006) | [BC-001] Success Criterion 6 |
| S01 | The project follows the common baseline of the framework (CN-007) | [BC-001] Objective 5 |

## Sign-Off

| Role | Stakeholder | Date | Decision |
| --- | --- | --- | --- |
| Product Owner | S01 | 2026-10-13 | Accepted in chat as part of the plan; reviewed by AI as stand-in for S01 (RC-002) |

The changes of the baseline milestone were accepted by the AI stand-in for S01 after the review record of this document (Go), autonomous, not independent.

---

[BC-001]: ./business-case.md
[b113e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/b113e6eacd12bb08045ecf6f7822837626a7b1f7
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[a579509]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/a5795093e1d293da9d29fced5cb24621b0a4c5bd
