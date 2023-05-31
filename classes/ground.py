import pygame
from settings import WIDTH

class Ground(pygame.sprite.Sprite):
    # Classe que representa o chão no jogo.

    def __init__(self, pos_x, sprite, speed):
        """
        Inicializa os atributos do chão.

        Carrega a imagem do chão e define as posições iniciais.

        Argumentos:
            pos_x: Posição x inicial do chão.
            sprite: Caminho do arquivo de imagem do chão.
            speed: Velocidade do chão.
        """

        super().__init__()
        ground = pygame.image.load(sprite).convert_alpha()
        self.image = ground
        self.rect = self.image.get_rect(bottomleft=(pos_x, 770))
        self.speed = speed
    
    def movement(self):
        """
        Método que move o chão para a esquerda.
        """

        self.rect.x -= self.speed
    
    def replace(self):
        """
        Repõe o chão quando ele sai da tela.
        """

        if self.rect.x <= -WIDTH + 10:
            self.rect.x = WIDTH
    
    def update(self):
        """
        Atualiza o chão.

        Chama os métodos movement() e replace() atualizar o chão.
        """

        self.movement()
        self.replace()
    
# Cria o grupo para o chão
ground = pygame.sprite.Group()