import pygame

from settings import WIDTH

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
        
ground = pygame.sprite.Group()