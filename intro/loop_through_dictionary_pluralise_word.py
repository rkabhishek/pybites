def print_game_stats(games_won):
    for name, num_games in games_won.items():
        suffix = 'game' if num_games == 1 else 'games'
        print(f'{name} has won {num_games} {suffix}')
