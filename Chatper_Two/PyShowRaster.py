import pygame

pygame.init()
ScreenWidth = 800
ScreenHeight = 400
Screen = pygame.display.set_mode((ScreenWidth,ScreenHeight))

pygame.display.set_caption("Fantastic Something")
done = False

background
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True