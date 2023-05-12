import pygame
from sys import exit

pygame.init()

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         player_1 = pygame.image.load("""imagem 1 do personagem""").convert_alpha()
#         player_2 = pygame.image.load("""imagem 2 do personagem""").convert_alpha()
#         self.player = [player_1, player_2]
#         self.player_index = 0
#         self.player_jump = pygame.image.load("""imagem do pulo""").convert_alpha()

#         self.image = self.player[self.player_index]
#         self.rect = self.image.get_rect(midbottom = ("""posição do personagem"""))
#         self.gravity = 0
#         self.keys = pygame.key.get_pressed()
#         self.frame_jump_counter = 0
#         self.jump_bool = False

#     def glide(self):
#         if self.jump_bool:
#             self.frame_jump_counter += 1
    
#     def jump(self):
#         if self.keys[pygame.K_SPACE] and self.rect.bottom >= 300:
#             self.gravity = -20
#             self.jump_bool = True
    
#     def apply_gravity(self):
#         # Gliding
#         if self.keys[pygame.K_SPACE] and self.frame_jump_counter > 20:
#             self.gravity = 2
#         # Falling
#         else: 
#             self.gravity += 1
#         self.rect.y += self.gravity
#         if self.rect.bottom >= 300:
#             self.rect.bottom = 300
#             self.jump_bool = False
#             self.frame_jump_counter = 0
    
#     def animation_state(self):
#         if self.rect.bottom < 300:
#             self.image = self.player_jump
#         else:
#             self.player_index += 0.1
#             if self.player_index > len(self.player_walk):
#                 self.player_index = 0
#             self.image = self.player_walk[int(self.player_index)]
    
#     def update(self):
#         self.jump()
#         self.apply_gravity()
#         self.animation_state()
#         self.glide()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pog Runner")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

playing = True

# Background
background = pygame.image.load('assets/bg.png').convert()
background2 = pygame.image.load('assets/bg2.jpg').convert()

background_rect = background.get_rect(topleft=(0, 0))
background2_rect = background2.get_rect(topleft=(background.get_width(), 0))

# Player
# player = pygame.sprite.GroupSingle()
# player.add(Player())

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

    # if playing:
    #     player.draw(screen)
    #     player.update()

    pygame.display.update()
    clock.tick(60)