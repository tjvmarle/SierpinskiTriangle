import math
import pygame
import random

class Triangle:

    def __init__(self, surface, top, width):
        self.clr = (255,255,255)
        self.clrs = ((255,0,0),(0,255,0),(0,0,255))
        self.surface = surface
        self.top = top
        self.width = width

        xLeft, _ = top
        xLeft -= width / 2 
        yLeft = math.sqrt(width * width - (width / 2) * (width / 2) )

        self.bLeft = (xLeft, yLeft)
        self.bRight = (xLeft + width, yLeft)

        pygame.draw.line(self.surface, self.clr, (self.top), (self.bRight))
        pygame.draw.line(self.surface, self.clr, (self.bLeft), (self.bRight))
        pygame.draw.line(self.surface, self.clr, (self.top), (self.bLeft))

        self.corners = (self.top, self.bLeft, self.bRight)
        self.pxl = random.choice(self.corners)

    def drawNext(self):
        curX, curY = self.pxl
        cornX, cornY = random.choice(self.corners)
        nextX = (curX + cornX) / 2
        nextY = (curY + cornY) / 2
        self.pxl = (nextX, nextY)
        pxlInt = (int(nextX), int(nextY))

        rgb = []
        for corner in self.corners:
            x, y = corner
            x_pos, y_pos = pxlInt
            color = int((1 - math.sqrt(abs(x - x_pos)**2 + abs(y - y_pos)**2) / self.width) * 255)
            rgb.append(color)

        self.surface.set_at(pxlInt, rgb) # Weighted RGB
        # pygame.draw.circle(self.surface, rgb, pxlInt, 1, 1) # Thicker dots weighted RGB

        # self.surface.set_at(pxlInt, random.choice(self.clrs)) # Random RGB

        # pygame.draw.circle(self.surface, random.choice(self.clrs), pxlInt, 1, 1) # Thicker dots