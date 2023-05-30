import pygame

class Rocks(pygame.sprite.Sprite):
    """Classe que representa as rochas no jogo."""

    def __init__(self, x_pos, y_pos, style):
        """
        Inicializa um objeto Rock.

        Carrega a imagem da rocha e define as posições iniciais.

        Args:
            x_pos (int): Posição x inicial da rocha.
            y_pos (int): Posição y inicial da rocha.
            style (str): Caminho do arquivo de imagem da rocha.

        """
        super().__init__()
        rock = pygame.image.load(style).convert_alpha()
        self.image = rock
        
        # Posiciona a rocha na parte inferior esquerda com as coordenadas fornecidas
        self.rect = self.image.get_rect(bottomleft=(x_pos, y_pos))
    
    def destroy(self):
        """
        Destroi a rocha se ela sair da tela.

        """
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        """
        Move a rocha para a esquerda.

        """
        self.rect.x -= 4

    def update(self):
        """
        Atualiza a rocha.

        Aplica o movimento da rocha e verifica se precisa ser destruída.

        """
        self.movement()
        self.destroy()
        
rocks = pygame.sprite.Group()