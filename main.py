import random
import pygame
from pygame import mixer
import pandas as pd
from math import floor
from sys import exit

from tree import Tree, tree
from ground import Ground, ground
from platforms import Platforms, platforms
from rocks import Rocks, rocks
from portal import Portal, portal
from demon import Demon, demon

from settings import WIDTH, HEIGHT
from utils import save_score

pygame.init()

# Nome do jogador
player_name = ''

player_sprites = {
    'kid': ['assets/kid/player1.png', 'assets/kid/player2.png'],
    'man': ['assets/man/player1.png', 'assets/man/player2.png'],
    'oldman': ['assets/oldman/player1.png', 'assets/oldman/player2.png'],
    'skeleton': ['assets/skeleton/skeleton1.png', 'assets/skeleton/skeleton2.png'],
}

################# CLASS PLAYER #################

class Player(pygame.sprite.Sprite):
    def __init__(self, player_type):
        super().__init__()
        # Load player sprites and scale
        player_1 = pygame.image.load(player_type[0]).convert_alpha()
        player_2 = pygame.image.load(player_type[1]).convert_alpha()

        # List containing player sprites for movement animation
        self.player_walk = [player_1, player_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 620))

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
            self.image = self.player_walk[int(
                self.player_index % len(self.player_walk))]
        # else:
        #     self.image = self.player_jump

    def collision_player_rocks():
        # Checks if the player is colliding with a rock
        if pygame.sprite.spritecollide(player.sprite, rocks, False):
            pass
        
    def collision_player_portal():
        # Checks if the player is colliding with the portal
        if pygame.sprite.spritecollide(player.sprite, portal, False):
            return True
        
    def collision_player_demon():
        if pygame.sprite.spritecollide(player.sprite, demon, False):
            return True

    def update(self):
        self.apply_gravity()
        self.jump()
        self.animation_state()

################# SETTINGS #################

# Window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Existential Crisis")

clock = pygame.time.Clock()
font_pixel = pygame.font.Font('font/Pixeltype.ttf', 50)
font_blox = pygame.font.Font('font/blox-brk.regular.ttf', 75)

# Instantiate mixer
mixer.init()
# Load audio file
mixer.music.load('music/music.mp3')
# Set preferred volume
mixer.music.set_volume(0.4)
# Play with loop
mixer.music.play(-1)

next_track = True

# Player, tree and ground groups
player = pygame.sprite.GroupSingle()
player.add(Player(player_sprites['kid']))

tree.add(Tree())

ground_styles = {
    'kid': 'assets/morning/ground_morning.png',
    'man': 'assets/afternoon/ground_afternoon.png',
    'oldman': 'assets/night/ground_night.png',
    'hell': 'assets/hell/hell_ground.png',
}
ground.add(Ground(0, ground_styles['kid']))
ground.add(Ground(WIDTH, ground_styles['kid']))

portal.add(Portal())
demon.add(Demon())

game_state = {
    'playing_kid': False,
    'playing_man': False,
    'playing_oldman': False, 
    'hell': False,
    'game_over': False,
    'menu': False, 
    'player_name': True
}

background_styles = {
    'kid': 'assets/morning/sky_morning.png',
    'man': 'assets/afternoon/sky_afternoon.png',
    'oldman': ['assets/night/sky_night.png', 'assets/night/sky_night2.png'],
    'hell': 'assets/hell/hell_background.png',
}

