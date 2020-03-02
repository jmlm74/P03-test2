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
from setup import colors, font_dejavu, font_bebas, font_freesansbold, WIN_MUSIC, LOOSE_MUSIC
"""
GUI play module
"""


def game_graphic(map, toto, screen):
    """
    pygame is initiliazed by the caller.
    some goodies : Messages and music (just for fun !)
    The MapDisplayGraphis is the 'builder' of the graphical map. It 's displayed only once (twice to remove
    the message) --> The screen is ready now we can loop for the game
    loop : while variable running is true
        test the victory or the defeat --> message an music then leave
        test a pygame event
            like Quit (X corner) or escape key --> leave
            like direction keys --> the key doesn't match the movement ! It's because the X an Y of the
            Pygame screen are not the same as the text Version --> to use only one class and method, I don't
            find anything else to do (just turn your mind of 90° counter-clockwise :) )
            the update only update the old and the new stripes (2 stripes only vs 15*15=225 stripes for the
            full screen)
            the pygame clock tic has benn set as 30 by seconds (FPS I think) not to handle too much ressources
    end loop
    """
    running = True
    clock = pygame.time.Clock()
    map_display_graphic = MapDisplayGraphic(map, toto, screen)
    map_display_graphic.update()
    couleur = colors['blue']
    map_display_graphic.message_display("LET'S GO", font=font_dejavu, size=55, wait=3, color=couleur)
    map_display_graphic = MapDisplayGraphic(map, toto, screen)
    map_display_graphic.update()

    while running:
        if toto.won:
            print("GAGNE !!!!!")
            color = colors['white']
            map_display_graphic.message_display('GAGNE!!!!!!', font=font_bebas, wait=1, size=100, color=color)
            running = False
            map_display_graphic.music_play(WIN_MUSIC)
        elif toto.dead:
            print("PERDU - Vous etes dead !!!")
            color = colors['black']
            map_display_graphic.message_display("PERDU - Vous etes dead !!!", size=45, wait=1,  color=color)
            running = False
            map_display_graphic.music_play(LOOSE_MUSIC)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_DOWN:
                    toto.move_graph("right")
                elif event.key == K_UP:
                    toto.move_graph("left")
                elif event.key == K_RIGHT:
                    toto.move_graph("down")
                elif event.key == K_LEFT:
                    toto.move_graph("up")
        map_display_graphic.update2()
        clock.tick(30)
    pygame.quit()
