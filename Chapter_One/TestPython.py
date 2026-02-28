import pygame
pygame.init()
ScreenWidth = 1000
ScreenHeight = 800
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

done = False
white = pygame.Color(255, 255, 255)

def to_pygame_coordinates(display, x, y):
    return x, display.get_height() - y

def draw_rect(x,y,size):
    pygame.draw.rect(screen, white, (x, y, size, size))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_rect(345,345,20)
    pygame.display.update()
pygame.quit()