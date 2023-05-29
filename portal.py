import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        portal1 = pygame.image.load('assets/portal/portal1.png').convert_alpha()
        portal2 = pygame.image.load('assets/portal/portal2.png').convert_alpha()
        
        self.portal_anim = [portal1, portal2]
        self.portal_index = 0
        self.image = self.portal_anim[self.portal_index]
        self.rect = self.image.get_rect(bottomleft=(1280*8, 620))
    
    def movement(self):
        self.rect.x -= 4

    def animation_state(self):
        # If player is not in the air, play the walking animation
        self.portal_index += 0.1
        self.image = self.portal_anim[int(self.portal_index % len(self.portal_anim))]

    def update(self):
        self.animation_state()
        self.movement()

portal = pygame.sprite.GroupSingle()