# Created by jmlm at 15/02/2020-17:50 - test1
from views.consolemode import MapDisplay
from setup import CHOICES, NB_ITEMS
import os
"""
module pour l'interface utilisateur en mode texte
"""


def game_text(map: object, toto: object) -> object:
    """
    On boucle indéfiniment sur le jeu tant que c'est pas gagné ou perdu ou abandonné avec ou sans sauvegarde
    boucle infinie :
        - on affiche la map de base en instanciant la classe MapDisplay (avec en parametre la map de base et le hero)
        - on attend le choix de l'utilisateur --> possibilité de sortie
    fin boucle
    """
    # TODO : Sauvegarde et déplacements en diagonale
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
