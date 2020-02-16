# Created by jmlm at 15/02/2020-22:28 - test2
import platform
import os
from models.map import Map
from models.position import Position
from setup import NB_COLS, NB_LINES, MC_GYVER


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


class MapDisplay:
    def __init__(self, map, hero):
        self.map = map
        self.hero = hero

    def __repr__(self):
        clear()
        for x in range(NB_LINES+1):
            line = ''
            for y in range(NB_COLS+1):
                mypos = Position(x, y)
                # test si chemin --> oui peut aussi etre le debut ou la sortie
                if self.map.is_path_position(mypos):
                    if self.hero.position == mypos:
                        line += MC_GYVER
                    elif self.map.get_goal == mypos:
                        line += 'G'
                    elif self.map.get_start == mypos:
                        line += 'S'
                    else:
                        line += ' '
                else:
                    line += 'W'

            print(line)
        return '\n'
