import pygame

pygame.init()

pygame.mixer.music.load('Maroon 5 - Maps (Audio).mp3')
pygame.mixer.music.play()

recurso = input('Digite stop para parar:')

if recurso == str('stop'):
    pygame.mixer.music.stop()
