import pygame
pygame.init()


Screen = pygame.display.set_mode((1000, 800))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
XOriginOffSet = int(Screen.get_width()/2)
YOriginOffSet = int(Screen.get_height()/2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #this is for the x axis
    for x in range(-500,500):
        Screen.set_at((x + XOriginOffSet,YOriginOffSet),green)

    for y in range(-400,400):
        Screen.set_at((XOriginOffSet,y+YOriginOffSet),green)

    for x in range(-500,500):
        y = 10 * x - 100
        Screen.set_at((x + XOriginOffSet, y + YOriginOffSet),white)

    pygame.display.update()
pygame.quit()