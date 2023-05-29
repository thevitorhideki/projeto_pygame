import pygame

class Fireman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        fireman = pygame.image.load('assets/fireman.png').convert_alpha()

        self.image = fireman
        self.rect = self.image.get_rect(bottomleft=(1280, 620))
    
    def movement(self):
        self.rect.x -= 4

    def update(self):
        self.movement()

fireman = pygame.sprite.GroupSingle()