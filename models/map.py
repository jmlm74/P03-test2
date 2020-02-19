# Created by jmlm at 15/02/2020-17:36 - test1
from .position import Position
from setup import WALL_BLOCK, START_BLOCK, PATH_BLOCK, NB_ITEMS
import random

"""
the Labyrinthe map (strongly inspired by Thierry Chappuis' webinar ) in memory
"""


class Map:
    """
    La classe Map :
    - define the map and the methods to manipulate it (hero movements, position...)
    init --> get the filename of the map the call methods to fill the lists
    properties (getx, gety... ) Return the x, the Y ... of the current position
    load from file : load the map in lists - walls, paths , start and goal position (list with 1 Item) -
        don't forget to remove the \n at the end of the file's lines
    put_items --> randomize 3 positions in the paths list but the start and the goal positions. Put them in a lis
    """
    def __init__(self, filename):
        self.filename = filename

        self.paths = []
        self.walls = []
        self.start = []
        self.goal = []
        self.items = []

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
        self.items = random.sample(my_dummy_list, NB_ITEMS)

