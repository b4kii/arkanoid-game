import pygame
from config.constants import BLACK_COLOR, POWERUP_SPRITES, SCREEN_HEIGHT, ANIMATION_COOLDOWN, ANIMATION_STEPS
from utils.spritesheet import Spritesheet

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, pos, upgrade_type, groups, screen):
        super().__init__(groups)
        self.upgrade_type = upgrade_type
        self.screen = screen
        self.sprite_sheet = Spritesheet(POWERUP_SPRITES, 0, 0, 128, 55, color_key=BLACK_COLOR)

        self.animation_list = []
        self.animation_steps = ANIMATION_STEPS
        self.animation_cooldown = ANIMATION_COOLDOWN
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.populate_animation_list()

        self.image = self.animation_list[0]
        self.rect = self.image.get_rect(midtop = pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 3

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= self.animation_cooldown:
            self.frame = (self.frame + 1) % self.animation_steps
            self.last_update = current_time

        self.image = self.animation_list[self.frame]

        self.pos.y += self.speed
        self.rect.y = round(self.pos.y)

        if self.rect.top > SCREEN_HEIGHT + 100:
            self.kill()
    
    def populate_animation_list(self):
        y, width, height = 0, 16, 8

        if self.upgrade_type == "health":
            y = 16
        
        if self.upgrade_type == "size":
            y = 40

        for x in range(self.animation_steps):
            self.animation_list.append(self.sprite_sheet.get_sprite(x * 16, y, width, height, 3))