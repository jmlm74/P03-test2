# Created by jmlm at 15/02/2020-17:50 - test1
from views.consolemode import MapDisplay
from setup import CHOICES, NB_ITEMS
import os
"""
TUI or CUI (Text - Console User Interface !) - CLI play module ?
"""


def game_text(map: object, toto: object) -> object:
    """
    loop forever : The player can choose a move and Q to quit
    the loop is broken only if the player wins or loose ond chose to quit (Q choice)
    loop :
        - the map is displayed by instanciating the MapDisplay Class (params : map and Hero with his position)
        - waiting for the player choice --> can quit
    end loop
    """

    input_choice = ''
    while True:
        map_display = MapDisplay(map, toto)
        print(map_display)
        print('\n')
        if toto.victoire:
            print("GAGNE !!!!!")
            break
        elif toto.mort:
            print("PERDU - Vous etes mort !!!")
            break
        print("nb items to catch : {} - nb items caught : {}".format(NB_ITEMS, toto.nb_items))
        print("select your input : ")
        for key, value in CHOICES.items():
            print("{} --> {}".format(key, value))
        input_choice = input("Enter your choice then 'Enter' : ")
        if input_choice.upper() == "Q":
            print("Quit")
            break
        elif input_choice.upper() == "S":
            print("save")
            break
        elif input_choice.upper() in ("L", "R", "U", "D"):
            move = CHOICES.get(input_choice.upper())
            toto.move(move)
        else:
            os.system("beep")
