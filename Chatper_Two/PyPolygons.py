import pygame
pygame.init()

ScreenWidth = 1000
ScreenHeight = 800
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))

done = False
white = pygame.Color(255,255,255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.polygon(Screen,white,((150,200),(600,400),(400,600)))
    pygame.display.update()
pygame.quit()