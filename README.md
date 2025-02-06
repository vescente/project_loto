# Loto
The program is a simple implementation of the Loto game with special rules, interacting with the user via a command-line interface.

## Technologies Used
Python 3, pytest

## Game Rules
The game is played using special cards marked with numbers and chips (kegs) with numbers.

There are 90 kegs (with numbers from 1 to 90).

Each card contains 3 rows of 9 cells. Each row has 5 random numbers arranged in ascending order. All numbers on the card are unique.

#### Example of a card:

    --------------------------
        9 43 62          74 90
     2    27    75 78    82
       41 56 63     76      86
    --------------------------

There are 2 players in the game: the user and the computer. Each player is given a random card at the beginning.

Each turn, a random keg is drawn and displayed on the screen. The player's card and the computer's card are also displayed.

The user is prompted to cross out the number on the card or continue.

If the player chooses to "cross out":
 - if the number is on the card, it is crossed out and the game continues.
 - if the number is not on the card, the player loses and the game ends.

If the player chooses to "continue":

 - if the number is on the card, the player loses and the game ends.
 - if the number is not on the card, the game continues. The winner is the first to cross out all the numbers on their card.

#### Example of a turn:
    New keg: 70 (76 left)
    ------ Your card -----
     6  7          49    57 58
       14 26     -    78    85
    23 33    38    48    71
    --------------------------
    -- Computer's card ---
     7 87     - 14    11
          16 49    55 88    77
       15 20     -       76  -
    --------------------------
    Cross out the number? (y/n)
