import pygame

class Platforms(pygame.sprite.Sprite):
    # Classe que representa as plataformas do jogo

    def __init__(self, x_pos, y_pos, style, speed):
        """
        Inicializa os atributos das plataformas.

        Carrega a imagem da plataforma e define as posições iniciais.

        Argumentos:
            x_pos: Posição x inicial da rocha.
            y_pos: Posição y inicial da rocha.
            style: Caminho do arquivo de imagem da rocha.
            speed: Velocidade da rocha.
        """

        super().__init__()
        city_platform = pygame.image.load(style).convert_alpha()
        self.image = city_platform
        self.rect = self.image.get_rect(bottomleft=(x_pos, y_pos))
        self.speed = speed
    
    def destroy(self):
        """
        Método que destrói a plataforma se ela sair da tela.
        """

        if self.rect.x <= -300:
            self.kill()
    
    def movement(self):
        """
        Método que move a plataforma para a esquerda.
        """

        self.rect.x -= self.speed
    
    def update(self):
        """
        Atualiza a plataforma.

        Chama os métodos movement() e destroy() atualizar a plataforma.
        """

        self.movement()
        self.destroy()
    
# Cria o grupo para as plataformas
platforms = pygame.sprite.Group()