import pygame
from Chapter_Four.PyMesh import *
from Object import *
from pygame.locals import *
from OpenGL.GLU import *
from Transform import *

pygame.init()
ScreenWidth = 1000
ScreenHeight = 1000
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), DOUBLEBUF | OPENGL)

pygame.display.set_caption("OpenGL")
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (ScreenWidth / ScreenHeight), 0.1, 100)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0, 1))
cube = Object("Cube")
cube.add_component(Transform((0,0,0)))
cube.add_component(Cube(GL_POLYGON, "../Models/CidnerBricks.tif"))

clock = pygame.time.Clock()
fps = 30;
while not done:
    #the for loop is for click events such as button presses
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    cube.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
