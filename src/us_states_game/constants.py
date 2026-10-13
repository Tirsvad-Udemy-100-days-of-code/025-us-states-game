"""Constants of the U.S. States Game: titles, file names and limits.

@file constants.py
@brief Titles, file names and limits used by the game.

Every value the game needs in more than one place lives here, so the
game logic and the Turtle screen never repeat a literal.
"""

from pathlib import Path

## Folder of this package.
PACKAGE_DIR = Path(__file__).resolve().parent

## Folder with the course files the game reads at run time.
DATA_DIR = PACKAGE_DIR / "data"

## CSV file with the columns state, x and y for all 50 states.
STATES_CSV_PATH = DATA_DIR / "50_states.csv"

## GIF of the blank U.S. map, registered as a Turtle shape.
MAP_IMAGE_PATH = DATA_DIR / "blank_states_img.gif"

## File written when the game ends, listing the states the player missed.
STATES_TO_LEARN_FILENAME = "states_to_learn.csv"

## Column names in the states CSV file.
STATE_COLUMN = "state"
X_COLUMN = "x"
Y_COLUMN = "y"

## Title of the game window.
SCREEN_TITLE = "U.S. States Game"

## Number of states the player has to name.
NUMBER_OF_STATES = 50

## Text the player types to leave the game early.
EXIT_COMMAND = "exit"

## Title shown while playing; filled with the guessed count and the total.
TITLE_FORMAT = "{guessed}/{total} States Correct"

## Prompt of the answer dialog.
ANSWER_PROMPT = "What's another state's name?"

## Name under which the map image is registered as a Turtle shape.
MAP_SHAPE_NAME = str(MAP_IMAGE_PATH)

## Size in pixels of the map image, and so of the game window.
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491

## Font of the state names written on the map: family, size and style.
STATE_FONT = ("Courier", 8, "normal")

## Alignment of a state name written at its coordinates.
STATE_ALIGNMENT = "center"

## Name of the logger that reports mouse click coordinates.
LOGGER_NAME = "us_states_game"
