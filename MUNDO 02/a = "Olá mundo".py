import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("/home/Mylena/Downloads/ex21.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
