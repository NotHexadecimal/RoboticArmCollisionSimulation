import pygame
import math
import random

width = 800
height = 800

class Braccio():
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.la = 200
        self.lb = 200
        self.w = 20
        self.center = (400, 400)
        self.t = []

    def update(self):
        self.b += 0.02
        if self.b > math.pi * 2:
            self.b = 0
            self.a += 0.02
        self.t = []
        self.t.append(rectVertex(self.center, self.la, self.w, self.w, self.w, self.a))
        self.t.append(rectVertex(circlepos(self.a, self.la - self.w, self.center), self.lb, self.w, self.w, self.w, self.b))

    def draw(self):
        pygame.draw.polygon(screen, (0, 0, 0), self.t[0])
        pygame.draw.circle(screen, (255, 0, 0), self.center, 3)
        c = circlepos(self.a, self.la - self.w, self.center)
        pygame.draw.polygon(screen, (0, 0, 0), self.t[1])
        pygame.draw.circle(screen, (255, 0, 0), (int(c[0]), int(c[1])), 3)

    def collisionChecker(self, obstacleList):
          for i in obstacleList:
              if trianglesCollision(i, (self.t[0][0], self.t[0][1], self.t[0][2])):
                  return True
          for i in obstacleList:
              if trianglesCollision(i, (self.t[0][0], self.t[0][3], self.t[0][2])):
                  return True
          for i in obstacleList:
              if trianglesCollision(i, (self.t[1][0], self.t[1][1], self.t[1][2])):
                  return True
          for i in obstacleList:
              if trianglesCollision(i, (self.t[1][0], self.t[1][3], self.t[1][2])):
                  return True
          return False

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

def trianglesCollision(t1, t2):
    for i in range(3):
        z = pointInTriangle(t1[i], t2[0], t2[1], t2[2])
        if z: return True
    for i in range(3):
        z = pointInTriangle(t2[i], t1[0], t1[1], t1[2])
        if z: return True
    return False

def circlepos(angle, radius, pos):
    x = math.cos(angle) * radius + pos[0]
    y = math.sin(angle) * radius + pos[1]
    return (x, y)

def rectVertex(point, la, lb, lc, ld, rot):
    a = circlepos(rot, la, point)
    b = circlepos(rot - math.pi, lc, point)
    return [circlepos(rot - math.pi / 2, lb, a), circlepos(rot - math.pi / 2, lb, b), circlepos(rot + math.pi / 2, ld, b), circlepos(rot + math.pi / 2, ld, a)]

pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('BraccioThatCollide')
clock = pygame.time.Clock()

obList = [((300, 330), (120, 230), (320, 190)), ((550, 550), (600, 600), (550, 600))]
braccio = Braccio()
col = False
render = False

done = False
try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if render:
            screen.fill((255, 0, 0) if col else (255, 255, 255))

        braccio.update()

        col = braccio.collisionChecker(obList)

        if render:
            braccio.draw()
            for i in obList:
                pygame.draw.polygon(screen, (0, 0, 0), i)

            pygame.display.update()
            clock.tick(30)

finally:
    pygame.quit()
