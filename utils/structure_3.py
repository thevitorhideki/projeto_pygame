from classes.platforms import Platforms
from classes.rocks import Rocks
from settings import WIDTH

def structure_3(game_state, rocks, platforms, rock_styles, platform_style, speed):
    """
    Cria a estrutura 3 do jogo.

    Argumentos:
        game_state: Qual senário o jogador está.
        rocks: Grupo das pedras.
        platforms: Grupo das plataformas.
        rock_styles: Estilos das pedras.
        platform_style: Estilo das plataformas.
        speed: Velocidade do jogo.
    """
    if game_state['playing_kid']:
        for i in range(WIDTH, 1664, 50):
            rocks.add(Rocks(i, 620, rock_styles['normal'], speed['kid']))
        platforms.add(Platforms(WIDTH + 138, 520, platform_style['kid'], speed['kid']))
    elif game_state['hell']:
        for i in range(1280, 1664, 50):
            rocks.add(Rocks(i, 620, rock_styles['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 138, 520, platform_style['hell'], speed['hell']))
    elif game_state['playing_man']:
        for i in range(1280, 1664, 50):
            rocks.add(Rocks(i, 620, rock_styles['normal'], speed['man']))
        platforms.add(Platforms(WIDTH + 138, 520, platform_style['man'], speed['man']))
    elif game_state['playing_oldman']:
        for i in range(1280, 1664, 50):
            rocks.add(Rocks(i, 620, rock_styles['normal'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 138, 520, platform_style['oldman'], speed['oldman']))
            