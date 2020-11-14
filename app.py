import math
import random

import pygame

# initialize game
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# game loop
running = True

while running:
    screen.fill((0, 0, 0))
    # Background Image
    # screen.blit(background, (0, 0))

    # Caption and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('./assets/ufo.png')
    pygame.display.set_icon(icon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
