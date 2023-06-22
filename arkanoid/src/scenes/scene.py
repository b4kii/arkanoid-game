import json
import pygame, sys
from utils.spritesheet import Spritesheet
from utils.text import Text
from config.constants import FIELD_SPRITES, FONT_PATH, SCREEN_WIDTH, USER_DATA_JSON

class Scene(object):
    def __init__(self):
        self.mute = False
        self.background_image = Spritesheet(FIELD_SPRITES, 8, 264, 207, 231, auto_scale=("width", SCREEN_WIDTH)).sprite_image

    def update(self):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError
    
    def handle_events(self, event):
        raise NotImplementedError
    
    def get_text(self, text_data):
        text_list = []
        
        for item in text_data.values():
            text_list.append(Text(item["text"], item["color"], item["pos_x"],item["pos_y"], font_size=item["font_size"], font_path=FONT_PATH))

        return text_list

    def handle_shared_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_m:
                self.mute = not self.mute
                if self.mute:
                    pygame.mixer.pause()
                else:
                    pygame.mixer.unpause()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    def read_scores(self):
        data, best_scores = {}, []
        try:
            with open(USER_DATA_JSON, "r") as file:
                data = json.load(file)
            
            best_scores = data.get("best_scores", [])

        except json.JSONDecodeError:
            print(f"Invalid JSON format in file {USER_DATA_JSON}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return best_scores