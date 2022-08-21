"""
Playing Sounds
"""
import pygame
import time

# Setup for sounds. Default are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()


# Loading and playing a sound effect:
soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()

# Loading and playing background music:
# when you want to play an mp3 you have to:

# load the file
pygame.mixer.music.load('backgroundmusic.mp3')

# Invoke pygame.mixer.music.play() to start playback of the music stream. Finally, you have to wait for the file to play.
pygame.mixer.music.play()

# this line is mandatory to hear the music. Found this trick at: https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
pygame.event.wait()

# ...some more of your code goes here...
pygame.mixer.music.stop()

