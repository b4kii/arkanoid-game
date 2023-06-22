import pygame
from config.constants import BACKGROUND_SOUND_VOLUME, FIELD_SPRITES, INTRO_SOUND, SCREEN_WIDTH
from utils.text_data import INTRO_SCENE_TEXT
from scenes.scene import Scene

class IntroScene(Scene):
    def __init__(self):
        super().__init__()

        self.text_list = self.get_text(INTRO_SCENE_TEXT)

        self.intro_sound = pygame.mixer.Sound(INTRO_SOUND)
        self.intro_sound.set_volume(BACKGROUND_SOUND_VOLUME)
        self.intro_sound.play(-1)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        for text in self.text_list:
            text.update()
            text.draw(screen)

        pygame.display.update()

    def handle_events(self, events):
        for event in events:
            self.handle_shared_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    from scenes.game_scene import GameScene
                    self.intro_sound.stop()
                    self.manager.go_to(GameScene())
                if event.key == pygame.K_k:
                    from scenes.keybinds_scene import KeybindsScene
                    self.manager.go_to(KeybindsScene(self))
                if event.key == pygame.K_s:
                    from scenes.score_scene import ScoreScene
                    self.manager.go_to(ScoreScene(self))
    
    def update(self):
        pass