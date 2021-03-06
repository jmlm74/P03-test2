# Created by jmlm at 17/02/2020-20:15 - test2
import pygame
import time, sys
from .consolemode import MapDisplay
from models.position import Position
from setup import NB_COLS, NB_LINES, SPRITE_WIDTH, SPRITE_HEIGTH, SCREEN_WIDTH, SCREEN_HEIGTH, colors, NB_ITEMS, \
    ITEM1_FILE, ITEM2_FILE, ITEM3_FILE, BG_FILE, WALL_FILE, GUARD_FILE, font_bebas, font_dejavu, font_freesansbold, \
    msg_couleur

"""
GUI class module
"""


class MapDisplayGraphic:
    """
    class MapDisplayGraphic
    - the builder of the graphical labyrinthe

    - instance attributes :
        parameters
            map --> THE map
            hero --> THE hero
            screen --> pygame screen to blit the sprites
        *_img --> the sprites (wall, paths, items...)
    """
    def __init__(self, map, hero, screen):
        """
        get the map (lists of walls...)
        get the hero (the sprite, the position...)
        get the screen to display everything
        load and transform all the images in sprites (size...)
        Args: map, hero, screen
        Returns:
        """
        self.map = map
        self.hero = hero
        self.screen = screen
        path_image = pygame.image.load(BG_FILE).convert()
        self.path_img = pygame.transform.scale(path_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        wall_image = pygame.image.load(WALL_FILE).convert()
        self.wall_img = pygame.transform.scale(wall_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        goal_image = pygame.image.load(GUARD_FILE).convert()
        self.goal_img = pygame.transform.scale(goal_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.items = []
        item1_image = pygame.image.load(ITEM1_FILE).convert()
        self.item1_img = pygame.transform.scale(item1_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.items.append(self.item1_img)
        item2_image = pygame.image.load(ITEM2_FILE).convert()
        self.item2_img = pygame.transform.scale(item2_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.items.append(self.item2_img)
        item3_image = pygame.image.load(ITEM3_FILE).convert()
        self.item3_img = pygame.transform.scale(item3_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.items.append(self.item3_img)
        pygame.display.set_caption('P03 - Labyrinthe')

    def update(self):
        """
        The same loop as the console display : loop on the x and y and display the right stripe on each position.
        Args:
        Returns:
        """
        self.screen.blit(self.hero.hero_img, self.hero.rect)
        item = 0
        for x in range(NB_LINES+1):
            for y in range(NB_COLS+1):
                myposx = x * SPRITE_WIDTH
                myposy = y * SPRITE_HEIGTH
                mypos = Position(x, y)
                if self.map.is_path_position(mypos):
                    if self.hero.position == mypos:
                        self.screen.blit(self.hero.hero_img, self.hero.rect)
                    elif self.map.get_goal == mypos:
                        self.screen.blit(self.goal_img, (myposx, myposy))
                    elif self.map.get_start == mypos:
                        self.screen.blit(self.start_img, (myposx, myposy))
                    elif mypos in self.map.items:
                        self.screen.blit(self.items[item], (myposx, myposy))
                        item += 1
                    else:
                        self.screen.blit(self.path_img, (myposx, myposy))
                else:
                    self.screen.blit(self.wall_img, (myposx, myposy))
        pygame.display.update()

    def update2(self):
        """
        update the old position of the hero --> put the path image
        update the new position --> put the hero
        Args:
        Returns:
        """
        self.screen.blit(self.path_img, (self.hero.old_x, self.hero.old_y))
        self.screen.blit(self.hero.hero_img, self.hero.rect)
        if self.hero.get_item:
            couleur = colors[msg_couleur[self.hero.nb_items]]
            self.item_counter_display(font="font_dejavu", color=couleur)
        pygame.display.update()

    def item_counter_display(self, **font_desc):
        """
        args : **font_desc --> dictionary contents the desc of the message (font, size,color...)!
        1st update the 3 sprites to erase the old counter
        the update the counter changing color occording to number of caught items
        """
        font = "font_dejavu"
        size = 35
        couleur = colors["black"]
        for key, value in font_desc.items():
            if key == 'font':
                font = value
            elif key == 'size':
                size = int(value)
            elif key == 'wait':
                wait = int(value)
            elif key == 'color':
                couleur = value

        self.screen.blit(self.wall_img, (585, 585))
        self.screen.blit(self.wall_img, (540, 585))
        self.screen.blit(self.wall_img, (495, 585))
        pygame.display.update()
        police = pygame.font.SysFont(font, size)

        message = "NB ITEMS"
        text_surf, text_rect = self.text_objects(message, police, couleur)
        text_rect.x = 495
        text_rect.y = 585
        self.screen.blit(text_surf, text_rect)
        message = str(self.hero.nb_items) + "/" + str(NB_ITEMS)
        text_surf, text_rect = self.text_objects(message, police, couleur)
        text_rect.x = 530
        text_rect.y = 605
        self.screen.blit(text_surf, text_rect)
        self.hero.get_item = False

    def message_display(self, message, **font_size):
        """
        display a message (choose your font, color,font_size and how long to see it )
        Args: message, **font_size:
        Returns:
        """
        font = font_freesansbold
        size = 100
        wait = 3
        couleur = colors["red"]
        for key, value in font_size.items():
            if key == 'font':
                font = value
            elif key == 'size':
                size = int(value)
            elif key == 'wait':
                wait = int(value)
            elif key == 'color':
                couleur = value
        police = pygame.font.Font(font, size)
        text_surf, text_rect = self.text_objects(message, police, couleur)
        text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGTH/2)
        self.screen.blit(text_surf, text_rect)
        pygame.display.update()
        time.sleep(wait)

    def text_objects(self, text, font, color='(255, 0, 0)'):
        """
        Args: text font color(default red)
        Returns: surface and a rectangle with the text inside
        """
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def music_play(self, music):
        """
        play a little music at the end
        open/init mixer via pygame - load file then play and loop to wait until the end !
        if no mixer found --> handle exception
        """
        try:
            pygame.mixer.init(44100, -16, 2, 2048)
            clock = pygame.time.Clock()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                clock.tick(10000)
        except pygame.error:
            print("Erreur : ouverture sound-device %s" % sys.exc_info()[0])
