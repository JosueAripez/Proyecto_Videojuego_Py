import pygame, sys

pygame.init()
# Hola
# Hola comcklsdmvlksdm

size = (600,400)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()