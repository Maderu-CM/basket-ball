def game_dict():
    return {
        'home': {
            'team_name': 'Cleveland Cavaliers',
            'colors': ['wine', 'gold'],
            'players': [
                {
                    'player_name': 'LeBron James',
                    'number': 23,
                    'points_per_game': 25.0,
                    'age': 36,
                    'shoe_brand': 'Nike',
                    'career_points': 35000,
                    'position': 'Forward',
                    'rebounds_per_game': 7.4,
                    'assists_per_game': 7.4,
                    'steals_per_game': 1.6,
                    'blocks_per_game': 0.9,
                    'height_inches': 80,
                },
                {
                    'player_name': 'Kevin Love',
                    'number': 0,
                    'points_per_game': 12.5,
                    'age': 32,
                    'shoe_brand': 'Nike',
                    'career_points': 11000,
                    'position': 'Center',
                    'rebounds_per_game': 9.0,
                    'assists_per_game': 3.5,
                    'steals_per_game': 0.8,
                    'blocks_per_game': 0.4,
                    'height_inches': 82,
                },
            ],
        },
        'away': {
            'team_name': 'Golden State Warriors',
            'colors': ['blue', 'yellow'],
            'players': [
                {
                    'player_name': 'Stephen Curry',
                    'number': 30,
                    'points_per_game': 28.7,
                    'age': 33,
                    'shoe_brand': 'Under Armour',
                    'career_points': 28000,
                    'position': 'Guard',
                    'rebounds_per_game': 5.5,
                    'assists_per_game': 6.4,
                    'steals_per_game': 1.2,
                    'blocks_per_game': 0.2,
                    'height_inches': 75,
                },
                {
                    'player_name': 'Klay Thompson',
                    'number': 11,
                    'points_per_game': 19.0,
                    'age': 32,
                    'shoe_brand': 'Anta',
                    'career_points': 13000,
                    'position': 'Guard',
                    'rebounds_per_game': 3.9,
                    'assists_per_game': 2.3,
                    'steals_per_game': 0.9,
                    'blocks_per_game': 0.3,
                    'height_inches': 79,
                },
            ],
        },
    }

def num_points_per_game(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['player_name'] == player_name:
                return player['points_per_game']
    return None

def player_age(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['player_name'] == player_name:
                return player['age']
    return None

def team_colors(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team['team_name'] == team_name:
            return team['colors']
    return None

def team_names():
    game_data = game_dict()
    return [team['team_name'] for team in game_data.values()]

def player_numbers(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team['team_name'] == team_name:
            return [player['number'] for player in team['players']]
    return None

def player_stats(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['player_name'] == player_name:
                return {
                    'name': player['player_name'],
                    'number': player['number'],
                    'position': player['position'],
                    'points_per_game': player['points_per_game'],
                    'rebounds_per_game': player['rebounds_per_game'],
                    'assists_per_game': player['assists_per_game'],
                    'steals_per_game': player['steals_per_game'],
                    'blocks_per_game': player['blocks_per_game'],
                    'career_points': player['career_points'],
                    'age': player['age'],
                    'height_inches': player['height_inches'],
                    'shoe_brand': player['shoe_brand'],
                }
    return None

def average_rebounds_by_shoe_brand():
    shoe_brand_rebounds = {}
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            shoe_brand = player['shoe_brand']
            rebounds = player['rebounds_per_game']
            if shoe_brand in shoe_brand_rebounds:
                shoe_brand_rebounds[shoe_brand].append(rebounds)
            else:
                shoe_brand_rebounds[shoe_brand] = [rebounds]

    for brand, rebounds_list in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}: {average_rebounds:.2f}")

# Example usages:
print(num_points_per_game("LeBron James"))
print(player_age("Stephen Curry"))
print(team_colors("Cleveland Cavaliers"))
print(team_names())
print(player_numbers("Golden State Warriors"))
print(player_stats("Klay Thompson"))
average_rebounds_by_shoe_brand()
