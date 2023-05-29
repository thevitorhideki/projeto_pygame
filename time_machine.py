import pygame

class TimeMachine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        time_machine = pygame.image.load('assets/time_machine.png').convert_alpha()
        self.image = time_machine
        self.rect = self.image.get_rect(bottomleft=(1280*8, 620))
    
    def movement(self):
        self.rect.x -= 4

    def update(self):
        self.movement()

time_machine = pygame.sprite.GroupSingle()