[English](Install) | **Dansk** | [Bahasa Melayu](Install.ms)

# Installation

Opret et lokalt virtuelt miljø med navnet `.venv`, opgradér `pip` og installér projektet med testværktøjet.

## Krav

- Python 3.13 eller nyere, med `tkinter` (Turtle kræver det)
- `git`
- Valgfrit: Doxygen til at bygge kildedokumentationen

## Windows PowerShell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game.git
cd 025-us-states-game
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux Debian

```bash
sudo apt install python3 python3-venv python3-tk git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game.git
cd 025-us-states-game
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## MacOS

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game.git
cd 025-us-states-game
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør

```bash
python -m us_states_game
```

Skriv et delstatsnavn i prompten; store og små bogstaver er ligegyldige. Skriv `exit` (eller tryk Annuller) for at stoppe. De delstater, du ikke navngav, skrives til `states_to_learn.csv` i den aktuelle mappe. Tilføj `--show-coordinates` for at udskrive koordinaterne for museklik.

![Et spil i gang: 14 af 50 delstater navngivet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/raw/branch/main/docs/images/game-in-progress.png)

## Kør testene

```bash
python -m pytest
```

Testene kræver ingen skærm.
