def print_game_stats(games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing (print, not return) how many games each person has won,
       pluralize 'game' based on number.

       Expected output (ignore the docstring's indentation):

       sara has won 0 games
       bob has won 1 game
       tim has won 5 games
       julian has won 3 games
       jim has won 1 game
    """
    for name, num_games in games_won.items():
        suffix = 'game' if num_games == 1 else 'games'
        print(f'{name} has won {num_games} {suffix}')
