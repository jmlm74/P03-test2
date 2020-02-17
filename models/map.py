# Created by jmlm at 15/02/2020-17:36 - test1
from .position import Position
from setup import WALL_BLOCK, START_BLOCK, PATH_BLOCK, NB_ITEMS
import random

"""
La map du labyrinthe (fortement inspirée par webinaire de Thierry Chappuis) en mémoire
"""


class Map:
    """
    La classe Map --> va définir le dessin de la map et les méthodes pour la manipuler (déplacements du héros)
    init --> on récupère le nom du fichier puis on mets toutes les positions dans les listes qui vont bien avec
         la fonction load_from_file.
         Les listes start et goals sont des listes avec 1 item
    def_start et def_goal --> propriétés car renvoient une valeur sans prendre de parametres
    put_items --> prend aléatoirement 3 positions de chemin sans depart et arrivée et place les items
    """
    def __init__(self, filename):
        self.filename = filename

        # peut etre en privé --> _paths...
        # TODO rajouter liste collections speciales (items aiguille...)
        self.paths = []  # les chemins
        self.walls = []  # les murs
        self.start = []  # le heros
        self.goal = []   # la sortie
        self.items = []  # les objets

        self.load_load_from_file()
        self.put_items()


    @property
    def get_start(self):
        # return list(self.start)[0]
        return self.start[0]

    @property
    def get_goal(self):
        # return list(self.goal)[0]
        return self.goal[0]

    def is_path_position(self, position):
        return position in self.paths

    def load_load_from_file(self):
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    # ici on verifie si murs, passages, arrivee et depart
                    # voir strip pour \n en fin de ligne
                    if col == '\n':
                        continue
                    elif col == START_BLOCK:
                        self.start.append(Position(x, y))
                        self.paths.append(Position(x, y))
                    elif col == PATH_BLOCK:
                        self.paths.append(Position(x, y))
                    elif col == WALL_BLOCK:
                        self.walls.append(Position(x, y))
                    else:
                        self.goal.append(Position(x, y))
                        self.paths.append(Position(x, y))

    def put_items(self):
        my_dummy_list = []
        my_dummy_list = self.paths[:]
        my_dummy_list.remove(self.start[0])
        my_dummy_list.remove(self.goal[0])
        self.items = random.sample( my_dummy_list, NB_ITEMS)

