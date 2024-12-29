# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_caption("Asteroids")
    pygame.Surface.fill(screen, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    pygame.display.flip()

if __name__ == "__main__":
    main()