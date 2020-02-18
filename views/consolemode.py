# Created by jmlm at 15/02/2020-22:28 - test2
import platform
import os
from models.map import Map
from models.position import Position
from setup import NB_COLS, NB_LINES, MC_GYVER

"""
module pour le display en mode texte seulement
"""


def clear():
    """
    comme son nom l indique clearscreen
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")


class MapDisplay:
    """
    Effectue le display de la map en tenant compte du Hero (noté M), du depart (noté S),due la sortie (notée G)
    et des ITEMS (notés I).
    Init --> l'instance récupère la map pour avoir le schema du labyrinthe, le héros pour avoir sa position et
    les position des items
    __repr__ (surcharge de repr) --> on boucle sur x,y et a chaque point du labyrinthe, on regarde de quel type de
    position il s'agit --> mur ou chemin puis le reste et on affiche le point
    """
    def __init__(self, map, hero):
        self.map = map
        self.hero = hero

    def __repr__(self):
        clear()
        for x in range(NB_LINES+1):
            line = ''
            for y in range(NB_COLS+1):
                mypos = Position(x, y)
                # test si chemin --> si ok peut aussi etre le debut ou la sortie ou un Item
                if self.map.is_path_position(mypos):
                    if self.hero.position == mypos:
                        line += MC_GYVER
                    elif self.map.get_goal == mypos:
                        line += 'G'
                    elif self.map.get_start == mypos:
                        line += 'S'
                    elif mypos in self.map.items:
                        line += 'I'
                    else:
                        line += ' '
                else:
                    line += 'W'
            self.affiche(line)
        return '\n'

    def affiche(self, line):
        print(line)
        return
