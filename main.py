import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bread and Fred")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

background = pygame.image.load('assets/bg.png').convert()
background2 = pygame.image.load('assets/bg2.jpg').convert()

background_rect = background.get_rect(topleft=(0, 0))
background2_rect = background2.get_rect(topleft=(background.get_width(), 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, background_rect)
    screen.blit(background2, background2_rect)

    if background2_rect.topright[0] == WIDTH:
        background_rect.x = WIDTH
    elif background_rect.topright[0] == WIDTH:
        background2_rect.x = WIDTH

    background_rect.x -= 4
    background2_rect.x -= 4

    pygame.display.update()
    clock.tick(60)
