# https://www.geeksforgeeks.org/python/pygame-tutorial/
# https://www.geeksforgeeks.org/python/how-to-get-the-size-of-pygame-window/

from rich import print

print("[bold red]Exemple 1:[/bold red]")

# import package pygame
import pygame

# initialize pygame
pygame.init()

# Form screen
screen = pygame.display.set_mode()

# get the default size
x, y = screen.get_size()

# quit pygame
pygame.display.quit()

# view size (width x height)
print(x, y)

print("\n[bold red]Exemple 2:[/bold red]")
# import package pygame
import pygame

# initialize pygame
pygame.init()

# Form screen
screen = pygame.display.set_mode((500, 500))

# get the size
x, y = screen.get_size()

# quit pygame
pygame.display.quit()

# view size (width x height)
print(x, y)