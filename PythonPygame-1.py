# 1 - https://www.qwant.com/?client=brz-moz&t=videos&q=pygame&o=0%3AWxEmflz009U
# 2 - https://www.youtube.com/watch?v=W4cbtcyONag
# 3 - https://www.youtube.com/watch?v=N56R1V5XZBw
import sys
import pygame

# pygame.init()
#
# # Creating colors
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# screen = pygame.display.set_mode((400, 400))
# screen.fill(WHITE)
#
# image = pygame.image.load("ball.png")
# image = pygame.transform.rotozoom(image, 0, 0.2)
#
# x = 0
# y = 0
#
# clock = pygame.time.Clock()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_LEFT]:
#         x -= 1
#     if pressed[pygame.K_RIGHT]:
#         x += 1
#     if pressed[pygame.K_UP]:
#         y -= 1
#     if pressed[pygame.K_DOWN]:
#         y += 1
#
#     """
#     On repeint en blanc le fond afin d'effacer les traces laisser par le deplacement du ballon.
#     """
#     screen.fill(WHITE)
#     screen.blit(image, (x, y))
#     pygame.display.flip()
#     clock.tick(60)

"""
pygame.display.update()
Les deux fonctions font la meme action elles mettent à jour les informations de l'écran en appliquant les
changements faits. Cependant pygame.display.update() a une particularité, à l'aide d'un tuple de 4 valeurs 
(x, y. width, height) ou d'un objet rect: pygame.Rect(x, y, width, height) nous pouvons définir la zone que nous
souhaitons mettre à jour. Ainsi si nous utilisons la méthode sous cette forme pygame.display.update((0, 0, 150, 150)) 
nous mettons à jour qu'un carré de 150 pixels par 150 pixels qui se trouve aux coordonnées 0, 0.
pygame.display.flip() quand à lui ne prend aucun paramètre et permet de mettre à jour l'écran entier. Cependant
flip a été codé avec certaine optimisations qui permettent de mettre à jour l'écran plus rapidement.
"""

"""
pygame en oriente objet
"""


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    #  Gestion des évènements
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Gestion de logique et de mise à jour de chaque élément du jeu
    def update(self):
        pass

    # Gestion de l'affichage
    def display(self):
        pass

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
