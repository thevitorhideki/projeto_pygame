import pygame
from sys import exit
# from random import randint
from classes import Platforms, Ground, Rocks, platforms, ground, rocks

pygame.init()

# Window size
WIDTH = 800
HEIGHT = 600
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player sprites and scale
        player_1 = pygame.image.load('assets/cidade/player1.png').convert_alpha()
        player_2 = pygame.image.load('assets/cidade/player2.png').convert_alpha()
        
        # List containing player sprites for movement animation
        self.player_walk = [player_1, player_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100,501))
        
        # Load player jump sprite and scale
        # self.player_jump = pygame.image.load('assets/cidade/player1.png').convert_alpha()
        
        self.gravity = 1
        self.speedy = 0
        self.jump_bool = False

    def isCollidingPlatform(self, platforms):
        platforms_hit = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platforms_hit: 
            if self.rect.colliderect(platform.rect): 
                return platform
        return False
    
    def isCollidingGround(self, ground):
        for g in ground:
            if self.rect.colliderect(g.rect):
                return True
        return False
    
    def jump(self):
        # Verify if player press space and if it is, jump
        if keys[pygame.K_SPACE] and self.jump_bool == False:
            self.speedy -= 20
            self.jump_bool = True
    
    def apply_gravity(self):
        # If Player is jumping and the space key is pressed, apply gravity to the player.
        if keys[pygame.K_SPACE] and self.speedy >= 0:
            self.gravity = 0.1
        else:
            self.gravity = 1
        self.speedy += self.gravity
        self.rect.y += self.speedy
        if self.isCollidingGround(ground):
            for g in ground:
                if self.rect.bottom > g.rect.top + 1:
                    self.rect.bottom = g.rect.top + 1
                    self.jump_bool = False
                    self.speedy = 0 
            
        
        if self.isCollidingPlatform(platforms):
            platform = self.isCollidingPlatform(platforms)
            if self.speedy > 0:
                self.rect.bottom = platform.rect.top + 1
                self.jump_bool = False
                self.speedy = 0
                
            elif self.speedy < 0:
                self.rect.top = platform.rect.bottom 
                self.speedy = 0
        
    
    def animation_state(self):
        # If player is colliding with platform or ground, change sprite to walking animation
        if self.isCollidingPlatform(platforms) or self.isCollidingGround(ground):
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index % len(self.player_walk))]
        # else:
        #     self.image = self.player_jump
    
    def update(self):
        self.apply_gravity()
        self.jump()
        self.animation_state()


def collision_player_rocks():
    if pygame.sprite.spritecollide(player.sprite, rocks, False):
        rocks.empty()
        return False
    else:
        return True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Run")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

playing = True

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

ground.add(Ground())

rocks_list = []

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 2000)
rocks_timer = pygame.USEREVENT + 2
pygame.time.set_timer(rocks_timer, 1800)
clock = pygame.time.Clock()

# Pontuação
score = 0
score_text = font.render("Score: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(topright=(WIDTH - 660, 10))





while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == platform_timer:
            platforms.add(Platforms())
        if event.type == rocks_timer:
            rocks.add(Rocks())
    
    # Infinite background logic
    screen.fill((146, 244, 255))
    screen.blit(score_text, score_rect)

    # if background2_rect.topright[0] == WIDTH:
    #     background_rect.x = WIDTH
    # elif background_rect.topright[0] == WIDTH:
    #     background2_rect.x = WIDTH

    # background_rect.x -= 4
    # background2_rect.x -= 4

    if playing:
        player.draw(screen)
        player.update()
        platforms.draw(screen)
        platforms.update()
        rocks.draw(screen)
        rocks.update()
        ground.draw(screen)
        playing = collision_player_rocks()
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    else:
        platforms.empty()
        screen.fill((94,129,162))
        
        

    pygame.display.update()
    clock.tick(60)
    score+=1