import pygame

class Demon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        demon = pygame.image.load('assets/demon.png').convert_alpha()

        self.image = demon
        self.rect = self.image.get_rect(bottomleft=(1280, 620))
    
    def movement(self):
        self.rect.x -= 4

    def update(self):
        self.movement()

demon = pygame.sprite.GroupSingle()