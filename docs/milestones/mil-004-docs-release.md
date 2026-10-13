# MIL-004 Documentation, screenshots and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-006: Go | [b113e6e] |

---

## Purpose

Decide whether the repository is publishable for S02 and S03: README, source reference, screenshots and a three-language wiki.

## Deliverable

Completed README with screenshots, Doxygen comments verified and buildable, wiki pages in English, Danish and Bahasa Malaysia with screenshots, and a verified fresh-clone run.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `framework/scripts/check-readme.sh` passes | Met | Not met |
| 2 | `doxygen Doxyfile` builds without warnings about undocumented public functions | Met | Not met |
| 3 | The wiki has `Home`, `Install` and `Description` pages in `en`, `da` and `ms` and a `_Sidebar.md` | Met | Not met |
| 4 | README and wiki embed at least 2 screenshots of the running game | Met | Not met |
| 5 | A fresh clone follows the README and the game and tests run | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | There must be a running game to screenshot |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4; Success criteria 3, 4, 5 | [BC-001] |

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
| 1 | Capture screenshots of the running game | Take screenshots of the start screen and a game in progress from the real game, stored under `docs/images/`, used by README and wiki. Serves S02 and S03. | No | |
| 2 | Complete README | Fill every template section (requirements, set up for PowerShell, Debian and macOS, run, tests, continuous integration, source documentation, layout, license) and embed the screenshots. | No | |
| 3 | Review Doxygen comments and build | Verify every public function and constant has a Doxygen comment, run `doxygen Doxyfile`, and document the command in the README. | No | |
| 4 | Write the wiki in English, Danish and Bahasa Malaysia | Pages `Home`, `Install`, `Description` and `_Sidebar.md` under `wiki/` in the same layout as the TirSystem github-action wiki, each with `-da` and `-ms` variants and screenshots. | No | |
| 5 | Publish the wiki to the git host | Push the `wiki/` pages to the repository wiki on the git host. | No | |
| 6 | Verify from a fresh clone | Clone to a clean folder, follow the README, run the game and tests, and record the result. | No | |

---

[BC-001]: ../business-case.md
[b113e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/b113e6eacd12bb08045ecf6f7822837626a7b1f7
