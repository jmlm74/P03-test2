# Created by jmlm at 18/02/2020-10:14 - test2
import pygame
from models.hero import Hero
from models.position import Position
from setup import SPRITE_HEIGTH, SPRITE_WIDTH, SCREEN_HEIGTH, SCREEN_WIDTH


class HeroGraph(pygame.sprite.Sprite, Hero):
    def __init__(self, map):
        self.map = map
        self.text_mode = False
        pygame.sprite.Sprite.__init__(self)
        Hero.__init__(self, self.map)
        self.hero_image = pygame.image.load("ressource/MacGyver.png").convert()
        self.hero_img = pygame.transform.scale(self.hero_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.image = pygame.transform.scale(self.hero_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.rect = self.hero_img.get_rect()
        start_pos = self.map.get_start
        self.rect.x = start_pos.getx
        self.rect.y = start_pos.gety
        self.old_x = 0
        self.old_y = 0

    def move_graph(self, mouv):

        y = self.rect.y
        x = self.rect.x
        self.old_x = x
        self.old_y = y

        if mouv == "up":
            y -= SPRITE_HEIGTH
        elif mouv == "down":
            y += SPRITE_HEIGTH
        elif mouv == "right":
            x += SPRITE_WIDTH
        elif mouv == "left":
            x -= SPRITE_WIDTH

        mypos = Position(x/SPRITE_WIDTH, y/SPRITE_HEIGTH)
        self.position = mypos
        if self.map.is_path_position(mypos):
            self.test_pos()
            self.rect.y = y
            self.rect.x = x
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > SCREEN_HEIGTH - SPRITE_HEIGTH:
                self.rect.y = SCREEN_HEIGTH - SPRITE_HEIGTH
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > SCREEN_WIDTH - SPRITE_WIDTH:
                self.rect.x = SCREEN_WIDTH - SPRITE_WIDTH
        else:
            mypos = Position(self.old_x / SPRITE_WIDTH, self.old_y / SPRITE_HEIGTH)
            self.position = mypos