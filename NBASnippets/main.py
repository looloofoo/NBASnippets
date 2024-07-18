import webbrowser
import os
from utils.to_html import save_stats_to_html

####################################
# Main execution block  
####################################

if __name__ == "__main__":
    # User input for player ID and season
    player_id = int(input("Enter the player ID: "))
    season = input("Enter the season (e.g., 2023): ")

    try:
        # Return hmtl file created in 'to_html' utils
        filepath = save_stats_to_html(player_id, season)

        # Open the generated HTML file in the default web browser
        webbrowser.open('file://' + os.path.realpath(filepath))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")