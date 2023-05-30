import pygame

class Rocks(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, style):
        super().__init__()
        rock = pygame.image.load(style).convert_alpha()
        self.image = rock
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))
    
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
        
rocks = pygame.sprite.Group()
