# https://www.python4games.fr/introduction-aux-graphismes-2d-dans-pygame/
"""
Introduction aux graphismes 2D dans Pygame

Les graphismes 2D sont essentiels dans le développement de jeux vidéo, offrant aux développeurs une manière de présenter des personnages, des
objets et des environnements. Pygame, une bibliothèque Python largement utilisée pour les jeux 2D, simplifie le processus de gestion des images,
d'animation des personnages avec des sprites et de création d'effets visuels.

Dans cet article, nous allons explorer trois concepts clés des graphismes 2D dans Pygame : 
    1. Importer et afficher des images.
    2. Animer des personnages avec des sprites.
    3. Gérer les arrières-plans et les effets visuels.
"""


"""
1. Importer et afficher des images dans Pygame

L'un des premiers éléments graphiques que vous voudrez ajouter à un jeu est probablement une image. Dans Pygame, il est facile d'importer des images et
de les afficher à l'écran, qu'il s'agisse de personnages, d'objets ou d'éléments de l'interface utilisateur.

Charger une image

Pygame prend en charge différents formats d'image, notamment PNG, JPEG et BMP. Pour importer une image dans Pygame, vous devez utiliser la fonction
pygame.image.load() qui charge l'image dans la mémoire.
"""
# import pygame

# # Inititalisation de Pygame
# pygame.init()

# # Créer une fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))

# # Charger une image
# player_image = pygame.image.load(r'C:\Users\jpall\Documents\GitHub\Pygame\Python4Games\player.png')

# # Position initiale de l'image
# player_x = 100
# player_y = 100

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Effacer l'écran
#     screen.fill((255, 255, 255)) # Remplir l'écran de blanc

#     # Afficher l'image à la position spécifiée
#     screen.blit(player_image, (player_x, player_y))

#     # Mettre à jour l'affichage
#     pygame.display.flip()

# pygame.quit()


"""
Explication du code:
    + pygame.image.load(r'C:\\Users\jpall\Documents\GitHub\Pygame\Python4Games\player.png') : Cette fonction charge l'image spécifiée et la prépare pour être utilisée dans le jeu.
    + screen.blit(): Affiche l'image aux coordonnées (x, y)

Gestion de la transparence
Pour les jeux 2D, il est souvent nécessaire de gérer la transparence pour que les objets puissent être placés sur différents arrière-plans sans afficher un fond
carré ou rectangulaire autour d'eux. Pygame permet cela grâce à la fonction convert_alpha(), qui gère les images avec des canaux alpha (transparence).
    player_image = pygame.image.load(r'C:\\Users\jpall\Documents\GitHub\Pygame\Python4Games\player.png').convert_alpha()
"""


"""
2. Animer des personnages avec des sprites

Les sprites sont des images ou des animations qui représentent des personnages, des ennemis ou des objets dans un jeu. En Pygame, les sprites peuvent
être animés en modifiant leur position, en changeant les images utilisées pour les représenter ou en créant des séquences d'animations.

Animations de sprites avec plusieurs images

Une aninmation simple peut être réalisée en utilisant plusieurs images, représentant chaque étape du mouvement d'un personnage (par exemple, un personnage qui marche).
"""
import pygame

# Initialisation de Pygame
pygame.init()

# Créer une fenêtre de jeu
screen = pygame.display.set_mode((800, 600))

# Charger les images pour l'animation (par exemple, personnage qui marche)
walk_right = [pygame.image.load(r'Python4Games/tile000.png'),
              pygame.image.load(r'Python4Games/tile001.png'),
              pygame.image.load(r'Python4Games/tile002.png'),
              pygame.image.load(r'Python4Games/tile003.png'),
              pygame.image.load(r'Python4Games/tile004.png'),
              pygame.image.load(r'Python4Games/tile005.png'),
              pygame.image.load(r'Python4Games/tile006.png')]
# Variables pour l'animation
player_x = 100
player_y = 100
current_frame = 0
frame_rate = 5 # Nombre d'images par seconde pour l'animation
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Mettre à jour et afficher la prochaine image de l'animation
    screen.blit(walk_right[current_frame], (player_x, player_y))

    # Mettre à jour le cadre actuel toutes les "frame rate" frames
    current_frame = (current_frame + 1) % len(walk_right)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Controler la vitesse de l'animation
    clock.tick(frame_rate)
pygame.quit()
"""
Explication du code:
    + walk_right: Contient une liste d'images représentant les différentes étapes de l'animation.
    + current_frame: Suit l'image actuelle affichée pour l'animation.
    + clock.time(frame_rate): Contrôler la vitesse à laquelle les images sont changées, permettant de régler le nombre d'images affichées par seconde.


Utilisation de la classe Sprite dans Pygame

Pygame offre une classe Sprite pour faciliter la gestion des objets animés, avec des méthodes permettant de mettre à jour les sprites et de afficher
efficacement.
"""

