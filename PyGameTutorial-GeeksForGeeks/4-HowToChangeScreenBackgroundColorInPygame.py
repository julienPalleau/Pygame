# https://www.geeksforgeeks.org/python/pygame-tutorial/
# https://www.geeksforgeeks.org/python/how-to-change-screen-background-color-in-pygame/

from rich import print

"""
Exemple 1: This example sets the screen background color to red.
"""
print("[bold red]How to change screen background color in Pygame?[/bold red]")
print("[bold green]Example1: This example sets the screen background color to red[/bold green]")
# Importing the library
import pygame

# Initialize Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# set title
pygame.display.set_caption('Red background color')

# Initializing RGB color
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame after closing window
pygame.quit()



"""
Exemple 2: This example sets the screen background color to blue.
"""
# Initializing surface
surface = pygame.display.set_mode((400, 300))

# set title
pygame.display.set_caption('Blue background color')

# Initializing RGB color
color = (0, 0, 255)

# Changing surface color
surface.fill(color)
pygame.display.flip()

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame after closing window
pygame.quit()