import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("pAsteroids")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surface.fill((0, 0, 0))
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    main()
