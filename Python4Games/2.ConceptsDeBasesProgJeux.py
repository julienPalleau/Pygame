# https://www.python4games.fr/concepts-de-base-de-la-programmation-de-jeux-boucles-de-jeu-evenements-et-gestion-des-sprites/
"""
Concepts de base de la programmation de jeux : Boucles de jeu, événements, et gestion des sprites

La programmation de jeux vidéo repose sur une série de concepts fondamentaux qui permettent de créer des expériences interactives et virtuellement
captivantes. Parmi ces concepts, trois se démarquent comme essentiels. la boucle de jeu, la gestion des événements et des entrées utilisateur,
ainsi que l'affichage des sprites. Que vous développiez un jeu simple en 2D ou un project complexe, la compréhension de ces concepts vous permettra
de poser des bases solides pour la programmation de jeux vidéo.

Cet article explore ces notions en profondeur, en utilisant Pygame, l'une des bibliothèques les plus populaires pour le développement de jeux en 2D.


1. Boucle de jeu (Game Loop): comprendre les fondemnents
La boulcle de jeu, ou game loop, est l'élément central de tout jeu vidéo. C'est un mécanisme qui permet au jeu de rester actif, en actualisant l'affichage,
en cours.

Fonctionnement de la boucle de jeu

La boucle de jeu repose sur trois étapes principales:
    1. Gestion des événements: Capture des actions de l'utilisateur (comme appuyer sur une touche ou cliquer sur un bouton).
    2. Mise à jour de la logique du jeu: Calcul des changements à appliquer (comme le déplacement d'un personnage ou la vérification des collisions).
    3. Rendu graphique: Affichage des éléments du jeu à l'écran.

Voici un schéma simple d'une boucle de jeu en Pygame:
"""
# import pygame

# # Initialisation de Pygame
# pygame.init()

# # Création de la fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Boucle de jeu en Pygame")

# # Création d'une horloge pour contrôler les FPS
# clock = pygame.time.Clock()

# # Variable pour maintenir la boucle de jeu active
# running = True

# while running:
#     # 1. Gestion des événements
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # 2. Logique du jeu (mouvements, calculs, etc.)
#     # Exemple : Déplacer un objet, vérifier les collisions

#     # 3. Rendu graphique
#     screen.fill((0, 0, 0)) # Remplir l'écran de noir
#     # Dessiner ici des objets

#     # Actualiser L'affichage
#     pygame.display.flip()

#     # Limiter la vitesse de la boucle à 60 FPS
#     clock.tick(60)

# # Quitter Pygame
# pygame.quit()

"""
Explication de la boucle de jeu:
    + Gestion des événements: Permet de capturer et réagir aux actions de l'utilisateur.
    + Mise à jour de la logique: Les éléments du jeu sont modifés en fonction des interactions (déplacement des objets, vérification des conditions
      de victoire ou défaite).
    + Rendu graphique: L'écran est actualisé pour afficher les objets à leur nouvelle position ou état.

La fréquence de rafraîchissement (FPS) est contrôlée par pygame.time.Clock().tick(60), ce qui limite la boucle à 60 images par seconde,
garantissant ainsi une fluidité optimale. 
"""


"""
2. Gestion des événements et des entrées utilisateur
Les jeux vidéo sont interactifs par nature. La gestion des événements permet au jeu de réagir aux entrées utilisateur telles que les clics de souris, les
frappes de touches, ou le mouvement de la manette. Pyggame offre un système robuste pour capturer et gérer ces événements.

Gestions des événements avec Pygame

Pygame utilise une boucle dévénements pour capturer tout ce qui se passe pendant le jeu, comme les actions de joueur (fermer la fenêtre, déplacer un
personnage, tirer, etc.). Tous ces événements sont recueillis dans une liste que vous parcourez dans la boucle de jeu.

Voici un exemple simple pour détacher la fermeture de la fenêtre et l'appui sur une touche du clavier
"""
# import pygame

# # Initialisation de Pygame
# pygame.init()

# # Création de la fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Boucle de jeu en Pygame")

# # Création d'une horloge pour contrôler les FPS
# clock = pygame.time.Clock()

# # Variable pour maintenir la boucle de jeu active
# running = True

