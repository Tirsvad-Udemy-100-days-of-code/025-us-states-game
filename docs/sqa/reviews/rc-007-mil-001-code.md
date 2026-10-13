# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [QC-PY-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Claude (AI) for S01 | AI as stand-in for S01 | Initial review record: Go | [22f19c1] |

---

## Artifact Under Review

- Instance reviewed: source and workflow files delivered by MIL-001 (branch mil-001-baseline-setup)
- Checklist used: [QC-PY-001], [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the same AI)

## Checklist Results

### QC-PY-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) (Mandatory) | Pass | Constants are UPPER_SNAKE, functions snake_case; ruff rule set N passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes (Mandatory) | Pass | Names state purpose (STATES_TO_LEARN_FILENAME, NUMBER_OF_STATES). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions (Mandatory) | Pass | `ruff format` leaves files unchanged and `ruff check` passes with no suppressions; configured in pyproject.toml. |
| 4 | Every function and method signature is type-annotated, including `-> None` (Mandatory) | Pass | Both test functions are annotated `-> None`; `mypy --strict` passes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) (Mandatory) | N-A | No exception handling in this milestone's code. |
| 6 | No mutable default arguments and no shadowed builtins (Mandatory) | Pass | No function arguments with defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers (Mandatory) | Pass | Tests read the CSV with `Path.read_text`, which closes the file. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Module docstrings and `##` Doxygen comments on every constant. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output (Mandatory) | N-A | No logging or output in this milestone's code. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded (Mandatory) | N-A | No classes or operations; no Design Class Diagram exists for constants. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network (Mandatory) | Pass | tests/test_constants.py: two tests named for the behaviour; no order or network dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | `python -m mypy` strict mode reports no issues. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependencies; dev extra lists pytest, ruff, mypy and yamllint with lower bounds. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike (Mandatory) | Pass | Each path, file name and limit is defined once in constants.py. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles (Mandatory) | Pass | The package has no imports of UI or framework code. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations (Mandatory) | Pass | One module with one reason to change; no classes. |

### QC-YML-001

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping (Mandatory) | Pass | yamllint (PyYAML safe loader) parses the workflow and reports no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces (Mandatory) | Pass | 2-space indentation, LF endings enforced by .gitattributes, yamllint default rules pass. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments (Mandatory) | Pass | `yamllint .gitea .yamllint` passes with the committed .yamllint, no disable comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` (Mandatory) | Pass | `python-version: "3.13"` is quoted; `on` is allowed by the yamllint truthy rule for workflows. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it (Mandatory) | Pass | Plain mappings, sequences and strings only. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool (Mandatory) | Pass | No secret in the file; the workflow needs none. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it (Mandatory) | Pass | Each `run:` value has at most 2 lines. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) (Mandatory) | Pass | No repeated block. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them (Mandatory) | Pass | No anchors or aliases. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated (Optional) | N-A | No published schema is checked; the workflow is exercised by the host runner. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded (Mandatory) | Pass | Header comment states purpose, reader and where the design is recorded. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) (Mandatory) | Pass | kebab-case keys (`runs-on`, `timeout-minutes`) throughout. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters (Optional) | Pass | The `run:` block scalars use `|`; trailing newline does not matter. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository (Optional) | Pass | `run-tests.yml` is lowercase kebab-case with the .yml extension. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool (Optional) | N-A | The runner is not available locally; yamllint is the local check. |

## Overall Verdict

Go - Mandatory criteria of both checklists pass for the files delivered by MIL-001: constants module, package marker, smoke tests, pyproject and the workflow.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[22f19c1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/commit/22f19c188be10b216cc9da6f6f5ff9413aecd285
