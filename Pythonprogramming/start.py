import pygame

''' Initializing pygame'''
pygame.init()


''' get the monitor size '''
def get_screen_size(offset):
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h - offset
    return width, height
