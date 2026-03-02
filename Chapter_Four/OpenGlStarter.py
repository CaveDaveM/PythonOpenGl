import pygame
from PyMesh import *
from pygame.locals import *
from OpenGL.GLU import *

pygame.init()
ScreenWidth = 500
ScreenHeight = 500
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight),DOUBLEBUF|OPENGL)

pygame.display.set_caption("OpenGL")
done = False
white = pygame.Color(255,255,255)
gluPerspective(60, (ScreenWidth/ ScreenHeight), 0.1, 100)
glTranslatef(0.0,0.0,-3)
mesh = Cube()
while not done:
    #the for loop is for click events such as button presses
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    mesh.draw()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()