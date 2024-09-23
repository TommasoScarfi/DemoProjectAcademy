import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)




pygame.init()
SCREEN_WIDHT, SCREN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREN_HEIGHT))
pygame.display.set_caption("Titolo Gioco")
icona = pygame.image.load("images/bulbasaur.jpg")
pygame.display.set_icon(icona)
sfondo_colore = (150, 200, 250)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    

    screen.fill(sfondo_colore)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()