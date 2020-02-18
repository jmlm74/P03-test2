# Created by jmlm at 15/02/2020-17:36 - test1


class Position:
    """
    sert a determiner la position des items dans le labyrinthe (murs, passages, héros, items...)
    init --> prend un x,y et renvoi une position (x, y)
    __repr__ --> renvoi la position en str
    __eq__ --> permet de comparer 2 positions
    up,down,right,left --> renvoient la nouvelle position suivant mouvement demandé (quoi que ce soit - mur ou autre)
    cette classe ne s'occupe que des positions et non pas des possibilités de déplacement
    getxy --> renvoi une position d'un x et d'un y sans réinstancier la classe (ressemble à inverse de repr)
    """

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    # pouvoir hasher les postion pour les entrer dans un set (non utilisé ici)
    def __hash__(self):
        return hash(self.position)

    # on surcharge l'egalité pour comparer 2 positions (sert a verifier si mur ou autre)
    def __eq__(self, newpos):
        return self.position == newpos.position

# on ne regrade pas les validités des positions
# TODO - diagonales si OK !
    def up(self):
        x, y = self.position
        return Position(x-1, y)

    def down(self):
        x, y = self.position
        return Position(x+1, y)

    def right(self):
        x, y = self.position
        return Position(x, y+1)

    def left(self):
        x, y = self.position
        return Position(x, y-1)

    @property
    def getxy(self):
        x, y = self.position
        position_tuple = x, y
        return position_tuple

    @property
    def getx(self):
        x, y = self.position
        return x

    @property
    def gety(self):
        x, y = self.position
        return y
