import pygame
import pandas as pd
from math import floor
from sys import exit

from tree import Tree, tree
from ground import Ground, ground
from platforms import Platforms, platforms
from rocks import Rocks, rocks

from settings import WIDTH, HEIGHT

pygame.init()

# Nome do jogador
nome_player = ''

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
        self.rect = self.image.get_rect(midbottom = (100,620))
        
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
        
        if self.rect.bottom > 620:
            self.rect.bottom = 620
            self.speedy = 0
            self.jump_bool = False
        
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
            return True
        
    def update(self):
        self.apply_gravity()
        self.jump()
        self.animation_state()

# Window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Existential Crisis")

clock = pygame.time.Clock()
font_pixel = pygame.font.Font('font/Pixeltype.ttf', 50)
font_blox = pygame.font.Font('font/blox-brk.regular.ttf', 75)

# Player Group
player = pygame.sprite.GroupSingle()
player.add(Player())

tree.add(Tree())

ground.add(Ground(0))
ground.add(Ground(WIDTH))

game_state = {'playing': False, 'game_over': False, 'menu': False, 'player_name': True}

# Pontuação
score = 0
save = True
score_text = font_pixel.render("Score: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10, 10))


while game_state['player_name']:

    for event in pygame.event.get():
        print(event)
        # Check if the player clicks the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    
    
    background = pygame.image.load('assets/sky.png').convert_alpha()
    background_rect = background.get_rect(bottomleft=(0, 800))
    screen.blit(background, background_rect)
    
    ground.draw(screen)
    
    player_stand = pygame.image.load('assets/kid/player_stand.png').convert_alpha()
    player_stand_rect = player_stand.get_rect(midbottom = (100,620))
    screen.blit(player_stand, player_stand_rect)
    
    tree_stand = pygame.image.load('assets/tree.png').convert_alpha()
    tree_stand = pygame.transform.scale(tree_stand, (150, 150))
    tree_stand_rect = tree_stand.get_rect(bottomleft = (0,620))
    screen.blit(tree_stand, tree_stand_rect)
    
    start_text = font_pixel.render(f"Enter your name: {nome_player}", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(start_text, start_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enter_name = False
                game_state['player_name']=False
                game_state['menu']=True
            elif event.key == pygame.K_BACKSPACE:
                nome_player = nome_player[:-1]
            else:
                nome_player += event.unicode

        pygame.display.update()
        clock.tick(60)
    pygame.display.update()
    clock.tick(60)

while game_state['menu']:
    # Read the scoreboard file
    scoreboard = pd.read_csv('scoreboard.csv')
    
    # Get a tuple with all the keys, if the key is pressed, the value is True, if not, False
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        # Check if the player clicks the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    background = pygame.image.load('assets/sky.png').convert_alpha()
    background_rect = background.get_rect(bottomleft=(0, 800))
    screen.blit(background, background_rect)
    
    ground.draw(screen)
    
    player_stand = pygame.image.load('assets/kid/player_stand.png').convert_alpha()
    player_stand_rect = player_stand.get_rect(midbottom = (100,620))
    screen.blit(player_stand, player_stand_rect)
    
    tree_stand = pygame.image.load('assets/tree.png').convert_alpha()
    tree_stand = pygame.transform.scale(tree_stand, (150, 150))
    tree_stand_rect = tree_stand.get_rect(bottomleft = (0,620))
    screen.blit(tree_stand, tree_stand_rect)
    
    start_text = font_pixel.render(f"Press SPACE to START", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 320))
    screen.blit(start_text, start_text_rect)
    
    game_name = font_blox.render("EXISTENTIAL CRISIS", True, (255, 255, 255))
    game_name_rect = game_name.get_rect(center=((WIDTH / 2), HEIGHT / 2 - 250))
    screen.blit(game_name, game_name_rect)
    
    leaderboard_text = font_pixel.render(f"Leaderboard:", True, (255, 255, 255))
    leaderboard_rect = leaderboard_text.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 125))
    screen.blit(leaderboard_text, leaderboard_rect)
    
    for i in range(3):
        leaderboard = font_pixel.render(f"{i+1}: {scoreboard['Name'][i]} - {scoreboard['Score'][i]}pts", True, (255, 255, 255))
        leaderboard_rect = leaderboard.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 75 + i*50))
        screen.blit(leaderboard, leaderboard_rect)
    
    # Check if the player clicks the space key
    if keys[pygame.K_SPACE]:
        # If he does, start the game
        game_state['playing'] = True
        game_state['menu'] = False
    
    pygame.display.flip()
    clock.tick(60)

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 2400)

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
        if event.type == platform_timer and game_state['playing']:
            platforms.add(Platforms())
        if event.type == rocks_timer and game_state['playing']:
            rocks.add(Rocks())
    
    if game_state['playing']:
        save = True
        # Draw the background, score, tree, player, platforms, rocks and ground on the screen
        screen.blit(background, background_rect)
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
        ground.update()
    
        # Draw the game name on the screen only if it is on the screen
        if game_name_rect.right >= 0:
            screen.blit(game_name, game_name_rect)
        
        # Move the sky background and the game name to the left
        background_rect.x -= 1
        game_name_rect.x -= 1

        # Check if the player collides with a rock or the background ends, if he does, stop the game
        if Player.collision_player_rocks() or background_rect.right <= WIDTH:
            game_state['playing'] = False
            game_state['game_over'] = True
        
        # Update the score
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))
    # If the game is not running, show the game over screen
    if game_state['game_over']:
        # Clear all the sprites
        player.empty()
        rocks.empty()
        platforms.empty()
        ground.empty()
        
        # Fill the screen with a color
        screen.fill((94,129,162))
        background_rect.x = 0
        game_name_rect.center = (WIDTH / 2, HEIGHT / 2 - 250)
        
        # Save the best score in a csv
        if save:
            if nome_player not in scoreboard['Name'].values:
                scoreboard.loc[len(scoreboard)] = [nome_player, floor(score)]
            elif nome_player in scoreboard['Name'].values and score > scoreboard[scoreboard['Name'] == nome_player]['Score'].values[0]:
                scoreboard.loc[scoreboard['Name'] == nome_player, 'Score'] = floor(score)
            scoreboard = scoreboard.sort_values(by=['Score'], ascending=False)
                
            scoreboard.to_csv('scoreboard.csv', index=False)
            save = False
            
        # Show the game over text and the score
        game_over_text = font_pixel.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        # Best Score
        best_score = scoreboard.loc[scoreboard['Name'] == nome_player, 'Score']
        your_best_score = font_pixel.render("Your Best Score: " + str(floor(best_score)), True, (255, 255, 255))
        best_score_rect = your_best_score.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(your_best_score, best_score_rect)

        # Overall Best Score
        overall_best_score = scoreboard['Score'].max()
        overall_best_score_text = font_pixel.render("Overall Best Score: " + str(floor(overall_best_score)), True, (255, 255, 255))
        overall_best_score_rect = overall_best_score_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 250))
        screen.blit(overall_best_score_text, overall_best_score_rect)

        # If the player press space, restart the game
        if keys[pygame.K_SPACE]:
            game_state['playing'] = True
            game_state['game_over'] = False
            score = 0
            player.add(Player())
            ground.add(Ground(0))
            ground.add(Ground(WIDTH))
    
    pygame.display.flip()
    clock.tick(60)