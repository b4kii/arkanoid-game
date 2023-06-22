import pygame
from random import choice
from config.constants import *
from utils.spritesheet import Spritesheet

class Ball(pygame.sprite.Sprite):
    def __init__(self, sprite_group, player, blocks_group, upgrades_group, enemies_group):
        super().__init__(sprite_group)
        self.image = Spritesheet(VAUS_SPRITES,0, 40, 5, 4, scale=4, color_key=GREEN_COLOR).sprite_image
        self.rect = self.image.get_rect(midbottom=player.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2((choice((-1, 1)), -1))
        self.active = False
        self.player = player
        self.blocks_group = blocks_group
        self.upgrades_group = upgrades_group
        self.enemies_group = enemies_group

        self.bounce_sound = pygame.mixer.Sound(BOUNCE_SOUND)
        self.bounce_sound.set_volume(EFFECTS_SOUND_VOLUME)
        
        self.health_lose_sound = pygame.mixer.Sound(HEALTH_LOSE_SOUND)
        self.health_lose_sound.set_volume(EFFECTS_SOUND_VOLUME)
    
    def check_window_collision(self, direction):
        border_offset = SCREEN_WIDTH * 0.036 + 5
        if direction == "x":
            # if self.rect.left < 40:
            if self.rect.left < BORDER_OFFSET:
                # self.rect.left = 40
                self.rect.left = BORDER_OFFSET
                self.pos.x = self.rect.x 
                self.direction.x *= -1
                self.bounce_sound.play()
                
            if self.rect.right > SCREEN_WIDTH - BORDER_OFFSET:
            # if self.rect.right > SCREEN_WIDTH - 40:
                self.rect.right = SCREEN_WIDTH - BORDER_OFFSET
                # self.rect.right = SCREEN_WIDTH - 40
                self.pos.x = self.rect.x
                self.direction.x *= -1
                self.bounce_sound.play()

        if direction == "y":
            # if self.rect.top < 35:
                # self.rect.top = 35
            if self.rect.top < BORDER_OFFSET:
                self.rect.top = BORDER_OFFSET
                self.pos.y = self.rect.y
                self.direction.y *= -1
                self.bounce_sound.play()

            if self.rect.bottom > SCREEN_HEIGHT:
                self.active = False
                self.direction.y = -1
                self.player.health -= 1
                self.player.restore_mid_pos()
                for sprite in self.upgrades_group:
                    sprite.kill()
                for sprite in self.enemies_group:
                    sprite.kill()
                if self.player.health != 0:
                    self.health_lose_sound.play()
    
    def check_collision(self, direction):
        overlap_sprites = pygame.sprite.spritecollide(self,self.blocks_group, False)

        if self.rect.colliderect(self.player.rect):
            overlap_sprites.append(self.player)
        
        if overlap_sprites:
            if direction == "x":
                for sprite in overlap_sprites:
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left - 1
                        self.pos.x = self.rect.x
                        self.direction.x *= -1
                        self.bounce_sound.play()

                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right + 1
                        self.pos.x = self.rect.x
                        self.direction.x *= -1
                        self.bounce_sound.play()
                    
                    if getattr(sprite, "block_health", None):
                        sprite.get_damage(1)
                        sprite.update_image()

            if direction == "y":
                for sprite in overlap_sprites:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top - 1
                        self.pos.y = self.rect.y
                        self.direction.y *= -1
                        self.bounce_sound.play()

                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom + 1
                        self.pos.y = self.rect.y
                        self.direction.y *= -1
                        self.bounce_sound.play()

                    if getattr(sprite, "block_health", None):
                        sprite.get_damage(1)
                        sprite.update_image()

    def update(self):
        if self.active:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.old_rect = self.rect.copy()

            self.pos.x += self.direction.x * BALL_SPEED
            self.rect.x = round(self.pos.x)
            self.check_window_collision("x")
            self.check_collision("x")

            self.pos.y += self.direction.y * BALL_SPEED
            self.rect.y = round(self.pos.y)
            self.check_window_collision("y")
            self.check_collision("y")
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)
        
    def set_ball_state(self, start):
        self.active = start
        if start:
            self.bounce_sound.play()