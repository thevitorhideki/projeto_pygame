import pygame

class Demon(pygame.sprite.Sprite):
    # Classe que representa o demônio no jogo.

    def __init__(self, speed):
        """
        Inicializa os atributos do demônio.

        Carrega a imagem do demônio e define a posição inicial.

        Argumentos:
            speed: Velocidade do demônio.
        """

        super().__init__()

        # Carrega imagens do demônio e coloca em uma lista
        self.demon_list = [pygame.image.load(f'assets/demon/demon{i}.png').convert_alpha() for i in range(1, 9)]
        self.demon_index = 0
        self.image = self.demon_list[self.demon_index]
        self.rect = self.image.get_rect(bottomleft=(1280 * 3, 620))
        self.speed = speed

    def animation(self):
        """
        Método que define o estado da animação do demônio.

        Aumenta o índice do sprite do demônio para animar o demônio.
        """

        self.demon_index += 0.1
        self.image = self.demon_list[int(self.demon_index % len(self.demon_list))]

    def movement(self):
        """
        Método que move o demônio para a esquerda.
        """

        self.rect.x -= self.speed

    def update(self):
        """
        Atualiza o demônio.

        Chama os métodos movement() e animation() para atualizar o demônio.
        """

        self.movement()
        self.animation()

# Cria o grupo para o demônio
demon = pygame.sprite.GroupSingle()