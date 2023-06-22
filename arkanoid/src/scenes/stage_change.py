import pygame
from utils.text import Text
from config.constants import FONT_PATH, SH_MID, SW_MID, WHITE_COLOR
from scenes.scene import Scene

class StageChangeScene(Scene):
    def __init__(self, game_scene):
        super().__init__()
        self.game_scene = game_scene
        self.text = Text(f"Stage: {self.game_scene.stage_counter + 1}", WHITE_COLOR, SW_MID, SH_MID, font_path=FONT_PATH)
        self.duration = 2 
        self.clock = pygame.time.Clock()
        self.elapsed_time = 0

    def update(self):
        self.elapsed_time += self.clock.tick() / 1000

        if self.elapsed_time >= self.duration:
            self.manager.go_to(self.game_scene)

    def draw(self, screen):
        screen.blit(self.background_image, (0,0))
        self.text.update()
        self.text.draw(screen)

    def handle_events(self, events):
        pass
