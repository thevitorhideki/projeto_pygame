from classes.rocks import Rocks
from settings import WIDTH


def structure_2(game_state, rocks, platforms, rock_styles, platform_style, speed):
    """
    Cria a estrutura 2 do jogo.

    Argumentos:
        game_state: Qual senário o jogador está.
        rocks: Grupo das pedras.
        platforms: Grupo das plataformas.
        rock_styles: Estilos das pedras.
        platform_style: Estilo das plataformas.
        speed: Velocidade do jogo.
    """
    if game_state['playing_kid']:
        rocks.add(Rocks(WIDTH, 620, rock_styles['normal'], speed['kid']))
        rocks.add(Rocks(WIDTH+50, 620, rock_styles['normal'], speed['kid']))
        rocks.add(Rocks(WIDTH+100, 620, rock_styles['normal'], speed['kid']))
    elif game_state['hell']:
        rocks.add(Rocks(WIDTH, 620, rock_styles['hell'], speed['hell']))
        rocks.add(Rocks(WIDTH+50, 620, rock_styles['hell'], speed['hell']))
        rocks.add(Rocks(WIDTH+100, 620, rock_styles['hell'], speed['hell']))
    elif game_state['playing_man']:
        rocks.add(Rocks(WIDTH, 620, rock_styles['normal'], speed['man']))
        rocks.add(Rocks(WIDTH+50, 620, rock_styles['normal'], speed['man']))
        rocks.add(Rocks(WIDTH+100, 620, rock_styles['normal'], speed['man']))
    elif game_state['playing_oldman']:
        rocks.add(Rocks(WIDTH, 620, rock_styles['normal'], speed['oldman']))
        rocks.add(Rocks(WIDTH+50, 620, rock_styles['normal'], speed['oldman']))
        rocks.add(Rocks(WIDTH+100, 620, rock_styles['normal'], speed['oldman']))