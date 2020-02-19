# Created by jmlm at 15/02/2020-22:28 - test2
import platform
import os
from models.map import Map
from models.position import Position
from setup import NB_COLS, NB_LINES, MC_GYVER

"""
Display for Text mode only
"""


def clear():
    """
    It does his name : clearscreen (can't test on Mac and Windows) --> StackoverFlow
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")


class MapDisplay:
    """
    class MapDisplay:
    Display the map (loop of the game) in the text mode
    Init --> the instance get the map ta have the labyrinthe's shema and the hero to get his position
    __repr__  --> loop on x,y and at each position we look for the model (wall, path, Item Hero...) and add it
    onto the current line
    display_line : print the current line (with \n)
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
            self.display_line(line)
        return '\n'

    def display_line(self, line):
        print(line)
        return
