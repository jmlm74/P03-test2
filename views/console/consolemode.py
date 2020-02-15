# Created by jmlm at 15/02/2020-22:28 - test2
import platform
import os


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


class Carte:
    def __init__(self, filename):
        file = open(filename, "r")
        self.labyprt = file.read()
        file.close()

    def __repr__(self):
        return "{}".format(self.labyprt)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        ligne_liste = chaine.split("\n")
        return ligne_liste