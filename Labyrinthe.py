# Created by jmlm at 15/02/2020-21:36 - test2
from models.hero import Hero
from models.herograph import HeroGraph
from models.map import Map
from controllers.command import parse_arguments
from views.consolemode import clear
from controllers.playtxt import game_text
from controllers.playgraphic import game_graphic
import pygame
from setup import SCREEN_WIDTH, SCREEN_HEIGTH,MAP_FILE


"""
Labyrinthe - command line : python Labyrinthe.py [-h] [-t] [-g]
-h --> help
-t --> text mode
-g --> graphic mode
--- Directories ---
controllers --> user interface modules (the loops game)
ressource --> external resources (map shema, sounds, images...)
models : game objects --> map - hero (text and graph) - position
views : display objects
"""


def main():
    """
    parse parameters.
    The init is done here :
    - The map object remain the same in text or graphic mode --> instantiated at the begining and once
    - the hero and the output (text or graphic) mode are also instantiated here
        (toto is for the film 'toto le heros')
    """

    args = parse_arguments()
    map = Map(MAP_FILE)
    if args.text:
        clear()
        toto = Hero(map)
        game_text(map, toto)
    else:
        clear()
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        toto = HeroGraph(map)
        game_graphic(map, toto, screen)


if __name__ == "__main__":
    main()
