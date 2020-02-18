# Created by jmlm at 17/02/2020-20:15 - test2
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT,
    KEYDOWN
)
from views.graphicmode import MapDisplayGraphic
"""
module pour l'interface utilisateur en mode graphic
"""


def game_graphic(map, toto, screen):
    running = True
    clock = pygame.time.Clock()
    map_display_graphic = MapDisplayGraphic(map, toto, screen)
    map_display_graphic.update()

    while running:
        if toto.victoire:
            print("GAGNE !!!!!")
            map_display_graphic.message_display('GAGNE!!!!!!')
            running = False
        elif toto.mort:
            print("PERDU - Vous etes mort !!!")
            map_display_graphic.message_display("PERDU - Vous etes mort !!!")
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_DOWN:
                    toto.move_graph("down")
                elif event.key == K_UP:
                    toto.move_graph("up")
                elif event.key == K_RIGHT:
                    toto.move_graph("right")
                elif event.key == K_LEFT:
                    toto.move_graph("left")

        map_display_graphic.update2()
        clock.tick(30)
    pygame.quit()
