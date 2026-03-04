import pygame
from pygame.locals import *

pygame.init()
ScreenWidth, ScreenHeight = 800, 800
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

done = False
mouse_down = False
last_mouse_pos = (0, 0)
white = pygame.Color(255, 255, 255)
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down == True:
            pygame.draw.line(screen, white, last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()