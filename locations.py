import pygame
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

SCREEN_WIDHT, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    
    
    screen.fill((225, 225, 225))
    pygame.draw.circle(screen, (0,0,0), (SCREEN_WIDHT/2,SCREEN_HEIGHT/2), 300, 3)
    pygame.draw.circle(screen, (0,0,0), (SCREEN_WIDHT/2-100,SCREEN_HEIGHT/2-100), 30,3)
    pygame.draw.circle(screen, (0,0,0), (SCREEN_WIDHT/2-100,SCREEN_HEIGHT/2-100), 6)
    pygame.draw.ellipse(screen, (0,0,0), (SCREEN_WIDHT/4, SCREEN_HEIGHT/2-100-20, 90, 120), 3)
    pygame.draw.ellipse(screen, (0,0,0), (SCREEN_WIDHT/4*3-85, SCREEN_HEIGHT/2-100-20, 90, 120), 3)
    pygame.draw.circle(screen, (0,0,0), (SCREEN_WIDHT/2+100,SCREEN_HEIGHT/2-100), 30,3)
    pygame.draw.circle(screen, (0,0,0), (SCREEN_WIDHT/2+100,SCREEN_HEIGHT/2-100), 6)
    pygame.draw.rect(screen, (0,0,0), (540, 460, 200, 35))
    pygame.draw.polygon(screen, (0,0,0), [(SCREEN_WIDHT/2, SCREEN_HEIGHT/2-60), (600,SCREEN_HEIGHT/2+20), (680,SCREEN_HEIGHT/2+20) ])
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()