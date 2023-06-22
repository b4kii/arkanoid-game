import pygame, time
from config.constants import *
from utils.spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        self.image = self.get_image()
        self.rect = self.image.get_rect(midbottom = (SW_MID, SCREEN_HEIGHT - 20))
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
    
    def get_image(self):
        return Spritesheet(VAUS_SPRITES, 64, 16, 48, 7, scale=3, color_key=GREEN_COLOR).sprite_image

    def handle_events(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a] or key_pressed[pygame.K_LEFT]:
            self.direction.x = -1
        elif key_pressed[pygame.K_d] or key_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def check_window_collision(self):
        # if self.rect.left < 35:
            # self.rect.left = 35
        if self.rect.left < BORDER_OFFSET:
            self.rect.left = BORDER_OFFSET
            self.pos.x = self.rect.x
        
        # if self.rect.right + 35 > SCREEN_WIDTH:
            # self.rect.right = SCREEN_WIDTH - 35
        if self.rect.right + BORDER_OFFSET > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH - BORDER_OFFSET
            self.pos.x = self.rect.x

    def update(self):
        self.old_rect = self.rect.copy()
        self.handle_events()

        self.pos.x += self.direction.x * self.speed
        self.rect.x = round(self.pos.x)

        self.check_window_collision()

    def upgrade(self, upgrade_type):
        if upgrade_type == "health":
            self.health += 1

        if upgrade_type == "speed":
            self.speed += 1
        
        if upgrade_type == "size":
            width = self.rect.width * 1.1
            self.image = pygame.transform.scale(self.image, (width, self.rect.height))
            self.rect = self.image.get_rect(center = self.rect.center)
            self.pos.x = self.rect.x
    
    def enemy_hit(self, upgrade_type):
        if upgrade_type == "health":
            self.health -= 1

        if upgrade_type == "speed":
            self.speed -= 1
        
        if upgrade_type == "size":
            width = self.rect.width * 0.9
            self.image = pygame.transform.scale(self.image, (width, self.rect.height))
            self.rect = self.image.get_rect(center = self.rect.center)
            self.pos.x = self.rect.x
    
    def restore_mid_pos(self):
        self.rect.center = SW_MID, SCREEN_HEIGHT - 20
        self.pos.x = self.rect.x
    
    def remove_upgrades(self):
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.image = self.get_image()
        self.rect = self.image.get_rect(center = self.rect.center)
        self.pos.x = self.rect.x