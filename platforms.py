import pygame
from random import randint

from settings import WIDTH

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load('assets/platform.png').convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))

    def destroy(self):
        # Destroy platform if it goes off screen
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        # Move platform to the left
        self.rect.x -= 4

    def update(self):
        self.movement()
        self.destroy()
        
platforms = pygame.sprite.Group()