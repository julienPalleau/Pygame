# https://fr.acervolima.com/pygame-dessiner-des-objets-et-des-formes/
"""
Dessiner des ojbets et des formes dans PyGame
Vous pouvez facilement dessiner des formes des bases dans pygame en utilisant la méthode de dessin de pygame.

Forme de rectangle de dessin:
Pour dessiner un rectangle dans votre projet pygame, vous pouvez utiliser la fonction draw.rect()

Syntaxe: pygame.draw.rect(surface, couleur, rect, largeur)
Paramètres:
    + surface: Ici, nous pouvons passer la surface sur laquelle nous voulons dessiner notre rectangle. Dans l'exemple
      ci-dessus, nous avons créé un objet surface nommé <<fenêtre>>.
    + color: Ici, nous pouvons passer la couleur de notre rectangle. Nous utilisons la couleur bleue dans notre exemple.
    + rect: Ici, nous pouvons passer le rectangle, la position et les dimensions.
    + width: Ici, nous pouvons passer l'épaisseur de la ligne. Nous pouvons également créer un rectangle plein en
      changeant la valeur de ce parmètre de largeur.

Tout d'abord, importez le module requis et initialisez pygame. Maintenant, créez l'objet surface d'une dimension
spécifique à l'aide de la méthode display.set_mode() de pygame. Remplissez l'arrière-plan de l'objet surface de couleur
blanche à l'aide de la fonction fill() de pygame. Créez un rectangle en utilisant la méthode draw.rect() de pygame.
Mettez à jour l'objet Surface.

Exemple1: dessin d'un rectangle délimité à l'aide de pygame.
"""
## Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object
# # of specific dimension
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of
# # pygame to draw the outlined rectangle
# pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 2)

"""
Nous pouvons créer un rectangle solide en définissant le paramètre de largeur égale à 0 et le reste de l'approche reste
le même.
Exemple 2: dessin d'un rectangle plein
"""
## Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object
# # of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with the color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of
# # pygame to draw the solid rectangle
# pygame.draw.rect(window, (0, 0, 255), [100, 100, 400, 100], 0)

"""
Forme du cercle de dessin:
Pour dessiner un cercle dans votre projet pygame, vous pouvez utiliser la fonction draw.circle(). L'approche entière 
est la même que ci-dessus, seuls la fonction et les paramètres sont modifiés en conséquence.

Syntaxe: pygame.draw.circle(surface, couleur, centre, rayon, largeur)
Paramètres:
    + Surface: Ici, nous pouvons passer la surface sur laquelle nous voulons dessiner notre cerlce. Dans l'exemple 
    ci-dessus, nous avons créé un objet surface nommé <<fenêtre>>.
    + Couleur: Ici, nous pouvons passer la couleur de notre cercle. Nous utilisons la couleur verte dans notre exemple.
    + Center: Ici, nous pouvons passer les coordonnées (x, y) pour le centre du cercle.
    + rayon: Ici, nous pouvons passer le rayoun de notre cercle.
    + width: Ici, nous pouvons passer l'épaisseur de la ligne. nous pouvons également créer un cercle plein en changeant
    la valeur de ce paramètre de d'épaisseur.
"""
# # Importing pygame module
# import pygame
# from pygame.locals import *
#
# # Initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object
# # of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of pygame to draw the solid circle
# pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 3)

"""
Nous pouvons créer un cercle solide en définissant le paramètre d'épaisseur égal à 0.
"""
# # Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # create the display surface object of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of pygame to draw the solid circle
# pygame.draw.circle(window, (0, 255, 0), [300, 300], 170, 0)


"""
Dessiner une forme de polygone:
Le polygone souhaité peut être dessiné à l'aide de la fonction polygon().
    Syntaxe: polygon(surface, couleur, points, largeur)
    
Là encore, l'approche reste la même, seule la fonction et les parmètres changent.

Exemple 1: dessiner un polygone solide
"""
# # Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of
# # pygame to draw the outlined polygon
# pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]])
#
# # Draw the surface object to the screen.
# pygame.display.update()


"""
Dessiner un polygone creux
"""
# # Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission
# # to use pygame's functionality
# pygame.init()
#
# # create the display surface object of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of pygame to draw the outlined polygon
# pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400], [100, 300]], 5)

"""
Forme de la ligne de dessin:
Une ligne est l'entité de dessin la plus basique et peut être dessinée dans pygame en utilisant la fonction line().
Syntax : pygame.draw.line(surface, color, start_pos, end_pos, width)

Exemple 1: tracer une ligne
"""

# # Importing pygme module
# import pygame
# from pygame.locals import *
#
# # Initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object
# # of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with wite color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of pygame to draw the line
# pygame.draw.line(window, (0, 0, 0), [100, 300], [500, 300], 5)
#
# # Draws the surface object to the screen.
# pygame.display.update()


