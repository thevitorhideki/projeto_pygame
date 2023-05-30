import pygame

class Demon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.demon_list = [pygame.image.load(f'assets/demon/demon{i}.png').convert_alpha() for i in range(1, 9)]
        self.demon_index = 0
        self.image = self.demon_list[self.demon_index]
        self.rect = self.image.get_rect(bottomleft=(1280 * 3, 620))
    
    def animation(self):
        self.demon_index += 0.1
        self.image = self.demon_list[int(self.demon_index % len(self.demon_list))]
    
    def movement(self):
        self.rect.x -= 4

    def update(self):
        self.movement()
        self.animation()

demon = pygame.sprite.GroupSingle()