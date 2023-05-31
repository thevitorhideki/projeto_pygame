import random
import pygame
from pygame import mixer
import pandas as pd
from math import floor
from sys import exit

from classes.tree import Tree, tree
from classes.ground import Ground, ground
from classes.platforms import platforms
from classes.rocks import rocks
from classes.portal import Portal, portal
from classes.demon import Demon, demon

from settings import WIDTH, HEIGHT
from utils.structure_1 import structure_1
from utils.structure_2 import structure_2
from utils.structure_3 import structure_3
from utils.write_csv import save_score

pygame.init()

# Variável para armazenar o nome do jogador
player_name = ''

# Dicionário com assets diferentes para o jogador dependendo da fase
player_sprites = {
    'kid': ['assets/kid/player1.png', 'assets/kid/player2.png'],
    'man': ['assets/man/player1.png', 'assets/man/player2.png'],
    'oldman': ['assets/oldman/player1.png', 'assets/oldman/player2.png'],
    'skeleton': ['assets/skeleton/skeleton1.png', 'assets/skeleton/skeleton2.png'],
}

################# CLASSE JOGADOR #################

class Player(pygame.sprite.Sprite):
    # Classe que representa o jogador.
    
    def __init__(self, player_type):
        """
        Inicializa os atributos do jogador.

        Carrega os sprites do jogador, define condições para a animação, posiciona o jogador e
        inicializa os atributos de gravidade, velocidade vertical e pulo.

        Argumentos:
            player_type: Lista contendo assets diferentes do jogador para cada fase do jogo.
        """

        super().__init__()
        player_1 = pygame.image.load(player_type[0]).convert_alpha()
        player_2 = pygame.image.load(player_type[1]).convert_alpha()

        self.player_walk = [player_1, player_2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 620))

        self.gravity = 1
        self.speedy = 0
        self.jump_bool = False
        self.melodia_index = 0

    def isCollidingPlatform(self, platforms):
        """
        Método que verifica se o jogador está colidindo com uma plataforma.

        Argumentos:
            platforms: Grupo contendo as plataformas.

        Retornos:
            platform ou False: A plataforma com a qual o jogador está colidindo ou False se não houver colisão.
        """

        platforms_hit = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platforms_hit:
            if self.rect.colliderect(platform.rect):
                return platform

    def isCollidingGround(self, ground):
        """
        Método que verifica se o jogador está colidindo com o chão.

        Argumentos:
            ground: Grupo contendo o chão.

        Retornos:
            booleano: True se o jogador estiver colidindo com o solo ou False se não houver colisão.
        """

        for g in ground:
            if self.rect.colliderect(g.rect):
                return True

    def jump(self):
        """
        Método que realiza o pulo do jogador.

        Verifica se a tecla de espaço foi pressionada e se o jogador não está pulando.
        Se ambas as condições forem verdadeiras, aplica a velocidade vertical negativa
        para subir o jogador e define o estado de pulo como True.
        """

        if keys[pygame.K_SPACE] and not self.jump_bool:
            melodia = [4, 3, 2, 1]
            melodiaint=random.choice(melodia)
            if not game_state['hell']:
                jump_sound = pygame.mixer.Sound(f"music/jumps/jump{melodiaint}.mp3")
            else:
                jump_sound = pygame.mixer.Sound("music/jump_sound.mp3")

            jump_volume = 0.1
            jump_sound.set_volume(jump_volume)
            jump_sound.play()

            self.speedy -= 20
            self.jump_bool = True

    def apply_gravity(self):
        """
        Método que aplica a gravidade no jogador.

        Aplica a gravidade normal somente se o jogador estiver no ar e a tecla de espaço não estiver pressionada.
        Caso esrtiver no ar com o espaço apertado, o jogador plana.
        Em seguida, atualiza a posição vertical do jogador com base na velocidade vertical e gravidade,
        leva em conta também a colisão com o chão e com as plataformas.
        """

        if keys[pygame.K_SPACE] and self.speedy >= 0:
            self.gravity = 0.1
        else:
            self.gravity = 1

        self.speedy += self.gravity
        self.rect.y += self.speedy

        if self.rect.bottom > 620:
            self.rect.bottom = 620
            self.speedy = 0
            self.jump_bool = False

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
        """
        Método que define o estado da animação do jogador.

        Se a velocidade em y do jogador for nula, ou seja, estiver no chão ou em uma plataforma,
        aumenta o índice do sprite do jogador para animar a caminhada.
        """

        if self.speedy == 0:
            self.player_index += 0.1
            self.image = self.player_walk[int(self.player_index % len(self.player_walk))]

    def collision_player_rocks():
        """
        Método que verifica se o jogador está colidindo com uma pedra.

        Retorna:
            booleano: True se o jogador está colidindo com uma pedra, nada caso contrário.
        """

        if pygame.sprite.spritecollide(player.sprite, rocks, False):
            return True
        
    def collision_player_portal():
        """
        Método que verifica se o jogador está colidindo com um portal.

        Retorna:
            booleano: True se o jogador está colidindo com um portal, nada caso contrário.
        """

        if pygame.sprite.spritecollide(player.sprite, portal, False):
            portal_sound = pygame.mixer.Sound("music/portal.mp3")
            portal_volume = 0.2
            portal_sound.set_volume(portal_volume)
            portal_sound.play()
            return True
        
    def collision_player_demon():
        """
        Método que verifica se o jogador está colidindo com o demônio.

        Retorna:
            booleano: True se o jogador está colidindo com o domônio, nada caso contrário.
        """

        if pygame.sprite.spritecollide(player.sprite, demon, False):
            portal_sound = pygame.mixer.Sound("music/portal.mp3")
            portal_volume = 0.2
            portal_sound.set_volume(portal_volume)
            portal_sound.play()
            return True

    def update(self):
        """
        Atualiza o jogador.

        Chama os métodos apply_gravity(), jump() e animation_state() para atualizar o jogador.
        """

        self.apply_gravity()
        self.jump()
        self.animation_state()

