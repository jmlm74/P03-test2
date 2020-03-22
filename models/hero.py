# Created by jmlm at 15/02/2020-17:49 - test1
"""
The hero --> strongly inspired by Thierry Chappuis' webinar
"""


class Hero:
    """
    class Hero :
    The hero of the game 
    
    instance attribute : 
        map --> THE map 
        position --> the position during the game
        nb_items --> nb of items caught
        won - dead --> the end of the game --> the goal position has been reached. If you 've caught all the
            items --> won else dead !
     """
    def __init__(self, map):
        """
        The map + hero's start position (not necessary (0, 0))
        Position is at the start position
        get_item is set to true to display the first counter : 0/NB_ITEMS
        """
        self.map = map
        self.position = map.get_start
        self.nb_items = 0
        self.won = False
        self.dead = False
        self.get_item = True

    def move(self, direction):
        """
        Hero's move
        with getattr() --> avoid  if "up", "down"... the parameter (string) is transformed as an object property
        return the new position only if it's a path (walls and outside of the Labyrinthe are treated in one pass)
        calling a Map property :  is_path_position --> return True if OK (path)
        Args: direction:
        Returns:
        """
        new_pos = getattr(self.position, direction)()
        if self.map.is_path_position(new_pos):
            self.position = new_pos
            self.test_pos()

    def test_pos(self):
        """
        the 3 items in the table. Remove one by one when the hero catch one of them. The victory is
        only possible when the list is empty the the goal reached
        Args :
        Returns:
        """
        self.get_item = False
        if self.map.is_item_position(self.position):
            self.nb_items += 1
            self.get_item = True
            self.map.item_remove(self.position)
        if self.position in self.map.goal:
            if len(self.map.items) > 0:
                self.dead = True
            else:
                self.won = True
