import pygame, sys, time, json, datetime
from random import choice, randint
from config.constants import *
from utils.spritesheet import Spritesheet
from utils.text import Text
from entities.player import Player
from entities.ball import Ball
from entities.block import Block
from entities.upgrade import Upgrade
from entities.enemy import Enemy
from scenes.scene import Scene

class GameScene(Scene, pygame.sprite.Sprite):
    def __init__(self):

        # Initial pygame setup
        super().__init__()

        # Music
        self.background_sound = pygame.mixer.Sound(GAME_SCENE_SOUND)
        self.background_sound.set_volume(BACKGROUND_SOUND_VOLUME)
        self.background_sound.play(-1)

        self.upgrade_sound = pygame.mixer.Sound(UPGRADE_SOUND)
        self.upgrade_sound.set_volume(EFFECTS_SOUND_VOLUME)

        self.enemy_hit_sound = pygame.mixer.Sound(ENEMY_HIT_SOUND)
        self.enemy_hit_sound.set_volume(EFFECTS_SOUND_VOLUME)

        # Background

        self.background_list = self.get_background_list()
        self.background_image = self.background_list[0]

        # Sprite Groups

        self.all_sprites = pygame.sprite.Group()
        self.block_sprites = pygame.sprite.Group()
        self.upgrade_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Player
        self.player = Player(self.all_sprites)
        self.paddle_health_image = Spritesheet(VAUS_SPRITES, 32, 0, 32, 8, scale=1, color_key=GREEN_COLOR).sprite_image

        self.player_score = [0]
        self.score_text = Text(self.player_score[0], WHITE_COLOR, SCREEN_WIDTH -120, BORDER_OFFSET + 15, 18, font_path=FONT_PATH)

        self.stage_counter = 0
        self.current_stage_text = Text("", WHITE_COLOR, SCREEN_WIDTH // 2, BORDER_OFFSET + 15, 18, font_path=FONT_PATH)

        # Ball
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites, self.upgrade_sprites, self.enemy_sprites)

        # Game state
        self.paused = False
        self.pause_text = Text("Paused", WHITE_COLOR, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 36, font_path=FONT_PATH)

    def handle_events(self, events):
        for event in events:
            self.handle_shared_events(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    from scenes.intro_scene import IntroScene
                    self.background_sound.stop()
                    self.manager.go_to(IntroScene())

                if event.key == pygame.K_SPACE:
                    self.ball.set_ball_state(True)
                
                if event.key == pygame.K_p:
                    self.paused = True
                    pygame.mixer.pause()
                
                # DEBUG
                if event.key == pygame.K_0:
                    self.kill_sprites(self.block_sprites)
                    self.stage_counter = len(BLOCK_MAPS)
                if event.key == pygame.K_9:
                    self.kill_sprites(self.block_sprites)
                if event.key == pygame.K_8:
                    self.player.health = 0

    def update(self):
        pass
    
    def draw_text(self, screen):
        self.screen = screen
        self.score_text.update()
        self.score_text.draw(screen)
        self.score_text.text = str(f"SCORE: {self.player_score[0]}")

        self.current_stage_text.text = str(f"STAGE: {self.stage_counter}")
        self.current_stage_text.update()
        self.current_stage_text.draw(screen)

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))

        if self.paused:
            from scenes.pause_scene import PauseScene
            self.manager.go_to(PauseScene(self))
            return

        self.all_sprites.update()
        self.upgrade_collision()
        self.enemy_collision()
        self.all_sprites.draw(screen)
        self.draw_health(screen)

        self.draw_text(screen)
        self.change_stage()

        number = randint(1, 2000)
        if number < 5:
            x = randint(1,SCREEN_WIDTH - 200)
            # self.create_enemy((x + 100, 40))
            self.create_enemy((x + 100, BORDER_OFFSET))

        pygame.display.update()
    
    def create_grid(self, index):
        block_map = BLOCK_MAPS[index]

        grid_width = (SCREEN_WIDTH - 200) / len(block_map[0]) - GAP_SIZE
        grid_height = 30

        for row_index, row in enumerate(block_map):
            for col_index, col in enumerate(row):
                if col != " ":
                    x = 100 + col_index * (grid_width + GAP_SIZE) + GAP_SIZE // 2
                    y = 100 + row_index * (grid_height + GAP_SIZE) + GAP_SIZE // 2
                    Block([self.all_sprites, self.block_sprites], col, (x, y), grid_width, grid_height, self.create_upgrade, self.player_score)

    def draw_health(self, screen):
        for i in range(self.player.health):
            x = 70 + i * (self.paddle_health_image.get_width() + 5)
            screen.blit(self.paddle_health_image, (x, BORDER_OFFSET + 10))
    
    def kill_sprites(self, sprite_group):
        for sprite in sprite_group:
            sprite.kill()
    
    def change_stage(self):
        if self.player.health == 0:
            self.save_score()
            from scenes.lose_scene import LoseScene
            self.background_sound.stop()
            self.manager.go_to(LoseScene(self))
            self.kill_sprites(self.block_sprites)
            self.kill_sprites(self.upgrade_sprites)
            self.kill_sprites(self.enemy_sprites)

        # Get next stage
        elif len(self.block_sprites) == 0:
            if self.stage_counter >= len(BLOCK_MAPS):
                self.save_score()
                from scenes.win_scene import WinScene
                self.background_sound.stop()
                self.manager.go_to(WinScene(self))
            else:
                self.background_image = self.background_list[self.stage_counter % len(self.background_list)]
                if self.stage_counter != 0:
                    from scenes.stage_change import StageChangeScene
                    self.manager.go_to(StageChangeScene(self))

                self.kill_sprites(self.upgrade_sprites)
                self.kill_sprites(self.enemy_sprites)
                self.ball.set_ball_state(False)
                self.create_grid(self.stage_counter)
                self.stage_counter += 1
                self.player.restore_mid_pos()
                self.player.remove_upgrades()

    def create_upgrade(self, pos):
        upgrade_type = choice(UPGRADES)
        Upgrade(pos, upgrade_type, [self.all_sprites, self.upgrade_sprites], self.screen)
    
    def upgrade_collision(self):
        overlap_sprites = pygame.sprite.spritecollide(self.player, self.upgrade_sprites, True)

        for sprite in overlap_sprites:
            self.upgrade_sound.play()
            self.player.upgrade(sprite.upgrade_type)
        
    def create_enemy(self, pos):
        upgrade_type = choice(UPGRADES)
        Enemy(pos, upgrade_type, [self.all_sprites, self.enemy_sprites], self.screen)
    
    def enemy_collision(self):
        overlap_sprites = pygame.sprite.spritecollide(self.player, self.enemy_sprites, True)

        for sprite in overlap_sprites:
            self.enemy_hit_sound.play()
            self.player.enemy_hit(sprite.upgrade_type)

    def save_score(self):
        data = {}
        if self.player_score[0]:
            try:
                with open(USER_DATA_JSON, "r") as file:
                    data = json.load(file)

                scores = data["best_scores"]
                scores.append({
                    "score": self.player_score[0],
                    "day": datetime.date.today().day,
                    "month": datetime.date.today().month,
                    "time": datetime.datetime.now().strftime("%H:%M:%S")
                })
                scores.sort(key=lambda x: x["score"], reverse=True)
                top_scores = scores[:5]
                data["best_scores"] = top_scores

                with open(USER_DATA_JSON, "w") as file:
                    json.dump(data, file)

            except json.JSONDecodeError:
                print(f"Invalid JSON format in file {USER_DATA_JSON}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    def get_background_list(self):
        pos_x, width, height = 232, 224, 239
        backgrounds = []
        for i in range(5):
            backgrounds.append(Spritesheet(FIELD_SPRITES, i * pos_x, 0, width, height, auto_scale=("width", SCREEN_WIDTH)).sprite_image)
        return backgrounds

