import pygame

class Tree(pygame.sprite.Sprite):
    """Classe que representa uma árvore no jogo."""

    def __init__(self):
        """
        Inicializa um objeto Tree.

        Carrega a imagem da árvore, ajusta seu tamanho e define a posição inicial.

        """
        super().__init__()
        tree = pygame.image.load('assets/tree.png').convert_alpha()
        tree = pygame.transform.scale(tree, (150, 150))
        self.image = tree
        self.rect = self.image.get_rect(bottomleft=(0, 620))
    
    def destroy(self):
        """
        Destroi a árvore se ela sair da tela.

        """
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        """
        Move a árvore para a esquerda.

        """
        self.rect.x -= 4

    def update(self):
        """
        Atualiza a árvore.

        Aplica o movimento da árvore e verifica se precisa ser destruída.

        """
        self.movement()
        self.destroy()

tree = pygame.sprite.GroupSingle()
