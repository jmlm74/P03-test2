# Created by jmlm at 15/02/2020-17:49 - test1
"""
Le hero --> tres fortement inspiré par le webinaire de Thierry Chappuis
"""


class Hero:
    """
    init --> la map dans lequel se trouve le heros + sa position de départ (pas obligatoirement (0, 0))
         --> initialise la variable
    move --> deplacement du héros
         --> le getattr() permet d'eviter les if "up", "down"...
         --> ne donne la nouvelle position que si c'est un chemin (traite d'un coup les murs et hors du labyrinthe)
         en appelant la méthode de Map is_path_position qui renvoie True si OK
         --> traite les items et la victoire
    """
    # TODO : Les items
    def __init__(self, map):
        self.map = map
        self.position = map.get_start
        self.nb_items = 0
        self.victoire = False
        self.mort = False

    def move(self, direction):
        # si direction up down ... utilise getattr
        # getattr() can access an object property using a string --> transforme string en propriété
        new_pos = getattr(self.position, direction)()
        if self.map.is_path_position(new_pos):
            self.position = new_pos
            if self.position in self.map.items:
                self.nb_items += 1
                self.map.items.remove(self.position)
            if self.position in self.map.goal:
                if len(self.map.items) > 0:
                    self.mort = True
                else:
                    self.victoire = True
