**English** | [Dansk](Description.da) | [Bahasa Melayu](Description.ms)

# Description

The game follows the three lectures of day 25. This page explains how the code is built.

## Game rules

- The window shows the blank map from `blank_states_img.gif`.
- The prompt title shows how many states are named, for example `14/50 States Correct`.
- An answer is matched to a state without regard to case or surrounding spaces.
- A correct state is written on the map at its `x` and `y` from `50_states.csv`; a wrong or repeated answer asks again.
- `exit` or Cancel ends the game; the states not named are saved to `states_to_learn.csv`.

## Modules

| Module | Responsibility |
| --- | --- |
| `constants.py` | Every constant: titles, file names, column names, limits |
| `states.py` | The rules: `State`, `find_state`, `get_missing_states`; no files, no screen |
| `storage.py` | Reads `50_states.csv` and writes `states_to_learn.csv` with the standard library `csv` module |
| `game.py` | The guess loop `play` and `run_game`, working through a `GameScreen` protocol |
| `turtle_screen.py` | The only module that imports `turtle`: map, prompt, state names, click coordinates |
| `main.py` | Entry point that connects the parts |

## Tests, CI and documentation

- `python -m pytest` runs the tests with a fake screen, so no window opens.
- `.gitea/workflows/run-tests.yml` runs ruff, mypy, yamllint and pytest on every push and pull request.
- `doxygen Doxyfile` builds the source documentation into `docs/build/doxygen`.

```bash
python -m pytest
doxygen Doxyfile
```
