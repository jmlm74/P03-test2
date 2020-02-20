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
    
    init --> the map + hero's start position (not necessary (0, 0))
         --> position is at the start position 
    move --> Hero's move
         --> with getattr() --> avoid  if "up", "down"... the parameter (string) is transformed as an objet property
         --> return the new position only if it's a path (walls and outside of the Labyrinthe are treated in one pass)
         calling a Map property :  is_path_position --> return True if OK (path)
    test_pos --> the 3 items in the table. Remove one by one when the hero catch one of them. The victory is
    only possible when the list is empty the the goal reached
    """
    def __init__(self, map):
        self.map = map
        self.position = map.get_start
        self.nb_items = 0
        self.won = False
        self.dead = False

    def move(self, direction):
        new_pos = getattr(self.position, direction)()
        if self.map.is_path_position(new_pos):
            self.position = new_pos
            self.test_pos()

    def test_pos(self):
        if self.map.is_item_position(self.position):
            self.nb_items += 1
            self.map.item_remove(self.position)
        if self.position in self.map.goal:
            if len(self.map.items) > 0:
                self.dead = True
            else:
                self.won = True
