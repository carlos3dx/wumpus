# A game of Wumpus
_Original README by CHS is [here](README_CHS.md)_

The game was coded on Python 3.7 cause the position offered is for a Python developer. PyCharm was employed during the development of this game.

In order to execute the game use the following command:
```
python3.7 main.py [-h] [--debug] cols rows pits arrows 

positional arguments:
  cols        Number of columns for the board game
  rows        Number of rows for the board game
  pits        How many pits should be
  arrows      How many arrows have the player

optional arguments:
  -h, --help  show this help message and exit
  --debug     Enambles debug mode
```

The commands to control the character are (does mather if upper or lower case:

* move | move forward | move forwards
* turn left | left turn
* turn right | right turn
* shoot | shoot arrow | throw arrow
* exit | exit board | exit game | go outside

If debug mode is enabled, the board is drawn in ASCII, with a character which symbolise the information contained in that cell  (due to obvious reasons, if a cell contains more tha one thing, only the most relevant is shown).
```
  Legend:
  * P -> Player
  * W -> Wumpus
  * G -> Gold
  * O -> Pit 
  * w -> Wall
  * o -> Wumpus odor
  * b -> Breeze
```
Also is shown where the player is looking and how many arrows has
