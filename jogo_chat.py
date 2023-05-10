import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Tiro")
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Classe para representar a nave espacial do jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem = pygame.image.load("nave.png")
        self.rect = self.imagem.get_rect()
        self.rect.centerx = largura_tela // 2
        self.rect.bottom = altura_tela - 10
        self.velocidade = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        # Mantém a nave dentro dos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > largura_tela:
            self.rect.right = largura_tela

    def atirar(self):
        projetil = Projetil(self.rect.centerx, self.rect.top)
        all_sprites.add(projetil)
        projeteis.add(projetil)

# Classe para representar os inimigos
class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem = pygame.image.load("inimigo.png")
        self.rect = self.imagem.get_rect()
        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidade = random.randint(1, 3)

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura_tela + 10:
            self.rect.x = random.randint(0, largura_tela - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidade = random.randint(1, 3)

# Classe para representar os projéteis
class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagem = pygame.image.load("projetil.png")
        self.rect = self.imagem.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.velocidade = -5

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.bottom < 0:
            self.kill()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
projeteis = pygame.sprite.Group()

# Criação do jogador
jogador = Jogador()
all_sprites.add(jogador)

# Criação dos inimigos
for _ in range(10):
    inimigo = Inimigo()
    all_sprites.add(inimigo)
    inimigos.add(inimigo)

# Loop principal do jogo
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogador.atirar()

# Atualizações dos sprites
all_sprites.update()

# Verifica colisões entre projéteis e inimigos
hits = pygame.sprite.groupcollide(projeteis, inimigos, True, True)
for hit in hits:
    inimigo = Inimigo()
    all_sprites.add(inimigo)
    inimigos.add(inimigo)

# Verifica colisões entre jogador e inimigos
if pygame.sprite.spritecollide(jogador, inimigos, False):
    running = False

# Renderização na tela
tela.fill(BRANCO)
all_sprites.draw(tela)
pygame.display.flip()
clock.tick(60)  # Limita a taxa de atualização para 60 FPS

