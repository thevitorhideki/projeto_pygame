import pygame

class Portal(pygame.sprite.Sprite):
    """Classe que representa um portal no jogo."""

    def __init__(self, speed):
        """
        Inicializa um objeto Portal.

        Carrega as imagens dos portais e define as propriedades iniciais.

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
        Move o portal para a esquerda.

        """
        self.rect.x -= self.speed

    def animation_state(self):
        """
        Atualiza o estado da animação do portal.

        """
        # Se o portal não estiver no ar, reproduz a animação de caminhar
        self.portal_index += 0.1
        self.image = self.portal_anim[int(self.portal_index % len(self.portal_anim))]

    def update(self):
        """
        Atualiza o portal.

        Atualiza o estado da animação e aplica o movimento.

        """
        self.animation_state()
        self.movement()

portal = pygame.sprite.GroupSingle()