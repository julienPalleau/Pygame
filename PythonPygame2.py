# 3 - https://www.youtube.com/watch?v=N56R1V5XZBw
import sys
import pygame
from PythonPygame3 import Player


"""
pygame en oriente objet
"""


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0)
        self.area = pygame.Rect(300, 150, 300, 300)
        self.area_color = "red"

    #  Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

    # Gestion de logique et de mise à jour de chaque élément du jeu
    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "blue"
        else:
            self.area_color = "red"

    # Gestion de l'affichage
    def display(self):
        self.screen.fill("white")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.player.draw(self.screen)
        pygame.display.flip()

    # Boucle du jeu
    def run(self):
        while True:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((1000, 720))
game = Game(screen)
game.run()
