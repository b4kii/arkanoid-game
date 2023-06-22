import pygame
from utils.text_data import KEYBINDS_SCENE_TEXT, WIN_SCENE_TEXT
from scenes.scene import Scene
from utils.text import Text
from config.constants import FONT_PATH, SH_MID, SW_MID, WHITE_COLOR

class KeybindsScene(Scene):
    def __init__(self, intro_scene):
        super().__init__()
        self.intro_scene = intro_scene
        self.text_list = self.get_text(KEYBINDS_SCENE_TEXT)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for text in self.text_list:
            text.update()
            text.draw(screen)

    def handle_events(self, events):
        for event in events:
            self.handle_shared_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    from scenes.intro_scene import IntroScene
                    self.manager.go_to(self.intro_scene)
