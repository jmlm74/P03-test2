# Created by jmlm at 15/02/2020-21:36 - test2
from models.position import Position
from models.hero import Hero
from models.map import Map
from controlers.command import parse_arguments
from views.console.consolemode import clear, MapDisplay
from models.game import game_text

"""
Main
"""


def main():
    clear()
    args = parse_arguments()
    map = Map("./data/map01.txt")
    toto = Hero(map)
    if args.text:
        game_text(map, toto)
    else:
        pass




if __name__ == "__main__":
    main()
