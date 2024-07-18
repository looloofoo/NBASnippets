import pandas as pd
import os
from utils.fetch_data import fetch_last_game_stats, commonplayerinfo
"""
######################################################################
# This script fetches the last game statistics from 'fetch_data.py'  # 
# and creates an html fo the players stats in 'generated_files'      #
######################################################################
"""

# Function to get player's name
def get_player_name(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_name = player_info.get_data_frames()[0]['DISPLAY_FIRST_LAST'].values[0]
    return player_name

# Function to save stats to an HTML file in a specified directory
def save_stats_to_html(player_id, season, directory="html_files"):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Fetch stats for the specified player and season
    stats = fetch_last_game_stats(player_id, season)

    # Fetch the player's name
    player_name = get_player_name(player_id)
    sanitized_player_name = player_name.replace(" ", "_")  # Replace spaces with underscores for the filename

    # Define the filename using the player's name
    filename = f"{sanitized_player_name}_stats.html"

    # Convert stats dictionary to a pandas DataFrame
    stats_df = pd.DataFrame(stats)
    stats_df.columns = ['Stats', 'Value']

    # Define the full file path
    filepath = os.path.join(directory, filename)

    # Convert the DataFrame to HTML and save to file
    stats_df.to_html(filepath, index=False)
    with open(filepath, 'w') as f:
        f.write('<html>\n<head>\n')
        f.write('<link rel="stylesheet" type="text/css" href="../css/styles.css">\n')
        f.write('<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">\n')
        f.write('</head>\n<body>\n')
        f.write(f'<h1> {player_name}</h1>\n')
        f.write('<div class="container">\n')
        f.write(stats_df.to_html(index=False, escape=False))
        f.write('\n</body>\n</html>')

    print(f"Stats saved to {filepath}")

    # Return the file path of the generated HTML file
    return filepath
