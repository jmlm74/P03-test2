# Created by jmlm at 15/02/2020-17:49 - test1


class Hero:
    def __init__(self, map):
        self.map = map
        self.position = map.get_start

    def move(self, direction):
        # si direction up down ... utilise getattr
        # getattr() can access an object property using a string --> transforme string en propriété
        new_pos = getattr(self.position, direction)()
        if self.map.is_path_position(new_pos):
            self.position = new_pos