# Pontuação
score = 0
score_text = font_pixel.render("Score: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10, 10))

# Timers
platform_timer = pygame.USEREVENT + 1
pygame.time.set_timer(platform_timer, 2400)

rocks_timer = pygame.USEREVENT + 2
pygame.time.set_timer(rocks_timer, 1800)

################# GAME LOOP #################

def transition(screen):
    fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for alpha in range(0, 255, 5):  # Decrease alpha value
        fade_surface.fill((0, 0, 0, alpha))  # Fill with black and alpha value
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)  # Delay for smoother effect
        
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
        if event.type == platform_timer and (game_state['playing_kid'] or game_state['playing_man'] or game_state['playing_oldman']):
            x_pos = random.randint(WIDTH, WIDTH + 200)
            y_pos = random.randint(300, 450)
            
            rocks.add(Rocks(x_pos, y_pos - 20))
            
            platforms.add(Platforms(WIDTH, y_pos))
            platforms.add(Platforms(WIDTH + 128, y_pos))
        if event.type == rocks_timer and (game_state['playing_kid'] or game_state['playing_man'] or game_state['playing_oldman']):
            rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200), 620))
            
        # Get the input from the player and save it in the variable player_name
        if event.type == pygame.KEYDOWN and game_state['player_name']:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # If the player doesn't type anything, the name will be qwerty + bug prevention
                if player_name == '':
                    player_name = 'qwerty'
                game_state['player_name'] = False
                game_state['menu'] = True
            elif event.key == pygame.K_BACKSPACE:
                # If the player press backspace, delete the last character from the player_name variable
                player_name = player_name[:-1]
            else:
                player_name += event.unicode

    if game_state['player_name']:
        # Draw the game name on the screen
        game_name = font_blox.render("EXISTENTIAL CRISIS", True, (255, 255, 255))
        game_name_rect = game_name.get_rect(center=((WIDTH / 2), HEIGHT / 2 - 250))
        screen.blit(game_name, game_name_rect)

        # Draw the background
        background = pygame.image.load(background_styles['kid']).convert_alpha()
        background_rect = background.get_rect(bottomleft=(0, 800))
        screen.blit(background, background_rect)
        
        background_2 = pygame.image.load(background_styles['kid']).convert_alpha()
        background_2_rect = background.get_rect(bottomleft=(background_rect.width, 800))

        # Load the player and tree images and draw them on the screen
        player_stand = pygame.image.load('assets/kid/player_stand.png').convert_alpha()
        player_stand_rect = player_stand.get_rect(midbottom=(100, 620))
        screen.blit(player_stand, player_stand_rect)

        tree_stand = pygame.image.load('assets/tree.png').convert_alpha()
        tree_stand = pygame.transform.scale(tree_stand, (150, 150))
        tree_stand_rect = tree_stand.get_rect(bottomleft=(0, 620))
        screen.blit(tree_stand, tree_stand_rect)

        # Draw the ground
        ground.draw(screen)
        
        # Draw the text box
        name_text = font_pixel.render(f"Enter your name: {player_name}", True, (255, 255, 255))
        name_text_rect = name_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(name_text, name_text_rect)

    elif game_state['menu']:
        # Clear the rocks and platforms groups to avoid bugs
        rocks.empty()
        platforms.empty()

        # Draw the stuff on the screen
        screen.blit(background, background_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(tree_stand, tree_stand_rect)
        screen.blit(game_name, game_name_rect)
        ground.draw(screen)

        # Draw the start text on the screen
        start_text = font_pixel.render(f"Press SPACE to START", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 320))
        screen.blit(start_text, start_text_rect)

        # Draw the leaderboard on the screen
        leaderboard_text = font_pixel.render(f"Leaderboard:", True, (255, 255, 255))
        leaderboard_rect = leaderboard_text.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 125))
        screen.blit(leaderboard_text, leaderboard_rect)

        # Logic to get the top 3 scores their names to draw on the screen
        for i in range(3):
            leaderboard = font_pixel.render(
                f"{i+1}: {scoreboard['Name'][i]} - {scoreboard['Score'][i]}pts", True, (255, 255, 255))
            leaderboard_rect = leaderboard.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 75 + i*50))
            screen.blit(leaderboard, leaderboard_rect)

        # Check if the player clicks the space key
        if keys[pygame.K_SPACE]:
            # If he does, start the game
            game_state['playing_kid'] = True
            game_state['menu'] = False

    elif game_state['playing_kid']:
        # Draw the background, score, tree, player, platforms, rocks and ground on the screen
        screen.blit(background, background_rect)
        screen.blit(background_2, background_2_rect)
        screen.blit(score_text, score_rect)
        tree.draw(screen)
        tree.update()
        # Draw the game name on the screen only if it is on the screen
        if game_name_rect.right >= 0:
            screen.blit(game_name, game_name_rect)
        player.draw(screen)
        player.update()
        rocks.draw(screen)
        rocks.update()
        platforms.draw(screen)
        platforms.update()
        ground.draw(screen)
        ground.update()
        portal.draw(screen)
        portal.update()

        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        # Move the sky background and the game name to the left
        background_rect.x -= 1
        background_2_rect.x -= 1
        game_name_rect.x -= 1
        
        # Check if the player collides with a rock or the background ends, if he does, stop the game
        if Player.collision_player_rocks():
            game_state['playing_kid'] = False
            game_state['game_over'] = True
        
        if Player.collision_player_portal():
            transition(screen)
            game_state['playing_kid'] = False
            game_state['playing_man'] = True
            background_rect = background.get_rect(bottomleft=(0, 800))
            background = pygame.image.load(background_styles['man']).convert_alpha()
            background_2 = pygame.image.load(background_styles['man']).convert_alpha()
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            player.add(Player(player_sprites['man']))
            ground.add(Ground(0, ground_styles['man']))
            ground.add(Ground(WIDTH, ground_styles['man']))
            portal.add(Portal())

        # Update the score
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))
    # If the game is not running, show the game over screen

    elif game_state['playing_man']:
        screen.blit(background, background_rect)
        screen.blit(background_2, background_2_rect)
        screen.blit(score_text, score_rect)

        player.draw(screen)
        player.update()
        rocks.draw(screen)
        rocks.update()
        platforms.draw(screen)
        platforms.update()
        ground.draw(screen)
        ground.update()
        portal.draw(screen)
        portal.update()

        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        background_rect.x -= 1
        background_2_rect.x -= 1

        if Player.collision_player_rocks():
            game_state['playing_man'] = False
            game_state['game_over'] = True

        if Player.collision_player_portal():
            transition(screen)
            game_state['playing_man'] = False
            game_state['playing_oldman'] = True
            background_rect = background.get_rect(bottomleft=(0, 800))
            background = pygame.image.load(background_styles['oldman'][0]).convert_alpha()
            background_2 = pygame.image.load(background_styles['oldman'][1]).convert_alpha()
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            player.add(Player(player_sprites['oldman']))
            ground.add(Ground(0, ground_styles['oldman']))
            ground.add(Ground(WIDTH, ground_styles['oldman']))

        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))


    elif game_state['playing_oldman']:
        screen.blit(background, background_rect)
        screen.blit(background_2, background_2_rect)
        screen.blit(score_text, score_rect)

        player.draw(screen)
        player.update()
        rocks.draw(screen)
        rocks.update()
        platforms.draw(screen)
        platforms.update()
        ground.draw(screen)
        ground.update()
        demon.draw(screen)
        demon.update()

        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        background_rect.x -= 1
        background_2_rect.x -= 1

        if Player.collision_player_rocks():
            game_state['playing_oldman'] = False
            game_state['game_over'] = True

        if Player.collision_player_demon():
            transition(screen)
            game_state['playing_oldman'] = False
            game_state['hell'] = True
            
            background_rect = background.get_rect(bottomleft=(0, 800))
            background = pygame.image.load(background_styles['hell']).convert_alpha()
            background_2 = pygame.image.load(background_styles['hell']).convert_alpha()
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            player.add(Player(player_sprites['skeleton']))
            ground.add(Ground(0, ground_styles['hell']))
            ground.add(Ground(WIDTH, ground_styles['hell']))

        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))

    elif game_state['hell']:
        if next_track:
            mixer.music.load('music/music_hell.mp3')
            mixer.music.play()
            next_track = False
        
        screen.blit(background, background_rect)
        screen.blit(background_2, background_2_rect)
        
        screen.blit(score_text, score_rect)

        player.draw(screen)
        player.update()
        rocks.draw(screen)
        rocks.update()
        platforms.draw(screen)
        platforms.update()
        ground.draw(screen)
        ground.update()

        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH
            
        background_rect.x -= 1
        background_2_rect.x -= 1

        if Player.collision_player_rocks():
            game_state['hell'] = False
            game_state['game_over'] = True

        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))

    elif game_state['game_over']:
        # Clear all the sprites
        player.empty()
        rocks.empty()
        platforms.empty()
        ground.empty()
        portal.empty()
        demon.empty()

        # Fill the screen with a color
        screen.fill((94, 129, 162))
        background_rect.x = 0
        game_name_rect.center = (WIDTH / 2, HEIGHT / 2 - 250)

        # Save the best score in a csv
        save_score(player_name, score, scoreboard)

        # Show the game over text and the score
        game_over_text = font_pixel.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        # Best Score
        best_score = scoreboard.loc[scoreboard['Name'] == player_name, 'Score']
        your_best_score = font_pixel.render("Your Best Score: " + str(floor(best_score)), True, (255, 255, 255))
        best_score_rect = your_best_score.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(your_best_score, best_score_rect)

        # Overall Best Score
        overall_best_score = scoreboard['Score'].max()
        overall_best_score_text = font_pixel.render(
            "Overall Best Score: " + str(floor(overall_best_score)), True, (255, 255, 255))
        overall_best_score_rect = overall_best_score_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 250))
        screen.blit(overall_best_score_text, overall_best_score_rect)

        # If the player press space, restart the game
        if keys[pygame.K_SPACE]:
            game_state['playing_kid'] = True
            game_state['game_over'] = False
            score = 0
            player.add(Player(player_sprites['kid']))
            ground.add(Ground(0))
            ground.add(Ground(WIDTH))
            portal.add(Portal())
            demon.add(Demon())


    pygame.display.flip()
    clock.tick(60)
