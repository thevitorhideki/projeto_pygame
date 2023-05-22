import pygame
from sys import exit
from random import randint
from classes import Rock

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
        
        self.gravity = 0
        self.frame_jump_counter = 0
        self.jump_bool = False

    def isCollidingPlatform(self, platforms):
        for platform in platforms: 
            if self.rect.colliderect(platform.rect):
                return True
        return False
    
    def isCollidingGround(self, ground):
        for g in ground:
            if self.rect.colliderect(g.rect):
                return True
        return False

    def glide(self):
        # Verify if player is jumping and if it is, count the frames
        if self.jump_bool:
            self.frame_jump_counter += 1
    
    def jump(self):
        # Verify if player press space and if it is, jump
        if keys[pygame.K_SPACE] and (self.isCollidingPlatform(platforms) or self.isCollidingGround(ground)):
            self.gravity = -20
            self.jump_bool = True
    
    def apply_gravity(self):
        # If player is gliding, apply gravity of 2
        if keys[pygame.K_SPACE] and self.frame_jump_counter > 20:
            self.gravity = 2
        # If player is jumping, add 1 to gravity every frame
        else: 
            self.gravity += 1
            
        self.rect.y += self.gravity
        if self.isCollidingPlatform(platforms):
            for platform in platforms:
                if self.rect.bottom >= platform.rect.top + 1:
                    self.rect.bottom = platform.rect.top + 1 
                    self.gravity = 0
                    self.jump_bool = False
                    self.frame_jump_counter = 0
        elif self.isCollidingGround(ground):
            for g in ground:
                if self.rect.bottom > g.rect.top + 1:
                    self.rect.bottom = g.rect.top + 1 
                    self.gravity = 0
                    self.jump_bool = False
                    self.frame_jump_counter = 0
    
    def animation_state(self):
        # If player is colliding with platform or ground, change sprite to walking animation
        if self.isCollidingPlatform(platforms) or self.isCollidingGround(ground):
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index % len(self.player_walk))]
        # else:
        #     self.image = self.player_jump
    
    def update(self):
        self.jump()
        self.apply_gravity()
        self.animation_state()
        self.glide()

class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load platform sprite
        city_platform = pygame.image.load('assets/cidade/platform.png').convert_alpha()
        self.image = city_platform
        
        # Positioning the platform sprite on a random y axis
        self.rect = self.image.get_rect(center = (900, randint(350,400)))

    def destroy(self):
        # Destroy platform if it goes off screen
        if self.rect.x <= -300:
            self.kill()

    def movement(self):
        # Move platform to the left
        self.rect.x -= 4

    def update(self):
        self.movement()
        self.destroy()
    
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ground = pygame.image.load('assets/cidade/ground.png').convert_alpha()
        self.image = ground
        self.rect = self.image.get_rect(center = (WIDTH/2, 550))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Run")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

playing = True

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Plataforms
platforms = pygame.sprite.Group()

# Rock
rocks = pygame.sprite.Group()

# Ground
ground = pygame.sprite.GroupSingle()
ground.add(Ground())

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 4000)
rock_timer = pygame.USEREVENT + 2
pygame.time.set_timer(rock_timer, 1800)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == platform_timer:
            platforms.add(Platforms())
        if event.type == rock_timer:
            rocks.add(Rock())
    
    # Infinite background logic
    screen.fill((146, 244, 255))

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
        

    pygame.display.update()
    clock.tick(60)