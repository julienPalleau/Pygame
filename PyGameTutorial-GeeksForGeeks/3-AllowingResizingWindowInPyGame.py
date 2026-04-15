# https://www.geeksforgeeks.org/python/pygame-tutorial/
# https://www.geeksforgeeks.org/python/allowing-resizing-window-in-pygame/

# import package pygame
import pygame
from rich import print

"""
Normal Pygame Window
"""
print("[bold red]Allowing resizing window in PyGame[/bold red]")
print("\n[bold green]Normal PyGame Window[/bold green]")
# Form screen with 400x400 size
# with not resizable
screen = pygame.display.set_mode((400, 400))

# set title
pygame.display.set_caption('Not resizable')

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame after closing window
pygame.quit()


"""
Resizable Pygame Window
"""
print("\n[bold green]Resizable PyGame Window[/bold green]")
# import package pygame
import pygame

# Form screen with 400x400 size
# and with resizable
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)

# set title
pygame.display.set_caption('Resizable')

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame after closing window
pygame.quit()