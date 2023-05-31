import pygame

class Portal(pygame.sprite.Sprite):
    # Classe que representa um portal no jogo.

    def __init__(self, speed):
        """
        Inicializa os atributos do portal.

        Carrega a imagem do portal, define sua posição inicial e define condições para a animação.

        Argumentos:
            speed: Velocidade do portal.
        """

        super().__init__()
        portal1 = pygame.image.load('assets/portal/portal1.png').convert_alpha()
        portal2 = pygame.image.load('assets/portal/portal2.png').convert_alpha()
        
        self.portal_anim = [portal1, portal2]
        self.portal_index = 0
        self.image = self.portal_anim[self.portal_index]
        self.rect = self.image.get_rect(bottomleft=(1280 * 3, 620))
        self.speed = speed
    
    def movement(self):
        """
        Método que move o portal para a esquerda.
        """

        self.rect.x -= self.speed

    def animation_state(self):
        """
        Método que define o estado da animação do portal.

        Aumenta o índice do sprite do jogador para animar o portal.
        """

        self.portal_index += 0.1
        self.image = self.portal_anim[int(self.portal_index % len(self.portal_anim))]

    def update(self):
        """
        Atualiza o portal.

        Chama os métodos animation_state() e movement() para atualizar o portal.
        """

        self.animation_state()
        self.movement()

# Cria o grupo para o portal
portal = pygame.sprite.GroupSingle()