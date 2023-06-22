import pygame
import sys
from utils.text_data import LOSE_SCENE_TEXT
from scenes.scene import Scene
from utils.text import Text
from config.constants import BACKGROUND_SOUND_VOLUME, EFFECTS_SOUND_VOLUME, FONT_PATH, LOSE_SOUND, SH_MID, SW_MID, WHITE_COLOR

class LoseScene(Scene):
    def __init__(self, game_scene):
        super().__init__()
        self.game_scene = game_scene
        self.player_score_text = Text(f"Score: {game_scene.player_score[0]}", WHITE_COLOR, SW_MID, SH_MID - 60, font_size=32, font_path=FONT_PATH)
        self.player_stage_text = Text(f"Stage: {game_scene.stage_counter}", WHITE_COLOR, SW_MID, SH_MID - 20, font_size=32, font_path=FONT_PATH)

        self.background_sound = pygame.mixer.Sound(LOSE_SOUND)
        self.background_sound.set_volume(EFFECTS_SOUND_VOLUME)
        self.background_sound.play()

        self.text_list = self.get_text(LOSE_SCENE_TEXT)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for text in self.text_list:
            text.update()
            text.draw(screen)

        self.player_score_text.update()
        self.player_score_text.draw(screen)
        self.player_stage_text.update()
        self.player_stage_text.draw(screen)

    def handle_events(self, events):
        for event in events:
            self.handle_shared_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    from scenes.intro_scene import IntroScene
                    self.game_scene.background_sound.stop()
                    self.background_sound.stop()
                    self.manager.go_to(IntroScene())
                if event.key == pygame.K_SPACE:
                    from scenes.game_scene import GameScene
                    self.game_scene.background_sound.stop()
                    self.background_sound.stop()
                    self.manager.go_to(GameScene())
