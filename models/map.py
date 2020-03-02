# Created by jmlm at 15/02/2020-17:36 - test1
from .position import Position
from setup import WALL_BLOCK, START_BLOCK, PATH_BLOCK, NB_ITEMS
import random

"""
the Labyrinth map (strongly inspired by Thierry Chappuis' webinar ) in memory
"""


class Map:
    """
    THE class Map :
    - define the map and the methods to manipulate it (hero movements, position...)

    instance attributes
        filename --> filename of the map shema
        paths[] --> list of the paths' position - list of positions
        walls[] --> list of the walls' position - list of positions
        start[] --> start position --> list of 1 position
        goal[] --> goal position --> list of 1 position
        items[] --> list of the items' positions --> list of positions
    """
    def __init__(self, filename):
        """
         get the filename of the map the call methods to fill the lists
        Args: filename
        """
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
        """
        Returns: the start position
        """
        return self.start[0]

    @property
    def get_goal(self):
        """
        Returns: the goal position
        """
        return self.goal[0]

    def is_path_position(self, position):
        """
        return True if the position in arg is in the paths list
        Args: position
        Returns: boolean

        """
        return position in self.paths

    def is_item_position(self, position):
        """
        Return True if the item in arg (position) is in the items list
        Args: position
        Returns: Boolean
        """
        return position in self.items

    def item_remove(self, position):
        """
        delete the item in the list (position in arg)
        Args: position
        Returns:
        """
        self.items.remove(position)

    def load_load_from_file(self):
        """
        load the map in lists - walls, paths , start and goal position (list with 1 Item) -
        don't forget to remove the \n at the end of the file's lines
        Args:
        Returns:
        """
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
        """
        randomize 3 positions in the paths list without the start and the goal positions. Put them in a list
        Args:
        Returns:
        """
        my_dummy_list = []
        my_dummy_list = self.paths[:]
        my_dummy_list.remove(self.start[0])
        my_dummy_list.remove(self.goal[0])
        self.items = random.sample(my_dummy_list, NB_ITEMS)

