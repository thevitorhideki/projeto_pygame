import pygame
from sys import exit
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_1 = pygame.image.load('assets/cidade/player1.png').convert_alpha()
        player_1 = pygame.transform.scale(player_1, (96,96))
        player_2 = pygame.image.load('assets/cidade/player2.png').convert_alpha()
        player_2 = pygame.transform.scale(player_2, (96,96))
        self.player_walk = [player_1, player_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('assets/cidade/player1.png').convert_alpha()
        self.player_jump = pygame.transform.scale(self.player_jump, (96,96))

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100,500))
        self.gravity = 0
        self.frame_jump_counter = 0
        self.jump_bool = False

    def glide(self):
        if self.jump_bool:
            self.frame_jump_counter += 1
    
    def jump(self):
        if keys[pygame.K_SPACE] and self.rect.bottom >= 500:
            self.gravity = -20
            self.jump_bool = True
    
    def apply_gravity(self):
        # Gliding
        if keys[pygame.K_SPACE] and self.frame_jump_counter > 20:
            self.gravity = 2
        # Falling
        else: 
            self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.jump_bool = False
            self.frame_jump_counter = 0
    
    def animation_state(self):
        if self.rect.bottom < 500:
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
        self.glide()

class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        plataform = pygame.image.load('assets/cidade/plataforma.png').convert_alpha()
        self.image = plataform
        self.rect = self.image.get_rect(center = (900, randint(350,450)))

    def destroy(self):
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        self.rect.x -= 4

    def update(self):
        self.movement()
        self.destroy()

class Obstacles:
    def __init__(self):
        super().__init__()
        pass
    
    def update(self):
        pass

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Run")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

playing = True

# Background
background = pygame.image.load('assets/bg.png').convert()
background2 = pygame.image.load('assets/bg2.jpg').convert()

background_rect = background.get_rect(topleft=(0, 0))
background2_rect = background2.get_rect(topleft=(background.get_width(), 0))

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Plataforms
platforms = pygame.sprite.Group()

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 2000)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == platform_timer:
            platforms.add(Platforms())
    
    screen.blit(background, background_rect)
    screen.blit(background2, background2_rect)

    if background2_rect.topright[0] == WIDTH:
        background_rect.x = WIDTH
    elif background_rect.topright[0] == WIDTH:
        background2_rect.x = WIDTH

    background_rect.x -= 4
    background2_rect.x -= 4

    if playing:            
        player.draw(screen)
        player.update()
        platforms.draw(screen)
        platforms.update()
        player_platform_collision = pygame.sprite.spritecollide(player.sprite, platforms, False)
        if player_platform_collision:
            player.sprite.rect.bottom = player_platform_collision[0].rect.top

    pygame.display.update()
    clock.tick(60)