import pygame
import math
import random

width = 800
height = 800

class Braccio():
    def __init__(self):
        a = 0
        b = 0
        la = 200
        lb = 200
        w = 20
    def draw(self):
        pass
    def __str__(self):
        return 'Perchè cazzo stai cercando di convertire un braccio in una stringa?!?'

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#Codice copiato spudoratamente da StackOverflow
def sign(p1, p2, p3):
  return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def pointInAABB(pt, c1, c2):
  return c2[0] <= pt[0] <= c1[0] and c2[1] <= pt[1] <= c1[1]

def pointInTriangle(pt, v1, v2, v3):
  b1 = sign(pt, v1, v2) <= 0
  b2 = sign(pt, v2, v3) <= 0
  b3 = sign(pt, v3, v1) <= 0

  return ((b1 == b2) and (b2 == b3)) and pointInAABB(pt, tuple(map(max, v1, v2, v3)), tuple(map(min, v1, v2, v3)))
#Fine codice copiato spudoratamente da StackOverflow

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BraccioThatCollide')
clock = pygame.time.Clock()

triangle = [[50, 75], [100, 25], [110, 100]]
a = False

done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255, 255, 255))

        pygame.draw.polygon(screen, (255, 0, 0) if a else (0, 0, 0), triangle)

        a = pointInTriangle(pygame.mouse.get_pos(), triangle[0], triangle[1], triangle[2])

        pygame.display.update()
        clock.tick(60)
finally:
    pygame.quit()