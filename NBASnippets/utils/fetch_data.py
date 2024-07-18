from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import pandas as pd
"""
######################################################################
# This script fetches the last game statistics for a specified NBA   #
# player and season using the nba_api library.                       #
#                                                                    #   
# Functions:                                                         #
# - fetch_last_game_stats(player_id, season): Fetches last game      #
#   stats for the specified player and season.                       #
#                                                                    #
# Dependencies:                                                      #
# - nba_api                                                          #
# - pandas                                                           #
######################################################################
"""

#############################
# Functions for data fetching
#############################

# Function for fetching stats from last game
def fetch_last_game_stats(player_id, season):
    # Fetch the game logs for the player
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)

    # Convert the data to a pandas DataFrame
    df = game_log.get_data_frames()[0]

    # Get the last game row
    last_game = df.iloc[0]

    # Fetch the player's name
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
   
    # Extract the desired statistics into a dict
    stats = {
        'Statistics': [
            'Points',
            'Assists',
            'Blocks',
            'FGP',
            '3p.%', 
            '3p. attempts',
            '+-'
        ],
        'Value': [
            last_game['PTS'],
            last_game['AST'],
            last_game['BLK'],
            f"{last_game['FG_PCT'] * 100:.2f}%",
            f"{last_game['FG3_PCT'] * 100:.2f}%",
            last_game['FG3A'],
            last_game['PLUS_MINUS']
        ]
    }
    return stats
