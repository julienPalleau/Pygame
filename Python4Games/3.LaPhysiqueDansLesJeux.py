# https://www.python4games.fr/la-physique-dans-les-jeux-bouger-les-objets-avec-precision/
"""
La physique dans les jeux: Bouger les objets avec précision

Introduction
La physique dans les jeux vidéo joue un rôle crucial dans la création de monde interactifs et réalistes. 
Grâce à la simulation des forces, de la gravité et des collisions, les objets peuvent réagir aux interactions
de manière cohérente, permettant de créer des environnements plus immersifs. Dans cet article, nous
explorerons les concepts essentiels de la physique dans les jeux vidéo, notamment la gestion des collisions,
l'application des forces et mouvements, et la simulation de la gravité et de l'inrertie.

Avec des exemples concrets en Pygame, vous apprendrez comment intégrer ces concepts pour donner vie à des objets en mouvement.
"""

"""
1. Gestion des collisions
Les Collisions sont un aspect fondamental de la physique des jeux vidéo, permettant aux objets d'interagir entre eux. La gestion précise des collisions est
essentielle pour s'assurer que les objets ne traversent pas les murs, que les balles rebondissent correctement, ou que les personnages sautent sur des
plateformes. 

Détection des collisions en 2D avec Pygame

En 2D, la détection des collisions est généralement basée sur la superposition de rectangles (bounding boxes) qui entourent les objets. Dans Pygame, chaque sprite possède
un rect (rectangle) qui définit sa position et ses dimensions. La méthode colliderect() permet de vérifier si deux rectangles se chevauchent.

Voici un exemple simple de détection de collision entre deux objets:
"""
# import pygame

# # Initialisation de Pygame
# pygame.init()

# # Créer une fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))

# # Créer deux rectangles pour représenter les objets
# rect1 = pygame.Rect(100, 100, 50, 50) # Rectangle pour l'objet 1
# rect2 = pygame.Rect(300, 100, 50, 50) # Rectangle pour l'objet 2

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Déplacer le rect1 à droite pour tester la collision
#     rect1.x += 1

#     # Détection de collision entre rect1 et rect2
#     if rect1.colliderect(rect2):
#         print("Collision détectée!")

#     # Raffraîchir l'écran
#     screen.fill((255, 255, 255)) # Effacer l'écran avec une couleur blanche
#     pygame.draw.rect(screen, (255, 0, 0), rect1) # Dessiner rect1 en rouge
#     pygame.draw.rect(screen, (0, 255, 0), rect2) # Dessiner rect2 en bleu
#     pygame.display.flip()
# pygame.quit()



"""
Types de collisions dans les jeux
    1. Collision statiques: Lorsqu'un objet rencontre un obstacle immobile, comme un mur ou une plateforme.
    2. Collision dynamiques: Quand deux objets en mouvement se percutent, comme deux balles dans un jeu de billard.

Résolution des collisions
Une fois qu'une collision est détectée, il est important de résoudre la collision pour éviter que les objets ne se chevauchent. 
Cela peut impliquer de 
    + Inverser la direction de l'objet (par exemple, un rebond).
    + Stopper l'objet lorsqu'il touche un mur.
    + Réduire la vitesse (simuler la perte d'énergie lors d'une collision). 
"""

"""
2.Appliquer des forces et mouvements
La simulation des mouvements réalistes dans les jeux vidéo repose sur l'application de forces qui modifient la vitesse et la position des objets. 
Les forces peuvent être continues (comme la gravité) ou ponctuelles (comme une explosion).

Mouvement de base

Le mouvement d'un objet est souvent contrôlé par sa vitesse(velocity), qui est mise à jour en fonction du temps. Par exemple, un objet qui se déplace à une
vitesse constante sur l'axe X pourrait être mis à jour à chaque cycle de la boucle de jeu. 
"""
# import pygame

# # Initialisation de Pygame
# pygame.init()

# # Créer une fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))

# # Créer deux rectangles pour représenter les objets
# rect1 = pygame.Rect(100, 100, 50, 50) # Rectangle pour l'objet 1
# rect2 = pygame.Rect(300, 100, 50, 50) # Rectangle pour l'objet 2

# # Variables pour la position et la vitesse de l'objet
# x, y = 100, 200
# speed_x, speed_y = 5, 0 # Mouvement constant à droite

# # Accélération vers la droite
# acceleration_x = 0.1
# velocity_x = 0
# position_x = 100

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Appliquer l'accélération à la vitesse
#     velocity_x += acceleration_x
    
#     # Mettre à jour la position en fonction de la vitesse
#     position_x += velocity_x

#     # Déplacer le rect1 à droite pour tester la collision
#     rect1.x += 1

#     # Détection de collision entre rect1 et rect2
#     if rect1.colliderect(rect2):
#         print("Collision détectée!")

#     # Mise à jour de la position
#     x += speed_x
#     y += speed_y

