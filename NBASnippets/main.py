import webbrowser
import json
import os
from utils.to_html import save_stats_to_html
from utils.fetch_data import update_json_with_last_game_stats

####################################
# Main execution block  
####################################

if __name__ == "__main__":

    json_file = 'json_files/miami_heat_players.json'
    season = '2023'  # Specify the season here
    update_json_with_last_game_stats(json_file, season)

    # Read the updated JSON file
    with open(json_file, 'r') as f:
        players_data = json.load(f)

    file_paths = []
    for player in players_data:
        player_id = player['id']
        save_stats_to_html(player_id, season)
        file_path = save_stats_to_html(player_id, season)
        file_paths.append(file_path)

    for path in file_paths:
        print(path)
        # Open the HTML file in the default web browser
        webbrowser.open(f'file://{os.path.realpath(path)}')