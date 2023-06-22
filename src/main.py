import pygame
from scenes.scene_manager import SceneManager
from config.constants import *
from scenes.intro_scene import IntroScene

def main():
    pygame.init()
    pygame.display.set_caption("Arkanoid")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    manager = SceneManager(IntroScene)

    while True:
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