#     # Raffraîchir l'écran
#     screen.fill((255, 255, 255)) # Effacer l'écran avec une couleur blanche
#     pygame.draw.rect(screen, (255, 0, 0), rect1) # Dessiner rect1 en rouge
#     pygame.draw.rect(screen, (0, 255, 0), rect2) # Dessiner rect2 en bleu
#     pygame.draw.circle(screen, (0, 0, 255), (x, y), 20) # Dessiner un cercle représentant l'objet
#     pygame.draw.circle(screen, (0, 128, 128), (int(position_x), 300), 20) # Dessiner un cercle représentant l'objet

#     pygame.display.flip()

#     pygame.time.Clock().tick(60) # Limiter à 60 FPS

#     pygame.display.flip()
# 


"""
3. Simulation de la gravité et de l'inertie
La gravité est une force universelle dans de nombreux jeux vidéo, simulant la façon dont les objets tombent vers le sol.
Combinée à l'inertie (la tendance d'un objet à maintenir son mouvemnent à moins qu'une force ne l'en empêche), elle permet
de créer des mouvements plus naturels et réalistes.

Simuler la gravité

Pour simuler la gravité, il suffit d'appliquer une force constante vers le bas sur l'objet. Cette force augmente la vitesse de l'objet,
ce qui simule une chute.

Voici un exemple simple où un objet tombe sous l'effet de la gravité:
"""
# import pygame

# # Initialisation de Pygame
# pygame.init()

# # Créer une fenêtre de jeu
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Gravity")

# x, y = 100, 100
# velocity_y = 0
# gravity = 0.5 # Force constante vers le bas
# running = True

# while running:
#     # Appliquer la gravité à la vitesse
#     velocity_y += gravity
#     y += velocity_y

#     # Empêcher l'objet de tomber en dessous du sol
#     if y > 600: # Sol à 600 pixels
#        
#         velocity_y = 0 # Stopper la chute

#     # Afficher l'objet
#     screen.fill((255, 255, 255)) # Effacer l'écran avec une couleur blanche
#     pygame.draw.circle(screen, (0, 0, 255), (x, int(y)), 20) # Dessiner un cercle représentant l'objet
#     pygame.display.flip()

#     pygame.time.Clock().tick(60) # Limiter à 60 FPS
# pygame.quit()
"""
Dans cet exemple:
    + gravity = 0.5: La gravité est appliquée à chaque cycle de la boucle de jeu, augmentant la vitesse verticale de l'objet au fil du temps.
    + Collision avec le sol: Lorsque l'objet atteint le sol (y > 600), sa vitesse verticale est réinitialisée à zéro pour simuler un atterrissage.
"""

"""
Simuler l'inertie

L'inertie est la tendance d'un objet à continuer de se déplacer dans la même direction jusqu'à ce qu'une force s'y oppose (comme la friction ou une 
collision). Dans un jeu, cela peut être simulé en laissant l'objet continuer à bouger avec sa vitesse actuelle jusqu'à ce qu'il rencontre un obstacle ou que sa
vitesse diminue à cause de forces opposées (comme le frottement de l'air).

Par exemple, si un objet en mouvement horizontal continuerait de se déplacer même après que le joueur ait relâché la touche de déplacement, ♂ moins que la
vitesse diminue à cause des forces opposées (comme le frottement de l'air).

Par exemple, un objet en mouvement horizontal continuerait de se déplacer même après que le joueur ait relâché la touche de déplacement, à moins que la
friction ou une autre force ne l'arrête.
"""
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Inertia")   

# Appliquer une légère friction pour ralentir l'objet
friction = 0.98
running = True

x, y = 50, 50

velocity_x = 10
velocity_y = 0
gravity = 0.5 # Force constante vers le bas
running = True

while running:
    # Appliquer la gravité à la vitesse
    friction = 0.98

    velocity_y += gravity
    y += velocity_y

    # Empêcher l'objet de tomber en dessous du sol
    if y > 580: # Sol à 600 pixels
        y = 580
        velocity_y = 0 # Stopper la chute

    # Appliquer la friction à la vitesse
    velocity_x *= friction
    x += velocity_x

    # Afficher l'objet
    screen.fill((255, 255, 255)) # Effacer l'écran avec une couleur blanche
    pygame.draw.circle(screen, (0, 200, 255), (x, int(y)), 20) # Dessiner un cercle représentant l'objet
    pygame.draw.circle(screen, (0, 0, 255), (int(x+100), 300), 20) # Dessiner un cercle représentant l'objet
    pygame.display.flip()   
    clock = pygame.time.Clock().tick(60) # Limiter à 60 FPS

    if velocity_x < 0.1:
        running = False
pygame.quit()
"""
Conclusion

Les concepts de physique dans les jeux vidéo sont essentiels pour donner vie à vos projets en créant des interactions réalistes et immersives.
La gestion des collisions, l'application de forces et la simulation de la gravité et de l'inertie permettent de créer des mouvements crédibles
et d'améliorer l'expérience du joueur.

En maîtrisant ces techniques, vous pourrez concevoir des jeux où les objets interagissent de manière fluide, simulant les lois du monde physique et
enrichissant le gameplay.
"""