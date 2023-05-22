import pygame
from random import randint

class Rock(pygame.sprite.Sprite):
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