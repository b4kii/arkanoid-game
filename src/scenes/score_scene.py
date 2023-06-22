import pygame
import sys
from utils.text_data import SCORE_SCENE_TEXT
from scenes.scene import Scene
from utils.text import Text
from config.constants import FONT_PATH, SH_MID, SW_MID, WHITE_COLOR

class ScoreScene(Scene):
    def __init__(self, intro_scene):
        super().__init__()
        self.intro_scene = intro_scene
        self.text_list = self.get_text(SCORE_SCENE_TEXT)

        self.best_scores = self.read_scores()
        self.best_scores_list = self.get_scores()

        self.no_score_text = Text("No scores yet", WHITE_COLOR, SW_MID, SH_MID, font_size=32, font_path=FONT_PATH)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for text in self.text_list:
            text.update()
            text.draw(screen)
        
        if len(self.best_scores) == 0:
            self.no_score_text.update()
            self.no_score_text.draw(screen)
        else:
            for score in self.best_scores_list:
                score.update()
                score.draw(screen)

    def handle_events(self, events):
        for event in events:
            self.handle_shared_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.manager.go_to(self.intro_scene)

    def get_scores(self):
        scores_list = []
        text_offsets = [-60, -20, 20, 60, 100]
        for count, best_score in enumerate(self.best_scores):
            zero_month = "0" if best_score["month"] < 10 else ""
            zero_day = "0" if best_score["day"] < 10 else ""

            scores_list.append(Text(f"{count + 1}:   {best_score['score']} [ {best_score['time']} - {zero_day}{best_score['day']}/{zero_month}{best_score['month']} ]", WHITE_COLOR, SW_MID, SH_MID + text_offsets[count], font_size=24, font_path=FONT_PATH))
        return scores_list
