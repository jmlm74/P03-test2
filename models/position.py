# Created by jmlm at 15/02/2020-17:36 - test1


class Position:
    """
    mettre doc
    """

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    # pouvoir hasher les postion pour les entrer dans un set
    def __hash__(self):
        return hash(self.position)

    # on surcharge l'egalité pour comparer 2 positions (dert a verifier su mur ou autre)
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

    def getxy(self):
        x, y = self.position
        position_tuple =  x, y
        return position_tuple