"""
Dessinez plusieurs formes:
Vous pouvez dessiner plusieurs formes sur le même objet de surface. Pour cela, les premiers modules requis sont importés
et pygame est initialisé. Maintenant, créez l'objet surface d'une dimension spécifique en utilisant la méthode  
display.set_mode() de pygame. Remplissez l'arrière-plan de l'objet surface de couleur blanche à l'aide de la fonction
fill() de pygame. Créer les formes requises sont décrites ci-dessus. Mettre à jour l'objet Surface

Exemple 1: Dessiner un cercle à l'intérieur d'un rectangle.
"""
# # Impporting pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()
#
# # create the display surface object of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Using draw.rect module of pygame to draw the rectangle
# pygame.draw.rect(window, (0, 0, 255), [50, 200, 500, 200])
#
# # Using draw.rect module of pygame to draw the circle inside the rectangle
# pygame.draw.circle(window, (0, 255, 0), [300, 300], 100)
#
# # Draws the surface object to the screen.
# pygame.display.update()

"""
Exemple 2: Dessiner des rectangles les uns dans les autres.
"""

# # Importing pygame module
# import pygame
# from pygame.locals import *
#
# # initiate pygame and give permission to use pygame's functionality.
# pygame.init()
#
# # Create the display surface object of specific dimension.
# window = pygame.display.set_mode((600, 600))
#
# # Fill the screen with white color
# window.fill((255, 255, 255))
#
# # Creating a list of different rects
# rectangle_list = [pygame.Rect(50, 100, 500, 200),
#                   pygame.Rect(70, 120, 460, 160),
#                   pygame.Rect(90, 140, 420, 120),
#                   pygame.Rect(110, 160, 380, 80),
#                   pygame.Rect(130, 180, 340, 40)]
#
# # Creating list of different colors
# colors_list = [(0, 0, 0),
#                (255, 255, 255),
#                (0, 0, 255),
#                (0, 255, 0),
#                (255, 0, 0)
#                ]
#
# # Creating a variable which we will use
# # to iterate over the color_list
# color_var = 0
#
# # Iterating over the rectangle_list using
# # for loop
#
# for rectangle in rectangle_list:
#
#     # Drawing the rectangle
#     # Using the draw.rect() method
#     pygame.draw.rect(window, colors_list[color_var], rectangle)
#
#     # Increasing the value of color_var by 1 after every interaction
#     color_var += 1
#
# # Draws the surface object to the screen.
# pygame.display.update()

"""
Ecrire vos propres fonctions de dessin:
Vous pouvez facilement créez vos propres fonctions de dessin spécialsées dans pygame.

Cela peut être fait en suivant la procédure indiquée. Créez une fonction de dessin qui prendra la position de départ, la
largeur et la hauteur comme paramètres. Dessinez les formes requises sont décrites ci-dessus. Appelez la fonction draw()
"""
# Importing pygame module
import pygame
from pygame.locals import *


# Creating Drawing function

def drawingfunction(x, y, width, height):
    # Creating rectangle using the draw.rect() method
    pygame.draw.rect(window, (0, 0, 255), [x, y, width, height])

    # Calculation the center of the circle
    circle_x = width / 2 + x
    circle_y = height / 2 + y

    # Calculating the radius of the circle
    if height < width:
        radius = height / 2
    else:
        radius = width / 2

    # Drawing the circle
    pygame.draw.circle(window, (0, 255, 0), [circle_x, circle_y], radius)

# initiate pygame and give permission to use pygame's functionality.
pygame.init()

# Create the display surface object of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the screen with white color
window.fill((255, 255, 255))

# Calling the draw function
drawingfunction(50, 200, 500, 200)

# Draws the surface object to the screen.
pygame.display.update()



"""
Dessiner des formes avec la souris:
Voyons maintenant comment nous pouvons créer des formes chaque fois que l'utilisateur clique sur la souris. Nous allons
créer des cercles dans l'exemple suivant, mais vous pouvez créer n'importe quelle form.

Créer une liste pour stocker la position de la forme à dessiner. Créer une variable pour stocker la couleur de la forme.
Céer une variable que nous utiliserons pour exécuter la boucle while et créez une boucle while. Itérer sur tous les
événements recus de pygame.event.get(). Si le type de l'événement est quit, définissez la variable d'exécution sur false.
Si le type de lévénement est MOUSEBUTTONDOWN (cet événement se produit lorsqu'un utilisateur appuie sur le bouton de la
souris) alors obtenir la position actuelle dans une variable puis ajouter cette position dans notre liste 
circle_positions. Itérer sur toutes les positions dans le array créé à l'aide d'une boucle for. Continuez à dessiner la
forme. Mettez à jour l'objet de surface.
"""
# Importing pygame module
import pygame
from pygame.locals import *

# Inititate pygame and give permission
# to use pygame's functionality.
pygame.init()

# Create the display surface object of specific dimension
window = pygame.display.set_mode((600, 600))

# Fill the screen with white color
window.fill((255, 255, 255))

# creating list in which we will store
# the position of the circle
circle_positions = []

# radius of the circle
circle_radius = 60

# Color of the circle
color = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            circle_positions.append(position)

    # Using for loop to iterate
    # over the circle_positions
    # list
    for position in circle_positions:

        # Drawing the circle
        pygame.draw.circle(window, color, position, circle_radius)

    # Draws the surface object to the screen.
    pygame.display.update()

    # Draws the sufrface object to the screen.
    pygame.display.update()

# End the window
pygame.quit()

