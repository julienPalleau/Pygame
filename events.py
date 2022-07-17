import pygame
import sys


def gameloop():
    game = 1
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = 0

    pygame.quit()
    sys.exit()