################# CONFIGURAÇÕES #################

# Configurações da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Existential Crisis")

clock = pygame.time.Clock()

# Carregando Fontes
font_pixel = pygame.font.Font('font/Pixeltype.ttf', 50)
font_blox = pygame.font.Font('font/blox-brk.regular.ttf', 75)

# Inicializa o mixer
mixer.init()
# Carrega arquivo de áudio
mixer.music.load('music/music.mp3')
# Define um volume
mixer.music.set_volume(0.4)
# Reproduz em loop a música
mixer.music.play(-1)

next_track = True

# Boleano para o controle da musica do game over
bool_game_over_music=True

"""
Grupos de jogador, árvore, chão, portal e demônio.

Estilos com os assets que serão utilizados em cada fase diferente do jogo
"""

player = pygame.sprite.GroupSingle()
player.add(Player(player_sprites['kid']))

speed = {
    'kid': 4,
    'man': 5,
    'oldman': 6,
    'hell': 7,
}

tree.add(Tree(speed['kid']))

ground_styles = {
    'kid': 'assets/morning/ground_morning.png',
    'man': 'assets/afternoon/ground_afternoon.png',
    'oldman': 'assets/night/ground_night.png',
    'hell': 'assets/hell/hell_ground.png',
}
ground.add(Ground(0, ground_styles['kid'], speed['kid']))
ground.add(Ground(WIDTH, ground_styles['kid'], speed['kid']))

portal.add(Portal(speed['kid']))

background_styles = {
    'kid': 'assets/morning/sky_morning.png',
    'man': 'assets/afternoon/sky_afternoon.png',
    'oldman': ['assets/night/sky_night.png', 'assets/night/sky_night2.png'],
    'hell': 'assets/hell/hell_background.png',
}

