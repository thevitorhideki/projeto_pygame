import pygame
from random import randint

from settings import WIDTH, HEIGHT

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

tree = pygame.sprite.GroupSingle()