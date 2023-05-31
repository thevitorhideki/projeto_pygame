import random

from classes.platforms import Platforms
from classes.rocks import Rocks
from settings import WIDTH

def structure_1(game_state, rocks, platforms, rock_styles, platform_style, speed):
    """
    Cria a estrutura 1 do jogo.

    Argumentos:
        game_state: Qual senário o jogador está.
        rocks: Grupo das pedras.
        platforms: Grupo das plataformas.
        rock_styles: Estilos das pedras.
        platform_style: Estilo das plataformas.
        speed: Velocidade do jogo.
    """
    if game_state['playing_kid']:
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200), 540 - 20, rock_styles['normal'], speed['kid']))
        platforms.add(Platforms(WIDTH, 540, platform_style['kid'], speed['kid']))
        platforms.add(Platforms(WIDTH + 128, 540, platform_style['kid'], speed['kid']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 256, 440 - 20, rock_styles['normal'], speed['kid']))
        platforms.add(Platforms(WIDTH + 256, 440, platform_style['kid'], speed['kid']))
        platforms.add(Platforms(WIDTH + 128 + 256, 440, platform_style['kid'], speed['kid']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 512, 340 - 20, rock_styles['normal'], speed['kid']))
        platforms.add(Platforms(WIDTH + 512, 340, platform_style['kid'], speed['kid']))
        platforms.add(Platforms(WIDTH + 128 + 512, 340, platform_style['kid'], speed['kid']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 500), 620, rock_styles['normal'], speed['kid']))
        rocks.add(Rocks(random.randint(WIDTH + 500, WIDTH + 1000), 620, rock_styles['normal'], speed['kid']))
    elif game_state['hell']:
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200), 540 - 20, rock_styles['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH, 540, platform_style['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 128, 540, platform_style['hell'], speed['hell']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 256, 440 - 20, rock_styles['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 256, 440, platform_style['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 128 + 256, 440, platform_style['hell'], speed['hell']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 512, 340 - 20, rock_styles['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 512, 340, platform_style['hell'], speed['hell']))
        platforms.add(Platforms(WIDTH + 128 + 512, 340, platform_style['hell'], speed['hell']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 500), 620, rock_styles['hell'], speed['hell']))
        rocks.add(Rocks(random.randint(WIDTH + 500, WIDTH + 1000), 620, rock_styles['hell'], speed['hell']))
    elif game_state['playing_man']:
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200), 540 - 20, rock_styles['normal'], speed['man']))
        platforms.add(Platforms(WIDTH, 540, platform_style['man'], speed['man']))
        platforms.add(Platforms(WIDTH + 128, 540, platform_style['man'], speed['man']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 256, 440 - 20, rock_styles['normal'], speed['man']))
        platforms.add(Platforms(WIDTH + 256, 440, platform_style['man'], speed['man']))
        platforms.add(Platforms(WIDTH + 128 + 256, 440, platform_style['man'], speed['man']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 512, 340 - 20, rock_styles['normal'], speed['man']))
        platforms.add(Platforms(WIDTH + 512, 340, platform_style['man'], speed['man']))
        platforms.add(Platforms(WIDTH + 128 + 512, 340, platform_style['man'], speed['man']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 500), 620, rock_styles['normal'], speed['man']))
        rocks.add(Rocks(random.randint(WIDTH + 500, WIDTH + 1000), 620, rock_styles['normal'], speed['man']))
    elif game_state['playing_oldman']:
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200), 540 - 20, rock_styles['normal'], speed['oldman']))
        platforms.add(Platforms(WIDTH, 540, platform_style['oldman'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 128, 540, platform_style['oldman'], speed['oldman']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 256, 440 - 20, rock_styles['normal'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 256, 440, platform_style['oldman'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 128 + 256, 440, platform_style['oldman'], speed['oldman']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 200) + 512, 340 - 20, rock_styles['normal'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 512, 340, platform_style['oldman'], speed['oldman']))
        platforms.add(Platforms(WIDTH + 128 + 512, 340, platform_style['oldman'], speed['oldman']))
        
        rocks.add(Rocks(random.randint(WIDTH, WIDTH + 500), 620, rock_styles['normal'], speed['oldman']))
        rocks.add(Rocks(random.randint(WIDTH + 500, WIDTH + 1000), 620, rock_styles['normal'], speed['oldman']))