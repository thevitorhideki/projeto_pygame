from math import floor

def save_score(player_name, score, scoreboard):
    if player_name not in scoreboard['Name'].values:
            scoreboard.loc[len(scoreboard)] = [player_name, floor(score)]
    elif player_name in scoreboard['Name'].values and score > scoreboard[scoreboard['Name'] == player_name]['Score'].values[0]:
        scoreboard.loc[scoreboard['Name'] == player_name, 'Score'] = floor(score)
    scoreboard = scoreboard.sort_values(by=['Score'], ascending=False)

    scoreboard.to_csv('scoreboard.csv', index=False)