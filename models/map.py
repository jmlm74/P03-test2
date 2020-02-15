# Created by jmlm at 15/02/2020-17:36 - test1
from position import Position
from hero import Hero


class Map:
    def __init__(self, filename):
        self.filename = filename

        # peut etre en privé --> _paths...
        # utilisation des sets pour : paths - start - goals (moins) --> donnera toutes
        # les position surlesquelles on pourra poser un objet
        self.paths = set()
        self.walls = set()
        self.start = set()
        self.goal = set()
        # rajouter liste collections speciales (items aiguille...)

        self.load_load_from_file()

    @property
    def get_start(self):
        return list(self.start)[0]

    @property
    def get_goal(self):
        return list(self.goal)[0]

    # ici on peut surcharger __contains__ eu utiliser p in map !
    def is_path_position(self,position):  #verifie si path en valide
        return position in self.paths

    def load_load_from_file(self):
        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, col in enumerate(line):
                    # ici on verifie si murs, passages, arrivee et depart
                    # voir strip pour \n en fin de ligne
                    if col == "d":  # mettre les var dans variables de classe
                        self.start.add(Position(x, y))
                        self.paths.add(Position(x, y))
                    elif col == "0":
                        self.paths.add(Position(x, y))
                    elif col == 'm':
                        self.walls.add(Position(x, y))
                    else:
                        self.goal.add(Position(x, y))
                        self.paths.add(Position(x, y))


def main():
    map = Map("../data/map01.txt")
# TODO Mettre des doctest si possible !
    p = Position(-1, 0)
    print(map.is_path_position(p))
    p = Position(0, 0)
    print(map.is_path_position(p))
    p = Position(0, 0).right()
    print(str(map.is_path_position(p)) + " - {}".format(p))
    p = Position(0, 0).right().right().right()
    print(str(map.is_path_position(p)) + " - {}".format(p))

    toto = Hero()
    print(toto.position)

if __name__ == "__main__":
    main()