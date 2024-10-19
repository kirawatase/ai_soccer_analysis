import matplotlib.pyplot as plt
import os
import numpy as np

class PlayerMaxSpeedAnalyzer:
    def __init__(self, tracks, team_assigner):
        self.tracks = tracks
        self.team_assigner = team_assigner
        self.max_speeds_team_1 = {}
        self.max_speeds_team_2 = {}

    def calculate_max_speed_per_player(self):
        """Calculate the maximum speed for each player and separate by teams."""
        for frame_num, player_track in enumerate(self.tracks['players']):
            for player_id, track in player_track.items():
                speed = track.get('speed', 0)  # Get the speed of the player in the current frame
                
                # Determine the player's team
                team = self.team_assigner.get_player_team(None, track['bbox'], player_id)

                # Store maximum speed for each player on the correct team, limit to 11 players per team
                if team == 1 and len(self.max_speeds_team_1) < 11:  # Team 1
                    if player_id not in self.max_speeds_team_1:
                        self.max_speeds_team_1[player_id] = speed
                    else:
                        self.max_speeds_team_1[player_id] = max(self.max_speeds_team_1[player_id], speed)
                elif team == 2 and len(self.max_speeds_team_2) < 11:  # Team 2
                    if player_id not in self.max_speeds_team_2:
                        self.max_speeds_team_2[player_id] = speed
                    else:
                        self.max_speeds_team_2[player_id] = max(self.max_speeds_team_2[player_id], speed)

    def plot_max_speeds(self):
        """Generate individual horizontal bar charts for the maximum speeds of players on Team 1 and Team 2 with custom colors."""
        # Create the assets folder if it doesn't exist
        assets_folder = os.path.join(os.getcwd(), "assets")
        if not os.path.exists(assets_folder):
            os.makedirs(assets_folder)

        # Filter out players with 0.0 m/s speed for both teams
        self.max_speeds_team_1 = {player_id: speed for player_id, speed in self.max_speeds_team_1.items() if speed > 0}
        self.max_speeds_team_2 = {player_id: speed for player_id, speed in self.max_speeds_team_2.items() if speed > 0}

        # Plot horizontal bar chart for Team 1 (individual output)
        if self.max_speeds_team_1:
            players_team_1 = list(self.max_speeds_team_1.keys())
            speeds_team_1 = list(self.max_speeds_team_1.values())
            
            plt.figure(figsize=(12, 8))

            # Plot horizontal bars with the correct Team 1 color (#6684a5)
            bars = plt.barh(np.arange(len(players_team_1)), speeds_team_1, height=0.8, color='#6684a5')

            plt.gca().set_yticks(np.arange(len(players_team_1)))
            plt.gca().set_yticklabels(players_team_1, fontsize=10)

            plt.title('Maximum Speed of Players on Team 1', fontsize=14, pad=15)
            plt.xlabel('Max Speed (m/s)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height()/2, '{:.2f} m/s'.format(width),
                         ha='left', va='center', fontsize=10, fontweight='bold')

            output_path_team_1 = os.path.join(assets_folder, "team_1_max_speed_chart.png")
            plt.savefig(output_path_team_1, dpi=300, bbox_inches='tight')
            print(f"Max speed chart for Team 1 saved to {output_path_team_1}")
            plt.close()

        # Plot horizontal bar chart for Team 2 (individual output)
        if self.max_speeds_team_2:
            players_team_2 = list(self.max_speeds_team_2.keys())
            speeds_team_2 = list(self.max_speeds_team_2.values())
            
            plt.figure(figsize=(12, 8))

            # Plot horizontal bars with the correct Team 2 color (#d5f0f5)
            bars = plt.barh(np.arange(len(players_team_2)), speeds_team_2, height=0.8, color='#d5f0f5')

            plt.gca().set_yticks(np.arange(len(players_team_2)))
            plt.gca().set_yticklabels(players_team_2, fontsize=10)

            plt.title('Maximum Speed of Players on Team 2', fontsize=14, pad=15)
            plt.xlabel('Max Speed (m/s)', fontsize=12)
            plt.ylabel('Player ID', fontsize=12)
            plt.grid(True, axis='x')

            for bar in bars:
                width = bar.get_width()
                plt.text(width, bar.get_y() + bar.get_height()/2, '{:.2f} m/s'.format(width),
                         ha='left', va='center', fontsize=10, fontweight='bold')

            output_path_team_2 = os.path.join(assets_folder, "team_2_max_speed_chart.png")
            plt.savefig(output_path_team_2, dpi=300, bbox_inches='tight')
            print(f"Max speed chart for Team 2 saved to {output_path_team_2}")
            plt.close()
