import pygame

class Platforms(pygame.sprite.Sprite):
    """
    Classe que representa uma plataforma do jogo
    """

    def __init__(self, x_pos, y_pos, style):
        """
        Construtor da classe Plataforma

        Parâmetros:
        - x_pos (int): Posição x inicial da plataforma.
        - y_pos (int): Posição y inicial da plataforma.
        - style (str): Caminho até o arquivo do sprite de plataforma.
        """
        super().__init__()
        city_platform = pygame.image.load(style).convert_alpha()
        # Load the platform image with transparency
        self.image = city_platform
        # Set the image of the platform
        self.rect = self.image.get_rect(bottomleft=(x_pos, y_pos))
        # Create a rect object for the platform with its initial position
    
    def destroy(self):
        """
        Destrói a plataforma quando ela sai da tela.
        """
        if self.rect.x <= -300:
            # Check if the platform has gone off the left side of the screen
            self.kill()
            # Remove the platform from the sprite group
    
    def movement(self):
        """
        Move a plataforma horizontalmente.
        """
        self.rect.x -= 4
        # Move the platform rect horizontally to the left by 4 pixels in each update
    
    def update(self):
        """
        Atualiza o movimento da plataforma e a destrói se necessário.
        """
        self.movement()
        # Call the movement method to update the platform's position
        self.destroy()
        # Call the destroy method to check if the platform needs to be destroyed
    
platforms = pygame.sprite.Group()
# Create a sprite group for the platforms
