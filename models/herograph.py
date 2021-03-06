# Created by jmlm at 18/02/2020-10:14 - test2
import pygame
from models.hero import Hero
from models.position import Position
from setup import SPRITE_HEIGTH, SPRITE_WIDTH, SCREEN_HEIGTH, SCREEN_WIDTH, MC_GYVER_FILE


class HeroGraph(pygame.sprite.Sprite, Hero):
    """
    class hero --> The graphical hero :
    parent classes  --> pygame.sprite.Sprite --> Sprites methods
                    --> Hero (non graphical) --> the same attributes and methods

    instance attributes :
        - hero_img --> the sprite of the hero
        - rect -> the rectangle
        - rect.x - rect.y --> the position
        - old_x - old_y --> the old position
    """

    def __init__(self, map):
        """
        init of the parents + define the image and the scale of the Graphical Hero
        Args: map
        """
        self.map = map
        pygame.sprite.Sprite.__init__(self)
        Hero.__init__(self, self.map)
        hero_image = pygame.image.load(MC_GYVER_FILE).convert()
        self.hero_img = pygame.transform.scale(hero_image, (int(SPRITE_HEIGTH), int(SPRITE_WIDTH)))
        self.rect = self.hero_img.get_rect()
        start_pos = self.map.get_start
        self.rect.x = start_pos.getx
        self.rect.y = start_pos.gety
        self.old_x = 0
        self.old_y = 0

    def move_graph(self, mouv):
        """
        use the parent's "move" method. The specificity of the graphical move is the width and
        the height of the sprites --> the sprite can be outside the screen with an inside position (the position is the
        upper left corner). Nedd also to backup the old position to blit the background sprite on it after the move
        Args: mouv
        Returns:
        """
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        self.move(mouv)

        x = self.position.getx
        y = self.position.gety
        x *= SPRITE_WIDTH
        y *= SPRITE_HEIGTH
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
