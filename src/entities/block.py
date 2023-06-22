import pygame
from random import randint
from utils.spritesheet import Spritesheet
from config.constants import *

class Block(pygame.sprite.Sprite):
    def __init__(self, sprite_group, block_type, pos, width, height, create_upgrade, player_score):
        super().__init__(sprite_group)
        self.block_type = int(block_type)
        self.block_health = int(block_type)
        self.image = self.get_image(width, height)
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()
        self.create_upgrade = create_upgrade
        self.player_score = player_score

    def get_image(self, width, height):
        image = None
        cut_width, cut_height = 16, 8

        for count, block in enumerate(BLOCKS_HEALTH):
            if block == self.block_health:
                image = Spritesheet(BACKGROUND_SPRITES, count * cut_width, 0, cut_width, cut_height, scale_dimensions=(width, height), color_key=(255,255,255)).sprite_image
                break
        return image

    def update_image(self):
        self.image = self.get_image(self.rect.width, self.rect.height)

    def get_damage(self, amount):
        self.block_health -= amount

        if self.block_health > 0:
            pass
        else:
            if randint(0, 20) < 3:
                self.create_upgrade(self.rect.center)
            self.player_score[0] += 10 * self.block_type
            self.kill()
