import pygame

pygame.init()
ScreenWidth = 1000
ScreenHeight = 800
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range(ScreenHeight):
        for x in range(ScreenWidth):
            Screen.set_at((x, y), pygame.Color(0,
                                               int(y / ScreenHeight * 255), 255))
    pygame.display.update()
pygame.quit()