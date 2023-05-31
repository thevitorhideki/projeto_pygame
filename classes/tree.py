import pygame

class Tree(pygame.sprite.Sprite):
    # Classe que representa uma árvore no jogo.

    def __init__(self, speed):
        """
        Inicializa os atributos da árvore.

        Carrega a imagem da árvore, ajusta seu tamanho e define a posição inicial.

        Argumentos:
            speed: Velocidade da árvore.
        """

        super().__init__()
        tree = pygame.image.load('assets/tree.png').convert_alpha()
        tree = pygame.transform.scale(tree, (150, 150))
        self.image = tree
        self.rect = self.image.get_rect(bottomleft=(0, 620))
        self.speed = speed
    
    def destroy(self):
        """
        Método que destrói a árvore se ela sair da tela.
        """

        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        """
        Método que move a árvore para a esquerda.
        """

        self.rect.x -= self.speed

    def update(self):
        """
        Atualiza a árvore.

        Chama os métodos movement() e destroy() atualizar a árvore.
        """

        self.movement()
        self.destroy()

# Cria o grupo para a árvore
tree = pygame.sprite.GroupSingle()
