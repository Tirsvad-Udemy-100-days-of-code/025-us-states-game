[English](Description) | **Dansk** | [Bahasa Melayu](Description.ms)

# Beskrivelse

Spillet følger de tre lektioner fra dag 25. Denne side forklarer, hvordan koden er bygget.

## Spilregler

- Vinduet viser det blanke kort fra `blank_states_img.gif`.
- Promptens titel viser, hvor mange delstater der er navngivet, for eksempel `14/50 States Correct`.
- Et svar matches med en delstat uden hensyn til store og små bogstaver eller mellemrum omkring.
- En rigtig delstat skrives på kortet ved sin `x` og `y` fra `50_states.csv`; et forkert eller gentaget svar spørger igen.
- `exit` eller Annuller afslutter spillet; de delstater, der ikke er navngivet, gemmes i `states_to_learn.csv`.

## Moduler

| Modul | Ansvar |
| --- | --- |
| `constants.py` | Alle konstanter: titler, filnavne, kolonnenavne, grænser |
| `states.py` | Reglerne: `State`, `find_state`, `get_missing_states`; ingen filer, ingen skærm |
| `storage.py` | Læser `50_states.csv` og skriver `states_to_learn.csv` med standardbibliotekets `csv`-modul |
| `game.py` | Gætteløkken `play` og `run_game` via en `GameScreen`-protokol |
| `turtle_screen.py` | Det eneste modul, der importerer `turtle`: kort, prompt, delstatsnavne, klikkoordinater |
| `main.py` | Indgangspunkt, der forbinder delene |

## Tests, CI og dokumentation

- `python -m pytest` kører testene med en falsk skærm, så intet vindue åbnes.
- `.gitea/workflows/run-tests.yml` kører ruff, mypy, yamllint og pytest ved hvert push og hver pull request.
- `doxygen Doxyfile` bygger kildedokumentationen i `docs/build/doxygen`.

```bash
python -m pytest
doxygen Doxyfile
```
