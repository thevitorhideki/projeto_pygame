from math import floor

def save_score(player_name, score, scoreboard):
    """
    Salva a pontuação do jogador no placar.

    Verifica se o nome do jogador já está no placar e atualiza o score se for maior.
    Caso contrário, adiciona um novo registro com o nome do jogador e score.
    Em seguida, ordena o placar por ordem decrescente de score.

    Argumentos:
        player_name: Nome do jogador.
        score: Pontuação do jogador.
        scoreboard: CSV representando o placar.
    """

    if player_name not in scoreboard['Name'].values:
        scoreboard.loc[len(scoreboard)] = [player_name, floor(score)]
    elif player_name in scoreboard['Name'].values and score > scoreboard[scoreboard['Name'] == player_name]['Score'].values[0]:
        scoreboard.loc[scoreboard['Name'] == player_name, 'Score'] = floor(score)
    scoreboard = scoreboard.sort_values(by=['Score'], ascending=False)

    scoreboard.to_csv('scoreboard.csv', index=False)