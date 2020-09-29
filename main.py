import pygame
import time
from lib.Logic.FpsTimer import FpsTimer
from Triangle import Triangle

pygame.init()

pygame.display.set_caption("Triangle")

screen_x = 700
screen_y = screen_x

screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((50, 50, 50))
pygame.display.update()

cntr = 0
running = True
baseWidth = 600
tri = Triangle(pygame.Surface((screen_x,screen_y)),(screen_x / 2,(screen_x - baseWidth) / 2), baseWidth)

# fpsClock = FpsTimer(time.time(), 120) # Uncomment to slow down high performant system

while running:
    cntr += 1

    if cntr == 30000:
        running = False

    tri.drawNext()

    screen.blit(tri.surface, (0,0))
    pygame.display.update()

    # fpsClock.endFrame() # Uncomment to slow down high performant system