# while running:
#     # 1. Gestion des événements
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 print("Flèche gauche appuyée")
#             if event.key == pygame.K_RIGHT:
#                 print("Flèche droite appuyée")


#     # 3. Rendu graphique
#     screen.fill((0, 0, 0)) # Remplir l'écran de noir
#     # Dessiner ici des objets

#     # Actualiser L'affichage
#     pygame.display.flip()

#     # Limiter la vitesse de la boucle à 60 FPS
#     clock.tick(60)

# # Quitter Pygame
# pygame.quit()
"""
Types d'événements communs dans Pygame:
    + QUIT: Se produit lorsque l'utilisateur ferme la fenêtre du jeu.
    + KEYDOWN: Se produit lorsqu'une touche du clavier est enfoncée.
    + KEYUP: Se produit lorsqu'une touche du clavier est relâchée.
    + MOUSEBUTTONDOWN: Se produit lorsqu'un bouton de la souris est enfoncé.
    + MOUSEBUTTONUP: Se produit lorsqu'un bouton de la souris est relâché.
    + MOUSEMOTION: Se produit lorsque la souris est déplacée.

Gestion des entrées utilisateur en temps réel
Pour des actions continues comme le mouvement d'un personnage, il est souvent plus pratique de vérifier si une touche est maintenue enfoncée plutôt que 
de réagir uniquement à l'appui initial. Voici comment détecter si des touches sont préssées en continu:
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    print("Le joueur se déplace à gauche")
if keys[pygame.K_RIGHT]:
    print("Le joueur se déplace à droite")

Avec cette méthode, vous pouver facilement contrôler les mouvements continus, comme le déplacement d'un personnage ou le défilement d'un
environnement de jeu.
"""


"""
3. Affichage et gestion des sprites

Les sprites sont des objets graphiques utilisés pour représenter les éléments visuels d'un jeu, comme les personnages, les objets, ou les ennemis.
En programmation de jeux, les sprites sont souvent des images avec des propriétés comme la position, la taille, et les animations.

Création et affichage de sprites avec Pygame

Dans Pygame, les sprites sont généralement gérés à l'aide de la classe Sprite, qui offre une structure pour organiser les objets graphiques. Voici un exemple
simple pour créer un sprite qui représente un personnage ou un objet.
"""
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\jpall\Documents\GitHub\Pygame\Python4Games\player.png').convert_alpha() # Charger une image pour le sprite
        self.image = pygame.transform.smoothscale(self.image, (70, 70)) # Redimensionner l'image du sprite
        self.rect = self.image.get_rect() # Créer un rectangle autour de l'image pour la gestion des collisions
        self.rect.center = (320, 240) # Positionner le sprite au centre de la fenêtre

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Créer une instance de la classe Player
player = Player()

# Ajouter le sprite à un groupe de sprites pour une gestion collective
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettre à jour tous les sprites
    all_sprites.update()

    # Dessiner tous les sprites
    screen.fill((255, 255, 255)) # Remplir l'écran de blanc
    all_sprites.draw(screen) # Dessiner tous les sprites du groupe
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
"""
Explication :
    + pygame.sprite.Sprite: Représent un objet graphique avec des propriétés (image, position, taille).
    + pygame.image.load(): Charger une image depuis un fichier pour l'utiliser comme sprite.
    + self.rect: Définit la position et la taille du sprite. Ce rectangle permet aussi de gérer les collisions.
    + update(): Méthode appelée à chaque cycle de la boucle de jeu pour mettre à jour la position du sprite. 

Conclusion :
Les boucles de jeu, la gestion des événements, et l'affichage des sprites sont les piliers de la programmation de jeux vidéo. 
Maîtriser ces concepts vous permettra de créer des jeux interactifs et visuellement attrayants, que ce soit en 2D ou en 3D. 
Pygame offre une excellente plateforme pour apprendre et mettre en pratique ces concepts, avec une structure simple et des
outils puissants pour créer des jeux fonctionnels.

En comprenant comment fonctionne la boucle de jeu, comment capturer les événements utilisateur et comment manipuler des sprites,
vous êtes sur la bonne voie pour développer vos propres jeux vidéo.
"""