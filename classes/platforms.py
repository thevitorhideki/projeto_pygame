import pygame

class Platforms(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, style):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load(style).convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))

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
        
platforms = pygame.sprite.Group()