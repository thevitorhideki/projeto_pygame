import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_1 = pygame.image.load("""imagem 1 do personagem""").convert_alpha()
        player_2 = pygame.image.load("""imagem 2 do personagem""").convert_alpha()
        self.player = [player_1, player_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("""imagem do pulo""").convert_alpha()

        self.image = self.player[self.player_index]
        self.rect = self.image.get_rect(midbottom = ("""posição do personagem"""))
        self.gravity = 0
        self.keys = pygame.key.get_pressed()
    
    def jump(self):
        if self.keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    
    def apply_gravity(self):
        # Gliding
        if self.keys[pygame.K_SPACE] and self.rect.bottom < 300:
            self.gravity += 0.2
        # Falling
        else: 
            self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.jump()
        self.apply_gravity()
        self.animation_state()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bread and Fred")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

active = True

# Background
background = pygame.image.load('assets/bg.png').convert()
background2 = pygame.image.load('assets/bg2.jpg').convert()

background_rect = background.get_rect(topleft=(0, 0))
background2_rect = background2.get_rect(topleft=(background.get_width(), 0))

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background, background_rect)
    screen.blit(background2, background2_rect)

    if background2_rect.topright[0] == WIDTH:
        background_rect.x = WIDTH
    elif background_rect.topright[0] == WIDTH:
        background2_rect.x = WIDTH

    background_rect.x -= 4
    background2_rect.x -= 4

    if active:
        player.draw(screen)
        player.update()

    pygame.display.update()
    clock.tick(60)