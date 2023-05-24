import pygame
import pandas as pd
from sys import exit
# from random import randint
from classes import Platforms, Ground, Rocks, Tree, platforms, ground, rocks, tree
from math import floor

pygame.init()

# Window size
WIDTH = 800
HEIGHT = 600

# Nome do jogador
nome_player = input("Digite o nome do jogador: ")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player sprites and scale
        player_1 = pygame.image.load('assets/kid/player1.png').convert_alpha()
        player_2 = pygame.image.load('assets/kid/player2.png').convert_alpha()
        
        # List containing player sprites for movement animation
        self.player_walk = [player_1, player_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100,501))
        
        # Load player jump sprite and scale
        # self.player_jump = pygame.image.load('assets/kid/player1.png').convert_alpha()
        
        self.gravity = 1
        self.speedy = 0
        self.jump_bool = False

    def isCollidingPlatform(self, platforms):
        # Checks if the player is colliding with a platform
        platforms_hit = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platforms_hit: 
            if self.rect.colliderect(platform.rect): 
                # Returns witch platform the player is colliding with
                return platform
        return False
    
    def isCollidingGround(self, ground):
        # Checks if the player is colliding with the ground
        for g in ground:
            if self.rect.colliderect(g.rect):
                return True
        return False
    
    def jump(self):
        # Verify if player press space and he's not jumping if both are true, jump
        if keys[pygame.K_SPACE] and self.jump_bool == False:
            self.speedy -= 20
            self.jump_bool = True
    
    def apply_gravity(self):
        # If Player is in the air and the space key is pressed, apply the glide effect.
        if keys[pygame.K_SPACE] and self.speedy >= 0:
            self.gravity = 0.1
        else:
            self.gravity = 1
            
        # Gravity effect
        self.speedy += self.gravity
        self.rect.y += self.speedy
        if self.isCollidingGround(ground):
            # Checks if the player is colliding with the ground
            for g in ground:
                if self.rect.bottom > g.rect.top + 1:
                    self.rect.bottom = g.rect.top + 1
                    self.jump_bool = False
                    self.speedy = 0 
            
        
        if self.isCollidingPlatform(platforms):
            platform = self.isCollidingPlatform(platforms)
            # Checks if the player is colliding with a platform and if he is, checks if he is falling or jumping
            if self.speedy > 0:
                # If player is falling, stop him from falling and set his position to the top of the platform
                self.rect.bottom = platform.rect.top + 1
                self.jump_bool = False
                self.speedy = 0
            elif self.speedy < 0:
                # If player is jumping, stop him from jumping and set his position to the bottom of the platform
                self.rect.top = platform.rect.bottom 
                self.speedy = 0
        
    
    def animation_state(self):
        # If player is not in the air, play the walking animation
        if self.speedy == 0:
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index % len(self.player_walk))]
        # else:
        #     self.image = self.player_jump
    
    def collision_player_rocks():
        # Checks if the player is colliding with a rock
        if pygame.sprite.spritecollide(player.sprite, rocks, False):
            # If player is colliding with a rock, clear the list of rocks and return False
            rocks.empty()
            return False
        else:
            return True
        
    def update(self):
        self.apply_gravity()
        self.jump()
        self.animation_state()

# Window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evolution Run")

clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Player Group
player = pygame.sprite.GroupSingle()
player.add(Player())

ground.add(Ground())

tree.add(Tree())

playing = True

# Pontuação
score = 0
save = True
score_text = font.render("Score: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(topright=(WIDTH - 660, 10))

while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Check if the player clicks the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    player_stand = pygame.image.load('assets/kid/player_stand.png').convert_alpha()
    player_stand_rect = player_stand.get_rect(midbottom = (100,501))
    tree_stand = pygame.image.load('assets/tree.png').convert_alpha()
    tree_stand = pygame.transform.scale(tree_stand, (150, 150))
    tree_stand_rect = tree_stand.get_rect(bottomleft = (0,500))
    start_text = font.render(f"Press SPACE to START", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 250))
    screen.fill((146, 244, 255))
    ground.draw(screen)
    screen.blit(tree_stand, tree_stand_rect)
    screen.blit(player_stand, player_stand_rect)
    screen.blit(start_text, start_text_rect)
    # Check if the player clicks the space key
    if keys[pygame.K_SPACE]:
        # If he does, start the game
        break

    pygame.display.update()
    clock.tick(60)

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 2000)

rocks_timer = pygame.USEREVENT + 2
pygame.time.set_timer(rocks_timer, 1800)

while True:
    # Read the scoreboard file
    scoreboard = pd.read_csv('scoreboard.csv')
    
    # Get a tuple with all the keys, if the key is pressed, the value is True, if not, False
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        # Check if the player clicks the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Platform and rock timers
        if event.type == platform_timer:
            platforms.add(Platforms())
        if event.type == rocks_timer:
            rocks.add(Rocks())

    # Check if the game is running
    if playing:
        # Draw the player, platforms, rocks and ground on the screen
        # Fill the background with a color
        screen.fill((146, 244, 255))
        # Place the score text on the screen
        screen.blit(score_text, score_rect)
        tree.draw(screen)
        tree.update()
        player.draw(screen)
        player.update()
        platforms.draw(screen)
        platforms.update()
        rocks.draw(screen)
        rocks.update()
        ground.draw(screen)
        # Check if the player collides with a rock, if he does, stop the game
        playing = Player.collision_player_rocks()
        save = True
        # Update the score
        score += 0.2
        score_text = font.render("Score: " + str(floor(score)), True, (255, 255, 255))
    # If the game is not running, show the game over screen
    else:
        # Clear all the sprites
        player.empty()
        rocks.empty()
        platforms.empty()
        
        # Fill the screen with a color
        screen.fill((94,129,162))
        
        # Show the game over text and the score
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        # Best Score
        best_score = scoreboard.loc[scoreboard['Name'] == nome_player, 'Score']
        your_best_score = font.render("Your Best Score: " + str(floor(best_score)), True, (255, 255, 255))
        best_score_rect = your_best_score.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(your_best_score, best_score_rect)

        # Overall Best Score
        overall_best_score = scoreboard['Score'].max()
        overall_best_score_text = font.render("Overall Best Score: " + str(floor(overall_best_score)), True, (255, 255, 255))
        overall_best_score_rect = overall_best_score_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 250))
        screen.blit(overall_best_score_text, overall_best_score_rect)
        
        # Save the best score in a csv
        if save:
            scoreboard = scoreboard.sort_values(by=['Score'], ascending=False)
            if nome_player not in scoreboard['Name'].values:
                scoreboard.loc[len(scoreboard)] = [nome_player, floor(score)]
            elif nome_player in scoreboard['Name'].values and score > scoreboard[scoreboard['Name'] == nome_player]['Score'].values[0]:
                scoreboard.loc[scoreboard['Name'] == nome_player, 'Score'] = floor(score)
                
            scoreboard.to_csv('scoreboard.csv', index=False)
            save = False

        # If the player press space, restart the game
        if keys[pygame.K_SPACE]:
            playing = True
            score = 0
            player.add(Player())
            ground.add(Ground())
            rocks.empty()
            platforms.empty()
    
    pygame.display.update()
    clock.tick(60)