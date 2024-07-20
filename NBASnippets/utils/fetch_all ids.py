from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
import pandas as pd
import os
import json

def fetch_miami_heat_players():
    # Get the Miami Heat team ID
    team_list = teams.find_teams_by_full_name('Miami Heat')
    if not team_list:
        print("Miami Heat team not found.")
        return []
    
    miami_heat_id = team_list[0]['id']

    # Fetch the team roster
    team_roster = commonteamroster.CommonTeamRoster(team_id=miami_heat_id)
    roster_df = team_roster.get_data_frames()[0]

    # Extract relevant information
    players_info = roster_df[['PLAYER', 'PLAYER_ID']].rename(columns={'PLAYER': 'full_name', 'PLAYER_ID': 'id'})
    players = players_info.to_dict('records')

    return players

def save_to_json(players):
    # Ensure the json_files directory exists
    os.makedirs('json_files', exist_ok=True)

    # Define the file path
    file_path = 'json_files/miami_heat_players.json'

    # Write the player data to a JSON file
    with open(file_path, 'w') as f:
        json.dump(players, f, indent=4)

    print(f"JSON file generated successfully: {file_path}")

if __name__ == "__main__":
    players = fetch_miami_heat_players()
    if players:
        save_to_json(players)
