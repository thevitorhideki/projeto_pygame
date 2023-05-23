import pygame
from random import randint

WIDTH = 800

class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load('assets/cidade/platform.png').convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(center = (900, randint(350,400)))

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

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ground = pygame.image.load('assets/cidade/ground.png').convert_alpha()
        self.image = ground
        self.rect = self.image.get_rect(center = (WIDTH / 2, 550))

class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rock = pygame.image.load('assets/cidade/rock.png').convert_alpha()
        self.image = rock
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (randint(900, 1100), 500))
    
    def destroy(self):
        # Destroy platform if it goes off screen
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        # Move rock to the left
        self.rect.x -= 4

    def update(self):
        self.movement()
        self.destroy()

platforms = pygame.sprite.Group()
ground = pygame.sprite.GroupSingle()
rocks = pygame.sprite.Group()