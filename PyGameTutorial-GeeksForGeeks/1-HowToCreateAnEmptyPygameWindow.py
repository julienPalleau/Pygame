# https://www.geeksforgeeks.org/python/pygame-tutorial/
# https://www.geeksforgeeks.org/python/how-to-create-an-empty-pygame-window/

# import pygame package
import pygame

# Initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
pygame.display.set_mode((400, 500))

# Set title window
pygame.display.set_caption("HowToCreateAnEmptyPygameWindow")

# Creating a bool value which checks
# if game is running
running = True

# Keep game running till running is true
while running:

    # check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False
# Quit Pygame
pygame.quit()