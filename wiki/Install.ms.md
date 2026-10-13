[English](Install) | [Dansk](Install.da) | **Bahasa Melayu**

# Pemasangan

Cipta persekitaran maya tempatan bernama `.venv`, naik taraf `pip` dan pasang projek dengan alat ujiannya.

## Keperluan

- Python 3.13 atau lebih baharu, dengan `tkinter` (Turtle memerlukannya)
- `git`
- Pilihan: Doxygen untuk membina dokumentasi sumber

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

## Jalankan

```bash
python -m us_states_game
```

Taip nama negeri pada gesaan; huruf besar atau kecil tidak penting. Taip `exit` (atau tekan Cancel) untuk berhenti. Negeri yang tidak anda namakan ditulis ke `states_to_learn.csv` dalam folder semasa. Tambah `--show-coordinates` untuk mencetak koordinat klik tetikus.

![Permainan sedang berjalan: 14 daripada 50 negeri dinamakan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-us-states-game/raw/branch/main/docs/images/game-in-progress.png)

## Jalankan ujian

```bash
python -m pytest
```

Ujian tidak memerlukan paparan.
