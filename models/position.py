# Created by jmlm at 15/02/2020-17:36 - test1
"""
the positions in the map  (strongly inspired by Thierry Chappuis' webinar )
"""

class Position:
    """
    class position :
    the labyrinthe's elements position in the map (walls, paths...)
    init --> cath an x,y et and return a position (x, y)
    __repr__ --> return the position in string (to print)
    __eq__ --> comparison between 2 positions --> is it a wall ?
    up,down,right,left --> return the new position depending of the movement event if the new position is a wall
    or is outside --> the verifications must be done by the caller
    getx and gety --> properties which return an x or an y of the instance
    """

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __eq__(self, newpos):
        return self.position == newpos.position

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
    def getx(self):
        x, y = self.position
        return x

    @property
    def gety(self):
        x, y = self.position
        return y
