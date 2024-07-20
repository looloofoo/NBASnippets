from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import pandas as pd
import json
import os
"""
######################################################################
# funtions for data fetching.                                        #
######################################################################
"""

#############################
# Function for updating json files for last game stats 
# (TODO: change name to 'update_json_with_last_game_stats' )
#############################

def update_json_with_last_game_stats(json_file, season):
    # Ensure the JSON file exists
    if not os.path.exists(json_file):
        print(f"{json_file} does not exist.")
        return
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"{json_file} is not a valid JSON file.")
        return
    # Ensure data is a dictionary with a 'full_name' key
    
    if not isinstance(data, list) or not all('id' in player and 'full_name' in player for player in data):
        print("Invalid JSON format. Expected a list of dictionaries with 'full_name' and 'id'.")
        return
    
    # Update the JSON data with player stats
    for player in data:
        player_id = player['id']
        try:
            player_stats = fetch_last_game_stats(player_id, season)
            player['last_game_stats'] = player_stats
        except Exception as e:
            print(f"Error fetching data for player ID {player_id}: {e}")
    
    # Write the updated data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Updated {json_file} with the latest game stats.")


#############################
# Helpers
#############################
def fetch_last_game_stats(player_id, season):
    
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = game_log.get_data_frames()[0]
    last_game = df.iloc[0]
   
    # Extract the desired statistics into a dict
    stats = {
        'Minutes Played': int(last_game['MIN']),
        'Points': int(last_game['PTS']),
        'Assists': int(last_game['AST']),
        'Rebounds': int(last_game['REB']),
        'Blocks': int(last_game['BLK']),
        'FGP': f"{last_game['FG_PCT'] * 100:.2f}%",
        '3p.%': f"{last_game['FG3_PCT'] * 100:.2f}%",
        '3p. attempts': int(last_game['FG3A']),
        '+-': int(last_game['PLUS_MINUS'])
    }
    return stats