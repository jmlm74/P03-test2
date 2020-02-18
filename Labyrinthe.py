# Created by jmlm at 15/02/2020-21:36 - test2
from models.hero import Hero
from models.herograph import HeroGraph
from models.map import Map
from controllers.command import parse_arguments
from views.consolemode import clear
from controllers.playtxt import game_text
from controllers.playgraphic import game_graphic
import pygame
from setup import SCREEN_WIDTH, SCREEN_HEIGTH


"""
Labyrinthe - ligne de commande : python Labyrinthe.py [-h] [-t] [-g]
-h --> help
-t mode text
-g mode graphic
--- Repertoires ---
controllers --> interactions avec utilisateur - ligne de commande + "moteur"
data --> maps des labyrinthes
events : N/A
models : Jeu en mémoire --> map - hero - position
views : display 
"""


def main():
    """
    traitement des paramètres de la ligne de commande (mode texte ou graphique) puis chargement en mémoire des items
    communs (map complete avec les méthodes (position du héros et items compris) + héros avec ses méthodes)
    suivant paramètre lancement du jeu en mode texte ou graphique
    """

    args = parse_arguments()
    map = Map("./data/map012.txt")
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
