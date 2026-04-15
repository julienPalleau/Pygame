# https://www.python4games.fr/creer-votre-premier-jeu-avec-pygame-une-introduction-simple-avec-une-balle-qui-rebondit/
import pygame

# Initialize Pygame
pygame.init()

# Créer une fenêtre de jeu
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Balle qui rebondit")

# Couleur de l'arrière-plan de la balle
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Position et vitesse de la balle
ball_x = 320
ball_y = 240
ball_speed_x =3
ball_speed_y = 3

# Rayon de la balle
ball_radius = 20

running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacer la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Faire rebondir la balle sur les bords de la fenêtre
    if ball_x - ball_radius < 0 or ball_x + ball_radius > 640:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > 480:
        ball_speed_y = -ball_speed_y

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner la balle
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la boucle à 60 images par seconde
    pygame.time.Clock().tick(60)

pygame.quit()
