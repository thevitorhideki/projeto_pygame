import pygame
from random import randint
from settings import WIDTH, HEIGHT

class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load('assets/platform.png').convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (WIDTH, randint(350,400)))

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
        self.rect = self.image.get_rect(bottomleft = (pos_x, 700))
    
    def movement(self):
        self.rect.x -= 4
        
    def replace(self):
        # Destroy ground if it goes off screen
        if self.rect.x <= -WIDTH:
            self.rect.x = WIDTH
    
    def update(self):
        self.movement()
        self.replace()

class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        rock = pygame.image.load('assets/rock.png').convert_alpha()
        self.image = rock
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (randint(WIDTH, WIDTH + 200), 620))
    
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
        self.rect = self.image.get_rect(bottomleft = (0,620))
    
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