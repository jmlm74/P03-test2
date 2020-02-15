# Created by jmlm at 15/02/2020-17:36 - test1
from .position import Position
from setup import WALL_BLOCK, START_BLOCK, PATH_BLOCK


class Map:
    def __init__(self, filename):
        self.filename = filename

        # peut etre en privé --> _paths...
        # utilisation des sets pour : paths - start - goals (moins) --> donnera toutes
        # les position surlesquelles on pourra poser un objet
        # TODO rajouter liste collections speciales (items aiguille...)
        self.paths = []
        self.walls = []
        self.start = []
        self.goal = []

        self.load_load_from_file()

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


