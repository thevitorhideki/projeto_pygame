import pygame
from random import randint

WIDTH = 800

class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load('assets/platform.png').convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(center = (1000, randint(350,400)))

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
    def __init__(self, pos_x):
        super().__init__()
        ground = pygame.image.load('assets/ground.png').convert_alpha()
        self.image = ground
        self.rect = self.image.get_rect(bottomleft = (pos_x, 600))
    
    def movement(self):
        self.rect.x -= 4
        
    def destroy(self):
        # Destroy ground if it goes off screen
        if self.rect.x <= -WIDTH:
            self.kill()
    
    def update(self):
        self.movement()
        self.destroy()

class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rock = pygame.image.load('assets/rock.png').convert_alpha()
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

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        tree = pygame.image.load('assets/tree.png').convert_alpha()
        tree = pygame.transform.scale(tree, (150, 150))
        self.image = tree
        self.rect = self.image.get_rect(bottomleft = (0,500))
    
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
ground = pygame.sprite.Group()
rocks = pygame.sprite.Group()
tree = pygame.sprite.GroupSingle()