import pygame
from pygame.locals import *

pygame.init()
Screen = pygame.display.set_mode((1000,800))


done = False
white = pygame.Color(255,255,255)
green = pygame.Color(0,255,0)
TimesClicked = 0

def PlotLineAlgorithm(p1, p2):
    if p2[0] < p1[0]:
        temp = p2
        p2 = p1
        p1 = temp
    x0 , y0 = p1
    x1 , y1 = p2
    magnitude = (y1 - y0)/ (x1 - x0)
    yIntercept = y0 - (magnitude * x0)
    for x in range(x0, x1):
        y = magnitude * x + yIntercept
        Screen.set_at((int(x), int(y)), white)

def BersenhamAlgorithm(p1, p2):
    x0 , y0 = p1
    x1 , y1 = p2
    dx = abs(x1 - x0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    dy = -abs(y1 - y0)
    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx + dy
    while True:
        Screen.set_at((x0, y0), white)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx;
        if e2 <= dx:
            err += dx
            y0 += sy;

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if TimesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            TimesClicked += 1
            if TimesClicked > 1:
                BersenhamAlgorithm(point1, point2)
                TimesClicked = 0
    pygame.display.update()
pygame.quit()