rock_styles = {
    'normal': 'assets/rock.png',
    'hell': 'assets/hell/hell_rock.png',
}

platform_style = {
    'kid': 'assets/morning/platform_morning.png',
    'man': 'assets/afternoon/platform_afternoon.png',
    'oldman': 'assets/night/platform_night.png',
    'hell': 'assets/hell/hell_platform.png',
}

# Dicionário com os diferentes estados que o jogo pode ter
game_state = {
    'playing_kid': False,
    'playing_man': False,
    'playing_oldman': False, 
    'hell': False,
    'game_over': False,
    'menu': False, 
    'player_name': True
}


# Pontuação
score = 0
score_text = font_pixel.render("Score: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(topleft=(10, 10))

# Timers para geração de plataformas e das pedras
structure = pygame.USEREVENT + 1
pygame.time.set_timer(structure, 3200)

def transition(screen):
    """
    Função que realiza a transição entre as fases do jogo.

    Argumentos:
        screen: Tela do jogo na qual a troca será feita.
    """
    fade_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for alpha in range(0, 255, 5):
        fade_surface.fill((0, 0, 0, alpha))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)
        
################# GAME LOOP #################
while True:
    # Lê o arquivo de CSV com o placar
    scoreboard = pd.read_csv('scoreboard.csv')

    # Pega input do teclado
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        # Verifica se o jogador clicou no X da janela e fecha o jogo se sim
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """
        Gera estruturas no jogo a cada intervalo do timer, e é selecionado aleatoriamente entre 3 tipos de estruturas.
        """
        if event.type == structure and not (game_state['menu'] or game_state['player_name']):
            structures = [
                structure_1,
                structure_1,
                structure_1,
                structure_2,
                structure_3
            ]
            random.choice(structures)(game_state, rocks, platforms, rock_styles, platform_style, speed)
            
        """
        Coleta o input de nome do jogador, armazena em uma variável.
        Muda o estado do jogo para o menu inicial quando o jogador enviar seu nome.
        """
        if event.type == pygame.KEYDOWN and game_state['player_name']:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # Se o jogador não digitar nada, o nome padrão é "qwerty".
                if player_name == '':
                    player_name = 'qwerty'
                game_state['player_name'] = False
                game_state['menu'] = True
            elif event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            else:
                player_name += event.unicode

    if game_state['player_name']:
        """
        Estado do jogo no qual o jogador digita seu nome.
        Carrega os assets e textos necessários para essa tela.
        Mostra esses assets e textos na tela.
        """

        background = pygame.image.load(background_styles['kid']).convert_alpha()
        background_rect = background.get_rect(bottomleft=(0, 800))
        screen.blit(background, background_rect)
        background_2 = pygame.image.load(background_styles['kid']).convert_alpha()
        background_2_rect = background.get_rect(bottomleft=(3840, 800))
        
        game_name = font_blox.render("EXISTENTIAL CRISIS", True, (255, 255, 255))
        game_name_rect = game_name.get_rect(center=((WIDTH / 2), HEIGHT / 2 - 250))
        screen.blit(game_name, game_name_rect)

        player_stand = pygame.image.load('assets/kid/player_stand.png').convert_alpha()
        player_stand_rect = player_stand.get_rect(midbottom=(100, 620))
        screen.blit(player_stand, player_stand_rect)

        tree_stand = pygame.image.load('assets/tree.png').convert_alpha()
        tree_stand = pygame.transform.scale(tree_stand, (150, 150))
        tree_stand_rect = tree_stand.get_rect(bottomleft=(0, 620))
        screen.blit(tree_stand, tree_stand_rect)

        ground.draw(screen)
        
        name_text = font_pixel.render(f"Enter your name: {player_name}", True, (255, 255, 255))
        name_text_rect = name_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(name_text, name_text_rect)


    elif game_state['menu']:
        """
        Estado do jogo de menu que espera que o jogador aperte ESPAÇO para iniciar o jogo,
        caso sim, as variáveis de estado do jogo são alteradas.
        Carrega os assets e textos necessários para essa tela.
        Mostra esses assets e textos na tela.
        """

        # Limpa os grupos de pedras e plataformas para evitar bugs
        rocks.empty()
        platforms.empty()

        screen.blit(background, background_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(tree_stand, tree_stand_rect)
        screen.blit(game_name, game_name_rect)
        ground.draw(screen)

        start_text = font_pixel.render(f"Press SPACE to START", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 320))
        screen.blit(start_text, start_text_rect)

        leaderboard_text = font_pixel.render(f"Leaderboard:", True, (255, 255, 255))
        leaderboard_rect = leaderboard_text.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 125))
        screen.blit(leaderboard_text, leaderboard_rect)

        # Loop para mostrar os 3 melhores scores do jogo na tela
        for i in range(3):
            leaderboard = font_pixel.render(
                f"{i+1}: {scoreboard['Name'][i]} - {scoreboard['Score'][i]}pts", True, (255, 255, 255))
            leaderboard_rect = leaderboard.get_rect(topleft=((WIDTH / 2 + 200), HEIGHT / 2 - 75 + i*50))
            screen.blit(leaderboard, leaderboard_rect)

        if keys[pygame.K_SPACE]:
            game_state['playing_kid'] = True
            game_state['menu'] = False

    elif game_state['playing_kid']:
        """
        Estado do jogo da fase da criança.
        Desenha e atualiza as classes de árvore, jogador, pedras, plataformas, chão e portal na tela.
        Caso o jogador colida com alguma pedra, o jogo acaba e o estado do jogo é alterado para game over.
        Caso o jogador colida com o portal, o estado do jogo é alterado para a fase do adulto,
        é realizada a transição, os assets são ajustados e os grupos são esvaziados e depois repovoados para a fase do adulto.
        """

        screen.blit(background, background_rect)
        screen.blit(background_2, background_2_rect)
        screen.blit(score_text, score_rect)
        tree.draw(screen)
        tree.update()

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

        # Ativa o som de game over
        bool_game_over_music = True

        # Lógica para que o fundo seja infinito
        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        # Movimentação do cenário
        background_rect.x -= 1
        background_2_rect.x -= 1
        game_name_rect.x -= 1
        
        # Verifica colisão com a pedra
        if Player.collision_player_rocks():
            game_state['playing_kid'] = False
            game_state['game_over'] = True
        
        # Verifica colisão com o portal
        if Player.collision_player_portal():
            transition(screen)
            game_state['playing_kid'] = False
            game_state['playing_man'] = True
            background = pygame.image.load(background_styles['man']).convert_alpha()
            background_2 = pygame.image.load(background_styles['man']).convert_alpha()
            background_rect = background.get_rect(bottomleft=(0, 800))
            background_2_rect = background.get_rect(bottomleft=(3840, 800))
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            player.add(Player(player_sprites['man']))
            ground.add(Ground(0, ground_styles['man'], speed['man']))
            ground.add(Ground(WIDTH, ground_styles['man'], speed['man']))
            portal.add(Portal(speed['man']))

        # Atualiza a pontuação
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))
    

    elif game_state['playing_man']:
        """
        Estado do jogo da fase do adulto.
        Desenha e atualiza as classes de jogador, pedras, plataformas, chão e portal na tela.
        Caso o jogador colida com alguma pedra, o jogo acaba e o estado do jogo é alterado para game over.
        Caso o jogador colida com o portal, o estado do jogo é alterado para a fase do idoso,
        é realizada a transição, os assets são ajustados e os grupos são esvaziados e depois repovoados para a fase do idoso.
        """

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

        # Lógica para que o fundo seja infinito
        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        # Movimentação do cenário
        background_rect.x -= 1
        background_2_rect.x -= 1

        # Verifica colisão com a pedra
        if Player.collision_player_rocks():
            game_state['playing_man'] = False
            game_state['game_over'] = True

        # Verifica colisão com o portal
        if Player.collision_player_portal():
            transition(screen)
            game_state['playing_man'] = False
            game_state['playing_oldman'] = True
            background = pygame.image.load(background_styles['oldman'][0]).convert_alpha()
            background_2 = pygame.image.load(background_styles['oldman'][1]).convert_alpha()
            background_rect = background.get_rect(bottomleft=(0, 800))
            background_2_rect = background.get_rect(bottomleft=(3840, 800))
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            demon.add(Demon(speed['oldman']))
            player.add(Player(player_sprites['oldman']))
            ground.add(Ground(0, ground_styles['oldman'], speed['oldman']))
            ground.add(Ground(WIDTH, ground_styles['oldman'],  speed['oldman']))

        # Atualiza a pontuação
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))


    elif game_state['playing_oldman']:
        """
        Estado do jogo da fase do idoso.
        Desenha e atualiza as classes de jogador, pedras, plataformas, chão e demônio na tela.
        Caso o jogador colida com alguma pedra, o jogo acaba e o estado do jogo é alterado para game over.
        Caso o jogador colida com o demônio, o estado do jogo é alterado para a fase do inferno,
        é realizada a transição, há troca de música, os assets são ajustados
        e os grupos são esvaziados e depois repovoados para a fase do inferno.
        """

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

        # Lógica para que o fundo seja infinito
        if background_2_rect.topright[0] == WIDTH:
            background_rect.x = WIDTH
        elif background_rect.topright[0] == WIDTH:
            background_2_rect.x = WIDTH

        # Movimentação do cenário
        background_rect.x -= 1
        background_2_rect.x -= 1
        
        # Verifica colisão com a pedra
        if Player.collision_player_rocks():
            game_state['playing_oldman'] = False
            game_state['game_over'] = True

        # Verifica colisão com o demônio
        if Player.collision_player_demon():
            transition(screen)
            game_state['playing_oldman'] = False
            game_state['hell'] = True
            
            background = pygame.image.load(background_styles['hell']).convert_alpha()
            background_2 = pygame.image.load(background_styles['hell']).convert_alpha()
            background_rect = background.get_rect(bottomleft=(0, 800))
            background_2_rect = background.get_rect(bottomleft=(3840, 800))
            player.empty()
            rocks.empty()
            platforms.empty()
            ground.empty()
            portal.empty()

            player.add(Player(player_sprites['skeleton']))
            ground.add(Ground(0, ground_styles['hell'],  speed['hell']))
            ground.add(Ground(WIDTH, ground_styles['hell'], speed['hell']))
            
            mixer.music.load('music/music_hell.mp3')
            mixer.music.set_volume(0.4)
            mixer.music.play()

        # Atualiza a pontuação
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))

    elif game_state['hell']:
        """
        Estado do jogo da fase do inferno.
        Alguns assets não são equivalentes aos das outras fases, como a troca da pedra por um olho,
        mas o funcionamento é o mesmo, por isso a classe e a lógica são mantidas, apenas o asset é alterado.
        Desenha e atualiza as classes de jogador, pedras, plataformas e chão na tela.
        Caso o jogador colida com alguma pedra, o jogo acaba e o estado do jogo é alterado para game over.
        Nesse caso, o jogo só termina quando o jogador perder.
        """

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

        # Lógica para que o fundo seja infinito
        if background_2_rect.topright[0] <= 0:
            background_2_rect.x = 3840
        elif background_rect.topright[0] <= 0:
            background_rect.x = 3840
        
        # Movimentação do cenário
        background_rect.x -= 1
        background_2_rect.x -= 1

        # Verifica colisão com a pedra
        if Player.collision_player_rocks():
            game_state['hell'] = False
            game_state['game_over'] = True

        # Atualiza a pontuação
        score += 0.2
        score_text = font_pixel.render("Score: " + str(floor(score)), True, (255, 255, 255))

    

    elif game_state['game_over']:
        """
        Estado do jogo de game over que espera que mostra a pontução final do jogador, sua pontuação máxima
        e a maior pontuação obtida por todos os jogadores.
        Espera que o jogador aperte R para reiniciar o jogo ou ESC para sair e voltar a tela de digitar seu nome.
        Os grupos são esvaziados e depois repovoados caso o jogo seja reiniciado.
        Carrega os assets e textos necessários para essa tela.
        Mostra esses assets e textos na tela.
        """

        # PARA A MUSICA QUE ESTA TOCANDO
        mixer.music.stop()
        # Carrega a música de game over
        game_over_music = pygame.mixer.Sound('music/game_over.mp3')
        # Reproduz a música de game over
        if bool_game_over_music==True:
            # Define o volume desejado (0.0 a 1.0)
            game_over_music_volume = 0.07
            game_over_music.set_volume(game_over_music_volume)
            game_over_music.play()
        bool_game_over_music=False


        player.empty()
        rocks.empty()
        platforms.empty()
        ground.empty()
        portal.empty()
        demon.empty()

        screen.fill((94, 129, 162))
        background_rect.x = 0
        game_name_rect.center = (WIDTH / 2, HEIGHT / 2 - 250)

        # Salva a pontuação no scoreboard
        save_score(player_name, score, scoreboard)

        game_over_text = font_pixel.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        best_score = scoreboard.loc[scoreboard['Name'] == player_name, 'Score']
        your_best_score = font_pixel.render("Your Best Score: " + str(floor(best_score)), True, (255, 255, 255))
        best_score_rect = your_best_score.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        screen.blit(your_best_score, best_score_rect)
        
        restart_text = font_pixel.render("Press R to restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(WIDTH / 2 - 200, HEIGHT / 2 + 150))
        screen.blit(restart_text, restart_rect)
        
        quit_text = font_pixel.render("Press ESC to quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=(WIDTH / 2 + 200, HEIGHT / 2 + 150))
        screen.blit(quit_text, quit_rect)

        overall_best_score = scoreboard['Score'].max()
        overall_best_score_text = font_pixel.render(
            "Overall Best Score: " + str(floor(overall_best_score)), True, (255, 255, 255))
        overall_best_score_rect = overall_best_score_text.get_rect(center=((WIDTH / 2), HEIGHT / 2 + 250))
        screen.blit(overall_best_score_text, overall_best_score_rect)

        # Se o jogador apertar R, o jogo é reiniciado
        if keys[pygame.K_r]:
            game_state['menu'] = True
            game_state['game_over'] = False
            score = 0
            player.add(Player(player_sprites['kid']))
            ground.add(Ground(0, ground_styles['kid'], speed['kid']))
            ground.add(Ground(WIDTH, ground_styles['kid'], speed['kid']))
            background = pygame.image.load(background_styles['kid']).convert_alpha()
            background_2 = pygame.image.load(background_styles['kid']).convert_alpha()
            background_rect = background.get_rect(bottomleft=(0, 800))
            background_2_rect = background.get_rect(bottomleft=(3840, 800))
            portal.add(Portal(speed['kid']))
            tree.add(Tree(speed['kid']))
            mixer.music.load('music/music.mp3')
            mixer.music.play(-1)

        # Se o jogador apertar ESC, o jogo volta para a tela de digitar seu nome
        elif keys[pygame.K_ESCAPE]:
            game_state['player_name'] = True
            game_state['game_over'] = False
            score = 0
            player_name = ''
            ground.add(Ground(0, ground_styles['kid'], speed['kid']))
            ground.add(Ground(WIDTH, ground_styles['kid'], speed['kid']))
            player.add(Player(player_sprites['kid']))
            tree.add(Tree(speed['kid']))
            portal.add(Portal(speed['kid']))
            mixer.music.load('music/music.mp3')
            mixer.music.play(-1)

    pygame.display.flip()
    clock.tick(60)
