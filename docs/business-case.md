# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; review RC-001: Go | [b113e6e] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 5, success criterion 7, a scope item, a risk, an assumption and a constraint exception for the baseline milestone MIL-005; added the link definitions of the cited documents; set the domain to education; reviewed in autonomous mode, not independent | [a579509] |

---

## Executive Summary

Build the U.S. States Game from Udemy's *100 Days of Code* (Day 25) as a small, clean, tested Python project: a Turtle window shows a blank U.S. map, the player types state names, correct guesses appear at their map coordinates, and on exit the states the player missed are saved to `states_to_learn.csv`. The project also serves as a worked example of a well-run repository: planned in documents, built through reviewed pull requests, with a README, a Doxygen source reference and a three-language wiki. A later milestone, [MIL-005], brings the finished project to the baseline of the framework.

## Methodological and Standards Foundation

Documents follow the SQA and QC framework mounted at `framework/` (artifact registry, QC checklists, review records). Quality characteristics are tagged with ISO/IEC 25010:2023. Code follows the `coding-conventions` skill (Python) and the layering of the `clean-architecture` skill where it fits a program of this size.

## Problem Statement

The course assignment is delivered as three lecture descriptions and a zip with a blank `main.py`. A participant who only follows the lectures ends with one untested script. Other course participants and repository viewers have no readable, runnable, documented reference solution to compare against, and the author has no repeatable example of a planned and reviewed delivery.

## Business Opportunity

A small, finished project is cheap to complete and makes a good public reference: course participants can compare solutions, viewers can borrow the repository structure (tests, continuous integration (CI), docs, wiki) for their own work.

## Objectives

1. Deliver a runnable U.S. States Game that meets the three lectures' behaviour (map, guess checking, exit and `states_to_learn.csv`).
2. Keep the assignment's vocabulary in the code (`screen`, `data`, `states`, `guessed_states`, `missing_states`, `states_to_learn.csv`) so participants can compare.
3. Cover the game logic with automated pytest tests that run without a display.
4. Publish the repository with a description, topics, README, Doxygen configuration and a wiki in English, Danish and Bahasa Malaysia, all with screenshots.
5. Bring the finished project to the common baseline of the framework: the adopted framework release, the wiki in the framework's location `docs/wiki/` with its page names, the README in the framework template, complete licence metadata, a traceability matrix and review records for the changed documents ([MIL-005]).

## Scope

### In Scope

- The game as described in the three lectures: map image, `50_states.csv`, case-insensitive guess, counter in the title, `exit` command, `states_to_learn.csv`.
- Python 3.13 or newer, `venv`, `pyproject.toml`, `constants.py`, `src/` and `tests/` layout, Python `.gitignore`.
- pytest tests, a continuous integration workflow, Doxygen comments and `Doxyfile`.
- README (given template) with screenshots, wiki in three languages with screenshots.
- Repository description and topics on the git host; one branch and pull request per step.
- The baseline milestone [MIL-005]: framework release, wiki moved to `docs/wiki/`, README in the framework template, licence metadata, traceability matrix and review records. It changes no behaviour of the game.

### Out of Scope

- Other countries or subjects (mentioned in the lecture only as an idea).
- A packaged installer, a web version, scoring, timers or persistent high scores.
- Runtime dependencies beyond what the assignment needs.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-005].

## Expected Benefits

### Tangible Benefits

- A working, tested game and a reproducible way to run and test it.
- A repository others can clone and run from README instructions alone.

### Intangible Benefits

- A reusable reference for how a small course project is planned, reviewed and documented.
- Practice with the framework's plan, review and pull-request flow.

## Strategic Alignment

Supports the author's course progress in the 100 Days of Code bootcamp and the habit of delivering each exercise as a reviewed, documented repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game behaviour | All behaviours of the three lectures work | Manual run and screenshot per behaviour; checklist in the final milestone |
| 2 | Automated tests | 100 % of tests pass, no display needed | `pytest` exit code 0, locally and in CI |
| 3 | Run-from-README | A fresh clone runs the game and tests with README steps only | Fresh clone walk-through on the author's machine |
| 4 | Documentation | README sections complete; wiki has en, da, ms pages with screenshots | `framework/scripts/check-readme.sh` and `check-languages.sh` pass |
| 5 | Repository | Description and at least 5 topics set | Repository page shows them |
| 6 | Dependencies | No runtime dependency beyond the standard library and what the assignment names (pandas) | `pyproject.toml` review |
| 7 | The baseline milestone is done (objective 5) | Wiki pages in 3 languages in `docs/wiki/`, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the CI checks of the pull request of [MIL-005] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Turtle needs a display, so tests and CI cannot open a window | Untestable game | Keep game logic in pure functions in a separate module; the Turtle layer is thin and tested with a fake screen |
| Pandas is heavy for a 50-row comma-separated values (CSV) file | Violates "no needless runtime dependencies" for S03 | Record the decision in an Architecture Decision Record (ADR); use the standard `csv` module unless the participant-facing assignment requires pandas (see Assumptions) |
| Git host token or API unavailable | Description, topics or issues cannot be set | Stop and report; the work in the repository is not blocked |
| Screenshots need a graphical session | Documentation incomplete | Capture on the author's desktop with the running game; stop and report if impossible |
| Credentials in `.env` leak | Secret exposure | `.env` is git-ignored, never imported, never printed |
| The documents of the baseline milestone [MIL-005] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- The Product Owner, developer and reviewer is S01 (see [SA-001]); no independent reviewer exists, so reviews in autonomous mode are recorded as not independent.
- Course participants (S02) and repository viewers (S03) are not interviewed; their needs are as stated in the request.
- The assignment's `50_states.csv` and `blank_states_img.gif` from the course zip may be committed under `src/`.
- Pandas is optional: the assignment uses it, but the standard library `csv` module is enough (decided in an ADR in the first build milestone).
- The baseline milestone [MIL-005] is finished within one week of its own start, 2026-11-15, by 2026-11-22. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Constraints

- Python 3.13 or newer; `venv`; `pytest`; constants in `constants.py`; configuration in `pyproject.toml`.
- Layout `src/`, `tests/`, `docs/`.
- Doxygen comments in source; a `Doxyfile`.
- Wiki in three languages (English, Danish, Bahasa Malaysia) modelled on `https://git.tirsystem.com/TirSystem/github-action/wiki`.
- Tokens come from `.env` for personal use only; they are not tested, imported or committed.
- Git host: `https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code` (organisation), repository `025-us-states-game`.
- Duration: one working day.
- The baseline milestone [MIL-005] is the exception to the duration of one working day and to the rule of one reviewer: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one day of the author's time; no licence or hosting cost (qualitative, the project is an exercise) | A finished reference project and a reusable repository structure (qualitative) |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer, reviewer: a finished, correct, reviewed exercise |
| S02 | Course participants: readable, runnable code with the assignment's names and README instructions |
| S03 | Repository viewers: clear description, topics, README, no runtime dependencies |

## Recommendation

Proceed — the scope is small, fully specified by the lectures, and low risk.

---

[b113e6e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/b113e6eacd12bb08045ecf6f7822837626a7b1f7
[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[a579509]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/a5795093e1d293da9d29fced5cb24621b0a4c5bd
