"""
Playing Sounds
"""
import pygame.mixer
import time

pygame.init()

# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()

# Loading and playing background music:
pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play(-1, 0.0)

# ...some more of your code goes here...
pygame.mixer.music.stop()

