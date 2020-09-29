import pygame
import time
from lib.Logic.FpsTimer import FpsTimer
from Triangle import Triangle

pygame.init()

pygame.display.set_caption("Tetris")

screen_x = 700
screen_y = 700
screen = pygame.display.set_mode((screen_x, screen_y))
screen.fill((50, 50, 50))
pygame.display.update()

cntr = 0
running = True
fpsClock = FpsTimer(time.time(), 960)
tri = Triangle(pygame.Surface((screen_x,screen_y)),(screen_x / 2,5), 600)

while running:
    cntr += 1

    if cntr == 25000:
        running = False

    screen.blit(tri.surface, (0,0))
    pygame.display.update()

    tri.drawNext()

    # fpsClock.endFrame()
