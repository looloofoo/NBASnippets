import pandas as pd
import os
from .fetch_data import fetch_last_game_stats, commonplayerinfo
"""
######################################################################
# This script fetches the last game statistics from 'fetch_data.py'  # 
# and creates an html fo the players stats in 'generated_files'      #
######################################################################
"""
def get_player_name(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_name = player_info.get_data_frames()[0]['DISPLAY_FIRST_LAST'].values[0]
    return player_name

def save_stats_to_html(player_id, season, directory="html_files"):
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    stats = fetch_last_game_stats(player_id, season)
    player_name = get_player_name(player_id)
    sanitized_player_name = player_name.replace(" ", "_")  # Replace spaces with underscores for the filename
    filename = f"{sanitized_player_name}_stats.html"
    filepath = os.path.join(directory, filename)

    # Create a DataFrame from the stats dictionary
    stats_df = pd.DataFrame(list(stats.items()), columns=['Stats', 'Value'])

    # Generate the image path
    img_path = os.path.join('imgs', f"{player_id}.png")
    
    # Write HTML to file in the specified directory
    with open(filepath, 'w') as f:
        f.write('<html>\n<head>\n')
        f.write('<link rel="stylesheet" type="text/css" href="../css/styles.css">\n')
        f.write('<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">\n')
        f.write('</head>\n<body>\n')
        f.write(f'<h1>{player_name}</h1>\n')
        if os.path.exists(img_path):  # Check if the image exists
            f.write(f'<img src="../{img_path}" alt="{player_name}" style="width:200px;height:auto;">\n')
        f.write('<div class="container">\n')
        f.write(stats_df.to_html(index=False, escape=False))
        f.write('</div>\n</body>\n</html>')

    return filepath