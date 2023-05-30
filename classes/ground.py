import pygame
from settings import WIDTH

class Ground(pygame.sprite.Sprite):
    """
    Classe que representa o chão do jogo.
    """

    def __init__(self, pos_x, sprite, speed):
        """
        Construtor da classe Ground.

        Parameters:
        - pos_x (int): Posição x inicial do chão.
        - sprite (str): Caminho até o arquivo do chão.
        """
        super().__init__()
        ground = pygame.image.load(sprite).convert_alpha()
        # Load the ground image with transparency
        self.image = ground
        # Set the image of the ground
        self.rect = self.image.get_rect(bottomleft=(pos_x, 770))
        # Create a rect object for the ground with its initial position
        self.speed = speed
    
    def movement(self):
        """
        Move a plataforma horizontalmente
        """
        self.rect.x -= self.speed
        # Move the ground rect horizontally to the left by 4 pixels in each update
    
    def replace(self):
        """
        Repõe o chão quando ele sai da tela.
        """
        if self.rect.x <= -WIDTH:
            # Check if the ground has gone off the left side of the screen
            self.rect.x = WIDTH
            # Set the x-position of the ground back to the right side of the screen
    
    def update(self):
        """
        Atualiza o movimento do chão e o repõe se necessário.
        """
        self.movement()
        # Call the movement method to update the ground's position
        self.replace()
        # Call the replace method to check if the ground needs to be replaced
    
ground = pygame.sprite.Group()
# Create a sprite group for the ground
