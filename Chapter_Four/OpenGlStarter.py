import pygame
from PyMesh import *
from pygame.locals import *
from OpenGL.GL import *
pygame.init()
Screen = pygame.display.set_mode((500, 500),DOUBLEBUF|OPENGL)

pygame.display.set_caption("OpenGL")
done = False
mesh = Mesh3D()
while not done:
    #the for loop is for click events such as button presses
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    pygame.display.flip()
pygame.quit()