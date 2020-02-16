# Created by jmlm at 15/02/2020-17:50 - test1
from views.console.consolemode import clear, MapDisplay
from setup import CHOICES


def game_text(map: object, toto: object) -> object:
    input_choice = ''
    while True:
        map_display = MapDisplay(map, toto)
        print(map_display)
        print('\n')
        print("select your input : ")
        for key, value in CHOICES.items():
            print("{} --> {}".format(key, value))
        input_choice = input("Enter your choice then 'Enter' : ")
        if input_choice.upper() == "Q":
            print("Quit")
            break
        elif input_choice.upper() == "S":
            print("save")
            break
        elif input_choice.upper() in ("L", "R", "U", "D"):
            move = CHOICES.get(input_choice.upper())
            toto.move(move)
