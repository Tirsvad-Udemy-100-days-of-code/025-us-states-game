[English](Description) | [Dansk](Description.da) | **Bahasa Melayu**

# Penerangan

Permainan ini mengikut tiga kuliah hari 25. Halaman ini menerangkan cara kod dibina.

## Peraturan permainan

- Tetingkap memaparkan peta kosong daripada `blank_states_img.gif`.
- Tajuk gesaan menunjukkan bilangan negeri yang dinamakan, contohnya `14/50 States Correct`.
- Jawapan dipadankan dengan negeri tanpa mengira huruf besar atau kecil atau ruang di sekelilingnya.
- Negeri yang betul ditulis pada peta di `x` dan `y` daripada `50_states.csv`; jawapan salah atau berulang ditanya semula.
- `exit` atau Cancel menamatkan permainan; negeri yang tidak dinamakan disimpan dalam `states_to_learn.csv`.

## Modul

| Modul | Tanggungjawab |
| --- | --- |
| `constants.py` | Semua pemalar: tajuk, nama fail, nama lajur, had |
| `states.py` | Peraturan: `State`, `find_state`, `get_missing_states`; tiada fail, tiada skrin |
| `storage.py` | Membaca `50_states.csv` dan menulis `states_to_learn.csv` dengan modul `csv` pustaka standard |
| `game.py` | Gelung meneka `play` dan `run_game` melalui protokol `GameScreen` |
| `turtle_screen.py` | Satu-satunya modul yang mengimport `turtle`: peta, gesaan, nama negeri, koordinat klik |
| `main.py` | Titik masuk yang menyambungkan bahagian-bahagian |

## Ujian, CI dan dokumentasi

- `python -m pytest` menjalankan ujian dengan skrin palsu, jadi tiada tetingkap dibuka.
- `.gitea/workflows/run-tests.yml` menjalankan ruff, mypy, yamllint dan pytest pada setiap push dan pull request.
- `doxygen Doxyfile` membina dokumentasi sumber ke dalam `docs/build/doxygen`.

```bash
python -m pytest
doxygen Doxyfile
```
