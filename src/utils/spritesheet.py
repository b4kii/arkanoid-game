import pygame
from config.constants import *


class Spritesheet:
    def __init__(self, file_name, x1, y1, width, height, scale=1, scale_dimensions=(0, 0), auto_scale=("", None), color_key=None):
        self.sprite_image = pygame.image.load(file_name).convert_alpha()
        self.color_key = color_key
        self.get_cut_out(x1, y1, width, height, scale=scale, scale_dimensions=scale_dimensions, auto_scale=auto_scale)
    
    def get_sprite(self, x1, y1, width, height, scale=1):
        sprite_clipped = pygame.Surface([width, height])
        sprite_clipped.blit(self.sprite_image, (0, 0), (x1, y1, width, height))
        sprite_clipped = pygame.transform.scale(sprite_clipped, (width * scale,height * scale))
        sprite_clipped.set_colorkey(self.color_key)
        return sprite_clipped

    def scale_image(self, image, scale, scale_dimensions, auto_scale):
        scale_factor = auto_scale[0] == "" and scale

        if auto_scale[0] == "width":
            scale_factor = auto_scale[1] / image.get_width()
        if auto_scale[0] == "height":
            scale_factor = auto_scale[1] / image.get_height()

        scaled_image = None

        if scale_dimensions[0] == 0 and scale_dimensions[1] == 0:
            scaled_width = image.get_width() * scale_factor
            scaled_height = image.get_height() * scale_factor
            scaled_image = pygame.transform.scale(
                image, (scaled_width, scaled_height))
        else:
            scaled_image = pygame.transform.scale(image, (scale_dimensions[0], scale_dimensions[1]))

        return scaled_image

    def get_cut_out(self, x1, y1, width, height, scale, scale_dimensions, auto_scale):
        image_clipped = self.get_sprite(x1, y1, width, height)

        self.sprite_image = self.scale_image(image_clipped, scale=scale, scale_dimensions=scale_dimensions, auto_scale=auto_scale)
        # return self