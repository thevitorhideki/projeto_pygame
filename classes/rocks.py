import pygame

class Rocks(pygame.sprite.Sprite):
    # Classe que representa as pedras no jogo.

    def __init__(self, x_pos, y_pos, style, speed):
        """
        Inicializa os atributos das pedras.

        Carrega a imagem da rocha e define as posições iniciais.

        Argumentos:
            x_pos: Posição x inicial da rocha.
            y_pos: Posição y inicial da rocha.
            style: Caminho do arquivo de imagem da rocha.
            speed: Velocidade da rocha.
        """

        super().__init__()
        rock = pygame.image.load(style).convert_alpha()
        self.image = rock
        self.rect = self.image.get_rect(bottomleft=(x_pos, y_pos))
        self.speed = speed
    
    def destroy(self):
        """
        Método que destrói a pedra se ela sair da tela.
        """

        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        """
        Método que move a pedra para a esquerda.
        """

        self.rect.x -= self.speed

    def update(self):
        """
        Atualiza a pedra.

        Chama os métodos movement() e destroy() atualizar a pedra.
        """

        self.movement()
        self.destroy()
        
# Cria o grupo para as pedras
rocks = pygame.sprite.Group()